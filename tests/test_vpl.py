import unittest
import os
import sys
from textwrap import dedent
from contextlib import redirect_stdout
import io

pedal_library = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, pedal_library)

from pedal.plugins.vpl import find_file, resolve, strip_tags
from pedal.source import next_section, verify_section
from pedal.report import MAIN_REPORT
from pedal.report.imperative import compliment, clear_report

class TestVPL(unittest.TestCase):
    def test_vpl(self):
        find_file('tests/datafiles/student_example.py', sections=True)
    
    def test_html_conversion(self):
        self.assertEqual(strip_tags(dedent('''
        <h1>Section 1</h1>
        This is some text.
        <pre>>a = 0
        None</pre>
        Here we go.
        ''')), dedent('''
        -Section 1
        This is some text.
        >>a = 0
        >None
        Here we go.
        '''))
    
    def test_resolve(self):
        clear_report()
        find_file('tests/datafiles/student_example.py', sections=True)
        # Part 0
        # Part 1
        next_section()
        verify_section()
        # Part 2
        next_section()
        verify_section()
        compliment('Hey, not a bad job!')
        # Part 3
        next_section()
        verify_section()
        # Part 4
        next_section()
        verify_section()
        f = io.StringIO()
        with redirect_stdout(f):
            resolve()
        output = f.getvalue()
        self.assertEqual(output, dedent('''
        <|--
        -##### Part 1
        -##### Part 2
        Hey, not a bad job!
        -##### Part 3
        Invalid syntax on line 13
        -Overall
        Incomplete
        --|>
        Grade :=>> 0
        '''[1:]))

if __name__ == '__main__':
    unittest.main(buffer=False)