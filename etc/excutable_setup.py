import pywintypes
import sys
from cx_Freeze import setup, Executable
import win32

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win64":
    base = "Win64GUI"

setup(  name = "Hooker",
        version = "1.1",
        description = "Lad's hooker",
        options = {"build_exe": build_exe_options},
        executables = [Executable("Hoocker.py", base=base)])
