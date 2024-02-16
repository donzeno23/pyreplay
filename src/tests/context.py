# -*- coding: utf-8 -*-

import sys
import os

dir_path = os.path.join(os.path.dirname(__file__), '..')
print(f"dir_path={dir_path}")
abs_dir_path = os.path.abspath(dir_path)
print(f"absolute dir path={abs_dir_path}")
sys.path.insert(0, abs_dir_path)
print(sys.path)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import replayfactory