import shutil
from pathlib import Path
# source = Path("/home/yousifcreates/Downloads/BBSHRRDB Instructor/Github/BBSHRRDB-Batch-1/OOP")
# destination = Path("test")
#
# shutil.copytree(source,
#                 destination,
#                 dirs_exist_ok = True,
#                 ignore = shutil.ignore_patterns
#                     ("Slides/Introduction to OOP in Python - Encapsulation.pptx",
#                                 "Code"
#                     )
#                 )
# print(f"Successfully copied {source} to {destination}")
# shutil.rmtree("test")

# usage = shutil.disk_usage("/")
# print(f"Free space in bytes: {usage.free}")
# print(f"Free space in KB: {usage.free / 1024}")
# print(f"Free space in MB: {usage.free / (1024 * 1024)}")
# print(f"Free space in GB: {usage.free / (1024 * 1024 * 1024)}")
#
# print(f"Total space in GB: {usage.total / (1024 * 1024 * 1024)}")
# print(f"Used space in GB: {usage.used / (1024 * 1024 * 1024)}")
#print(shutil.which("python"))

shutil.make_archive("XYZ", "zip")