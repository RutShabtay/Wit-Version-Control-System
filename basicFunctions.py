import os
import json
import datetime
import shutil
from os import listdir
from os.path import isdir


# function to check if specific file/folder exist
def is_exists(path, folder_name):
    folder_path = os.path.join(path, folder_name)
    return os.path.exists(folder_path)


# function to create a new folder
def create_a_new_folder(path, folder_name):
    newPath = os.path.join(path, folder_name)
    os.makedirs(newPath)


# function to create a new file
def create_a_new_file(path, file_name):
    with open(os.path.join(path, ".wit", "stagingArea", file_name), 'w') as file:
        with open(os.path.join(path, file_name), "r") as reading_file:
            file.write(reading_file.read())


# function to add a new version to commit
def add_version_to_commit_list(path, commit_message):
    last_hash_code = ""
    repository_data = load_repository_data_json()

    # moving on the repository data list
    for i in repository_data['repositoryData']:
        if i['path'] == path:
            # if the commit dictionary is empty:
            if not i['commit']:
                last_hash_code = "-1"
                # create a commit folder
                create_a_new_folder(path, "commit")
            else:
                # sort the commit keys
                sorted_keys = sorted(map(int, i['commit'].keys()))
                # get the last key
                last_hash_code = str(sorted_keys[-1])
            # save the name of the last commit
            last_commit = str(datetime.date.today()) + " Code-" + str(int(last_hash_code) + 1);
            # create a new version
            i['commit'][str(int(last_hash_code) + 1)] = {"message": commit_message,
                                                         "name": last_commit
                                                         }
        # save the name of the version folder to merge
        folder_name_to_merge = i['version_Hash_Code']
        # if it's the first commit:
        if folder_name_to_merge == "":
            create_a_new_folder(os.path.join(path, "commit"), last_commit)
        else:
            directory = os.path.join(path, "commit", folder_name_to_merge)
            shutil.copytree(directory, os.path.join(path, "commit", last_commit))
            # calling to a function that merge the stagingArea folder to the new version:
        merge_spec_version_with_staging_area(path, os.path.join(path, "commit", last_commit))
        # update the version_Hash_Code to the next version:
        i["version_Hash_Code"] = str(datetime.date.today()) + " Code-" + str(int(last_hash_code) + 1)

        break
    # calling to a func that update the repository data json
    dumps_to_repository_data_json(repository_data)


def merge_spec_version_with_staging_area(path, dest_path_to_merge):
    staging_area_path = os.path.join(path, "stagingArea")
    # moving the stagingArea files and folders:
    for i in listdir(staging_area_path):
        if isdir(os.path.join(staging_area_path, i)):
            if is_exists(dest_path_to_merge, i):
                # delete exists folder:
                shutil.rmtree(os.path.join(dest_path_to_merge, i))
            shutil.copytree(os.path.join(staging_area_path, i), os.path.join(dest_path_to_merge, i))

        else:
            if is_exists(dest_path_to_merge, i):
                # delete exists file:
                os.remove(os.path.join(dest_path_to_merge, i))
            shutil.copy(os.path.join(staging_area_path, i), os.path.join(dest_path_to_merge, i))


# return repository data json content:
def load_repository_data_json():
    with open(r'C:\Users\user1\Desktop\Python\FinalProject\pythonProject\repositoryData.json', 'r') as data:
        return json.load(data)


# update repository data json:
def dumps_to_repository_data_json(repository_data):
    with open(r'C:\Users\user1\Desktop\Python\FinalProject\pythonProject\repositoryData.json', 'w') as data:
        update_json_data = json.dumps(repository_data, indent=2)
        data.write(update_json_data)
