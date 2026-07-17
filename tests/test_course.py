import sys
import tempfile
import types
import unittest
from pathlib import Path

# The content loader only needs Streamlit at render time. A small stub keeps these
# unit tests fast and independent of the UI runtime.
sys.modules.setdefault("streamlit", types.SimpleNamespace(Page=object))

from course import (  # noqa: E402
    LESSONS_ROOT,
    LessonParseError,
    _read_lesson,
    _split_lesson,
    load_course,
)


class LessonParserTests(unittest.TestCase):
    def test_all_repository_lessons_load_and_are_unique(self) -> None:
        lessons = load_course(LESSONS_ROOT)
        self.assertEqual(42, len(lessons))
        self.assertEqual(len(lessons), len({lesson.key for lesson in lessons}))
        self.assertEqual(len(lessons), len({lesson.route for lesson in lessons}))

    def test_title_heading_is_removed(self) -> None:
        text = """---
title: Intro
module: 0 — Start
order: 1
level: 0
minutes: 2
---
# Intro

Body
"""
        metadata, body = _split_lesson(text)
        self.assertEqual("Intro", metadata["title"])
        self.assertEqual("Body", body)

    def test_invalid_metadata_reports_the_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "01-broken.md"
            path.write_text("---\ntitle: Broken\n---\nBody", encoding="utf-8")
            with self.assertRaisesRegex(LessonParseError, "01-broken.md.*missing metadata"):
                _read_lesson(path)

    def test_empty_course_is_an_error(self) -> None:
        with (
            tempfile.TemporaryDirectory() as directory,
            self.assertRaisesRegex(LessonParseError, "no lesson files found"),
        ):
            load_course(Path(directory))


if __name__ == "__main__":
    unittest.main()
