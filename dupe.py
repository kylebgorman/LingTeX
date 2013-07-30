#!/usr/bin/env python
# 
# Copyright (c) 2012 Kyle Gorman
# 
# Permission is hereby granted, free of charge, to any person obtaining a 
# copy of this software and associated documentation files (the 
# "Software"), to deal in the Software without restriction, including 
# without limitation the rights to use, copy, modify, merge, publish, 
# distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to 
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included 
# in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY 
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Quickly identify duplicate words in a LaTeX document. Will have some 
# false positives, natch.

import fileinput


if __name__ == '__main__':

    last_word = None
    for line in fileinput.input():
        words = line.rstrip().split()
        if not words:
            continue
        # first case
        if last_word == words[0]:
            print 'File {} line {}: {}'.format(fileinput.filename(), 
                                               fileinput.lineno(), 
                                               words[0])
        # normal case
        for j in xrange(1, len(words)):
            if words[j - 1] == words[j]:
                print 'File {} line {}: {}'.format(fileinput.filename(), 
                                               fileinput.lineno(), 
                                               words[j])
        last_word = words[-1]
