from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["pygame", "os", "random_words"], "include_files": ["data"]}

setup(
    name="hang_the_witch",
    version="1",
    description="hang_the_witch",
    options={"build_exe": build_exe_options},
    executables=[Executable("main.py")]
)
