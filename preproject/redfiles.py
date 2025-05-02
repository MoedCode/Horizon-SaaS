#!/usr/bin/env python3
import pathlib

# return currant file path
this_path = pathlib.Path(__file__)
dir_path = this_path.resolve().parent
# text file that we want to  read
file_path = dir_path / "text"
file_content  = file_path.read_text()
file_bytes  = file_path.read_bytes()
print(f"file_path: {file_path},\n file_content:\n{file_content}\
    \n content_in_bytes: \n {file_bytes}")

