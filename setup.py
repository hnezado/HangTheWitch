from cx_Freeze import setup, Executable

# To generate a new build:
# pip install --upgrade cx_Freeze
# python setup.py build

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': ["pygame", "random_words"], 'include_files': ["data"]}

setup(name='hangTheWitch',
      version='2.1',
      description='Hang The Witch game',
      options={'build_exe': build_options},
      executables=[
            Executable(
                  script="main.py",
                  target_name="hangTheWitch",
                  base="Win32GUI",
                  icon="main.ico"
            )]
      )
