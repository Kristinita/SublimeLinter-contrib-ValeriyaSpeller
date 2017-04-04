#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sasha Chernykh
# Copyright (c) 2017 Sasha Chernykh
#
# License: MIT
#

"""This module exports the ValeriyaSpeller plugin class."""

from SublimeLinter.lint import NodeLinter
"""NodeLinter

ValeriyaSpeller — Node.js module.
"""
from SublimeLinter.lint import highlight
"""highlight

Highlight typos as warnings or errors.
http://www.sublimelinter.com/en/latest/linter_attributes.html#default-type
I select warnings, because yaspeller have false positives, special in names
Own
"""
from SublimeLinter.lint import util
"""util

Errors reporting type.
http://www.sublimelinter.com/en/latest/linter_attributes.html#error-stream
I test yaspeller and get STREAM_BOTH.
"""


class ValeriyaSpeller(NodeLinter):
    """Provides an interface to ValeriyaSpeller."""

    syntax = ('*')
    cmd = 'yaspeller --check-yo --find-repeat-words --ignore-digits --ignore-latin --ignore-roman-numerals --ignore-uppercase --ignore-urls'
    npm_name = 'yaspeller'
    default_type = highlight.WARNING
    executable = None
    error_stream = util.STREAM_BOTH
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 3.1.0'
    regex = r'''(?xi)
        ((^(?P<error_stream>.+):\s\d+$\r?\n)?)
        (^\d+\.\s.+\((?P<line>\d+):(?P<col>\d+),(
        (\scount:\s\d+,)?)((\sen:\s.+,)?)((\ssuggest:\s)?)
        ((?P<message>.+)?)\)$\r?\n)
    '''
    multiline = True
    selectors = {
        '*': 'text.html.markdown, text.plain, text.tex.latex, comment'
    }
    word_re = None
    defaults = {}
    line_col_base = (1, 1)
    inline_settings = None
    inline_overrides = None
    comment_re = r'\s*/[/*]'
