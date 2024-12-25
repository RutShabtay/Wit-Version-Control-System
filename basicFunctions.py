import os


def is_exists(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    return os.path.exists(folder_path)


def create_a_new_folder(path, folder_name):

    newPath = os.path.join(path, folder_name)
    os.makedirs(newPath)

# def create_a_new_file(path,file_name)
