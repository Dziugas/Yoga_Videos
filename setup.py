from cx_Freeze import setup, Executable

setup(name ='yoga', version ='0.1', description ='Parse stuff', executables = [Executable("yoga_videos.py")])