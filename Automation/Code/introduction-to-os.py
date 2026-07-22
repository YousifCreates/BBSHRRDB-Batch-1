# # importing os
# import os
# # destination = "example.txt"
# # source = "renamed_file.txt"
# #
# # # os.rename(src, dst)
# # os.rename(source, destination)
# #
# # items = os.listdir(os.getcwd())
# # print(items)
#
# # file_path = "/home/yousifcreates/Downloads/BBSHRRDB Instructor/Github/BBSHRRDB-Batch-1/Automation/Code/example.txt"
# # dir_path = os.getcwd()
# # exists = os.path.exists(file_path)
# # print(exists)
# #
# # if exists:
# #     # os.remove(file_path)
# #     print(os.path.isfile(file_path))
# #     print(os.path.isfile(dir_path))
# #     print(os.path.isdir(dir_path))
# #     print(os.path.isdir(file_path))
#
# video ="/media/yousifcreates/339b14bb-e7ae-4348-b1dd-b0b8a896b600/Special Kalam Syeda-e-Pak Hazrat Bibi Fatima - New Tarz - Owais Raza Qadri - 2025(720P_HD).mp4"
# if os.path.ex
#ists(video):
#     size_bytes = os.path.getsize(video)
#     print(f"Video size in Bytes: {size_bytes}")
#     file_size_mbs = size_bytes / (1024 * 1024)
#     print(f"Video size in MBs: {file_size_mbs:.2f} MBs")
import os
def create_project(project_name):
    base_dir = os.path.join(os.getcwd(), project_name)
    if not os.path.exists(base_dir):
        os.mkdir(base_dir)
        print(f"Successfully created the directory {base_dir}")
    folders = ['code', 'images', 'api', 'ignored_files']
    for folder in folders:
        if not os.path.exists(os.path.join(base_dir, folder)):
            os.mkdir(os.path.join(base_dir, folder))
        else:
            print(f"Folder {folder} already exists")

create_project("test")







