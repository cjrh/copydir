# coding: utf-8
from __future__ import print_function, division
import os
import shutil
import begin


@begin.start
# @begin.convert(ignores=list)
def main(DIR, TARGET_DIR, *ignores):
    if os.path.exists(TARGET_DIR):
        shutil.rmtree(TARGET_DIR)
    patterns = shutil.ignore_patterns(*ignores)
    shutil.copytree(DIR, TARGET_DIR, ignore=patterns)
