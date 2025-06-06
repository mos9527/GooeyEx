import unittest
from argparse import ArgumentParser
from itertools import *

from GooeyEx.tests.harness import instrumentGooey
from GooeyEx.tests import *


class TestGooeyHeader(unittest.TestCase):

    def make_parser(self):
        parser = ArgumentParser(description="description")
        return parser

    def test_header_visibility(self):
        """
        Test that the title and subtitle components correctly show/hide
        based on config settings.

        Verifying Issue #497
        """
        for testdata in self.testcases():
            with self.subTest(testdata):
                with instrumentGooey(self.make_parser(), **testdata) as (
                    app,
                    frame,
                    gapp,
                ):
                    frame: wx.Frame = frame

                    self.assertEqual(
                        frame.FindWindowByName("header_title").IsShown(),
                        testdata.get("header_show_title", True),
                    )

                    self.assertEqual(
                        frame.FindWindowByName("header_subtitle").IsShown(),
                        testdata.get("header_show_subtitle", True),
                    )

    def test_header_string(self):
        """
        Verify that string in the buildspec get correctly
        placed into the UI.
        """
        parser = ArgumentParser(description="Foobar")
        with instrumentGooey(parser, program_name="BaZzEr") as (app, frame, gapp):
            self.assertEqual(
                frame.FindWindowByName("header_title").GetLabel(), "BaZzEr"
            )
            self.assertEqual(
                frame.FindWindowByName("header_subtitle").GetLabel(), "Foobar"
            )

    def testcases(self):
        """
        Generate a powerset of all possible combinations of
        the header parameters (empty, some present, all present, all combos)
        """
        iterable = product(["header_show_title", "header_show_subtitle"], [True, False])
        allCombinations = list(powerset(iterable))
        return [{k: v for k, v in args} for args in allCombinations]


def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


if __name__ == "__main__":
    unittest.main()
