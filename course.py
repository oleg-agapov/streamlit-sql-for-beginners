from __future__ import annotations

from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent
LESSONS_ROOT = ROOT / "app_pages" / "lessons"
REQUIRED_METADATA = frozenset({"title", "module", "order", "level", "minutes"})
LEVEL_LABELS = {
    0: "Module 0",
    1: "Level 1",
    2: "Level 2",
    3: "Level 3",
    4: "Level 4",
    5: "Level 5",
}
_PAGE_REGISTRY: dict[str, st.Page] = {}


class LessonParseError(ValueError):
    """Raised when a lesson file does not follow the course authoring contract."""


@dataclass(frozen=True)
class Lesson:
    title: str
    module: str
    order: int
    level: int
    minutes: int
    slug: str
    body: str
    content_path: Path

    @property
    def key(self) -> str:
        return f"lesson_{self.level}_{self.order}"

    @property
    def route(self) -> str:
        return f"lesson-{self.level}-{self.slug}"


def _parse_error(content_path: Path, message: str) -> LessonParseError:
    return LessonParseError(f"{content_path}: {message}")


def _split_lesson(text: str, content_path: Path = Path("<lesson>")) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise _parse_error(content_path, "front matter must start with '---'")
    parts = text.split("---", 2)
    if len(parts) != 3:
        raise _parse_error(content_path, "front matter is missing its closing '---'")

    _, front_matter, body = parts
    metadata: dict[str, str] = {}
    for line_number, line in enumerate(front_matter.strip().splitlines(), start=2):
        if ":" not in line:
            raise _parse_error(content_path, f"metadata line {line_number} has no ':'")
        key, value = (part.strip() for part in line.split(":", 1))
        if not key or not value:
            raise _parse_error(
                content_path, f"metadata line {line_number} has an empty key or value"
            )
        if key in metadata:
            raise _parse_error(content_path, f"metadata key {key!r} is duplicated")
        metadata[key] = value

    missing = REQUIRED_METADATA - metadata.keys()
    unknown = metadata.keys() - REQUIRED_METADATA
    if missing:
        raise _parse_error(content_path, f"missing metadata: {', '.join(sorted(missing))}")
    if unknown:
        raise _parse_error(content_path, f"unknown metadata: {', '.join(sorted(unknown))}")

    body = body.strip()
    if not body:
        raise _parse_error(content_path, "lesson body is empty")
    heading = f"# {metadata['title']}"
    if body.startswith(heading):
        body = body[len(heading) :].lstrip()
    return metadata, body


def _positive_int(metadata: Mapping[str, str], field: str, content_path: Path) -> int:
    try:
        value = int(metadata[field])
    except ValueError as error:
        raise _parse_error(content_path, f"{field!r} must be an integer") from error
    if value <= 0 and field != "level":
        raise _parse_error(content_path, f"{field!r} must be positive")
    if field == "level" and value not in LEVEL_LABELS:
        raise _parse_error(content_path, f"level must be one of {sorted(LEVEL_LABELS)}")
    return value


def _read_lesson(content_path: Path) -> Lesson:
    metadata, body = _split_lesson(content_path.read_text(encoding="utf-8"), content_path)
    filename_parts = content_path.stem.split("-", 1)
    if len(filename_parts) != 2 or not filename_parts[1]:
        raise _parse_error(content_path, "filename must be '<order>-<slug>.md'")

    level = _positive_int(metadata, "level", content_path)
    module_prefix = f"{level} —"
    if not metadata["module"].startswith(module_prefix):
        raise _parse_error(content_path, f"module must start with {module_prefix!r}")

    return Lesson(
        title=metadata["title"],
        module=metadata["module"],
        order=_positive_int(metadata, "order", content_path),
        level=level,
        minutes=_positive_int(metadata, "minutes", content_path),
        slug=filename_parts[1],
        body=body,
        content_path=content_path,
    )


