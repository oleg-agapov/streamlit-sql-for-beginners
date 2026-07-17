from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Callable

import streamlit as st

ROOT = Path(__file__).parent
LESSONS_ROOT = ROOT / "app_pages" / "lessons"


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
        return f"/lesson-{self.level}-{self.slug}"


def _split_lesson(text: str) -> tuple[dict[str, str], str]:
    _, front_matter, body = text.split("---", 2)
    metadata = {}
    for line in front_matter.strip().splitlines():
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip()

    body = body.strip()
    heading = f"# {metadata['title']}"
    if body.startswith(heading):
        body = body[len(heading) :].lstrip()
    return metadata, body


def _read_lesson(content_path: Path) -> Lesson:
    metadata, body = _split_lesson(content_path.read_text(encoding="utf-8"))
    slug = content_path.stem.split("-", 1)[1]
    return Lesson(
        title=metadata["title"],
        module=metadata["module"],
        order=int(metadata["order"]),
        level=int(metadata["level"]),
        minutes=int(metadata["minutes"]),
        slug=slug,
        body=body,
        content_path=content_path,
    )


@lru_cache(maxsize=1)
def load_course() -> tuple[Lesson, ...]:
    lessons = [_read_lesson(path) for path in LESSONS_ROOT.glob("module-*/*.md")]
    return tuple(sorted(lessons, key=lambda lesson: (lesson.level, lesson.order)))


def module_name(module: str) -> str:
    return module.replace("0 —", "Module 0 ·").replace("1 —", "Level 1 ·").replace(
        "2 —", "Level 2 ·"
    ).replace("3 —", "Level 3 ·").replace("4 —", "Level 4 ·").replace(
        "5 —", "Level 5 ·"
    )


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
        help="Your progress is kept for this browser session.",
    )
    if st.session_state.get(lesson.key):
        st.success("Lesson complete — nice work!")

    previous_lesson = lessons[index - 1] if index > 0 else None
    next_lesson = lessons[index + 1] if index < len(lessons) - 1 else None
    previous_col, next_col = st.columns(2)
    with previous_col:
        if previous_lesson:
            st.link_button(
                f"← {previous_lesson.title}", previous_lesson.route, width="stretch"
            )
    with next_col:
        if next_lesson:
            st.link_button(f"{next_lesson.title} →", next_lesson.route, width="stretch")


def create_lesson_page(lesson: Lesson) -> Callable[[], None]:
    """Create the callable Streamlit uses as a page for one Markdown lesson."""

    def page() -> None:
        render_lesson(lesson)

    return page