def _assert_unique(lessons: Iterable[Lesson], attribute: str) -> None:
    seen: dict[object, Path] = {}
    for lesson in lessons:
        value = getattr(lesson, attribute)
        if value in seen:
            first_path = seen[value]
            message = (
                f"{lesson.content_path}: duplicate {attribute} {value!r}; "
                f"first used by {first_path}"
            )
            raise LessonParseError(message)
        seen[value] = lesson.content_path


def load_course(lessons_root: Path = LESSONS_ROOT) -> tuple[Lesson, ...]:
    """Load and validate lessons. Deliberately uncached so author edits appear on rerun."""

    lessons = tuple(
        sorted(
            (_read_lesson(path) for path in lessons_root.glob("module-*/*.md")),
            key=lambda lesson: (lesson.level, lesson.order),
        )
    )
    if not lessons:
        raise LessonParseError(f"{lessons_root}: no lesson files found")
    _assert_unique(lessons, "key")
    _assert_unique(lessons, "route")
    return lessons


def module_name(module: str) -> str:
    level_text, separator, title = module.partition(" — ")
    if not separator or not level_text.isdigit() or int(level_text) not in LEVEL_LABELS:
        return module
    return f"{LEVEL_LABELS[int(level_text)]} · {title}"


def register_page(route: str, page: st.Page) -> None:
    _PAGE_REGISTRY[route] = page


def page_for(lesson: Lesson) -> st.Page:
    return _PAGE_REGISTRY[lesson.route]


def completed_keys(lessons: Iterable[Lesson]) -> list[str]:
    return [lesson.key for lesson in lessons if st.session_state.get(lesson.key)]


def progress_query(lessons: Iterable[Lesson]) -> dict[str, str]:
    completed = completed_keys(lessons)
    return {"completed": ",".join(completed)} if completed else {}


def initialize_progress(lessons: Iterable[Lesson]) -> None:
    if st.session_state.get("_progress_initialized"):
        return
    valid_keys = {lesson.key for lesson in lessons}
    saved = set(st.query_params.get("completed", "").split(","))
    for key in valid_keys & saved:
        st.session_state[key] = True
    st.session_state["_progress_initialized"] = True


def save_progress(lessons: tuple[Lesson, ...]) -> None:
    query = progress_query(lessons)
    if query:
        st.query_params["completed"] = query["completed"]
    elif "completed" in st.query_params:
        del st.query_params["completed"]


def lesson_nav_title(lesson: Lesson) -> str:
    check = " :green[:material/check_circle:]" if st.session_state.get(lesson.key) else ""
    return f"{lesson.order}. {lesson.title}{check}"


def render_lesson(lesson: Lesson) -> None:
    lessons = load_course()
    index = lessons.index(lesson)

    st.caption(f"{module_name(lesson.module).upper()} · LESSON {lesson.order}")
    st.title(lesson.title)
    st.caption(f":material/schedule: About {lesson.minutes} minutes")
    st.divider()
    st.markdown(lesson.body)

    st.divider()
    st.checkbox(
        "I finished this lesson",
        key=lesson.key,
        help="Progress is saved in the page URL so it survives reloads and can be bookmarked.",
        on_change=save_progress,
        args=(lessons,),
    )
    if st.session_state.get(lesson.key):
        st.success("Lesson complete — nice work!")

    previous_lesson = lessons[index - 1] if index > 0 else None
    next_lesson = lessons[index + 1] if index < len(lessons) - 1 else None
    previous_col, next_col = st.columns(2)
    query = progress_query(lessons)
    with previous_col:
        if previous_lesson:
            st.page_link(
                page_for(previous_lesson),
                label=f"← {previous_lesson.title}",
                width="stretch",
                query_params=query,
            )
    with next_col:
        if next_lesson:
            st.page_link(
                page_for(next_lesson),
                label=f"{next_lesson.title} →",
                width="stretch",
                query_params=query,
            )


def create_lesson_page(lesson: Lesson) -> Callable[[], None]:
    """Create the callable Streamlit uses as a page for one Markdown lesson."""

    def page() -> None:
        render_lesson(lesson)

    return page
