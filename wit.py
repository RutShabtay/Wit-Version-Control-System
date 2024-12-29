import json
import os
import shutil
from os import listdir
from os.path import isdir
from abstractWit import abstractWit
import Exceptions
import basicFunctions


# !/usr/bin/env python3


class Wit(abstractWit):

    def cli(self):
        pass

    @staticmethod
    def init():
        if not basicFunctions.is_exists(os.getcwd(), ".wit"):
            basicFunctions.create_a_new_folder(os.getcwd(), ".wit")
            folder_path = os.path.join(os.getcwd(), ".wit")
            repository_data = basicFunctions.load_repository_data_json()
            # create new repository:
            new_rep = {
                "path": folder_path,
                "version_Hash_Code": "",
                "commit": {}
            }
            # insert new repository to data json
            repository_data['repositoryData'].append(new_rep)
            basicFunctions.dumps_to_repository_data_json(repository_data)
        # if wit folder exists:
        else:
            raise Exceptions.FileExistsError("Reinitialized existing wit repository.")

    @staticmethod
    def add(name):
        full_path_wit = os.path.join(os.getcwd(), ".wit")
        full_path_name = os.path.join(os.getcwd(), name)
        # addition directory/file without wit folder isn't valid
        if not basicFunctions.is_exists(os.getcwd(), ".wit"):
            raise Exceptions.WitNotExistsError("fatal: not a wit repository (or any of the parent directories): .wit")
        # try to add file/folder that doesn't exists
        if (not basicFunctions.is_exists(os.getcwd(), name)):
            raise Exceptions.NotValidPathSpec("pathspec" + name + "didn't match any file.")
        if (not basicFunctions.is_exists(full_path_wit, "stagingArea")):
            basicFunctions.create_a_new_folder(full_path_wit, "stagingArea")

        if isdir(full_path_name):
            if basicFunctions.is_exists(os.path.join(full_path_wit, "stagingArea"), name):
                # if file/folder exists remove before add it
                shutil.rmtree(os.path.join(full_path_wit, "stagingArea", name))
            shutil.copytree(full_path_name, os.path.join(full_path_wit, "stagingArea", name))
        else:
            if os.path.isfile(full_path_name):
                basicFunctions.create_a_new_file(os.getcwd(), name)
            else:
                # if Invalid extention
                raise Exceptions.InvalidFileExtension(
                    "File Extention is not valid!!!")

    @staticmethod
    def commit_m_message(message):
        # try to do commit action before stagingArea folder exists
        if not basicFunctions.is_exists(os.path.join(os.getcwd(), ".wit"), "stagingArea"):
            print("nothing added to commit but untracked files present (use wit add to track)")
        else:
            # calling to a function that adding a version to commit list:
            basicFunctions.add_version_to_commit_list(os.path.join(os.getcwd(), ".wit"), message)
            # deleting staging area folder due to there is no new changes:
            shutil.rmtree(os.path.join(os.getcwd(), ".wit", "stagingArea"))

    @staticmethod
    def log():
        if not basicFunctions.is_exists(os.path.join(os.getcwd(), ".wit"), "commit"):
            print("fatal: your current branch 'master' does not have any commits yet")
            # moving on the commits list and print the version:
            repository_data = basicFunctions.load_repository_data_json()
            for rep in repository_data['repositoryData']:
                if rep['path'] == os.path.join(os.getcwd(), ".wit"):
                    for commit_id, commit in rep['commit'].items():
                        print (commit_id + ": " + commit['message'] + " : " + commit['name'])
                break

    @staticmethod
    def status():
        # if the stagingArea folder is empty:
        if not basicFunctions.is_exists(os.path.join(os.getcwd(), ".wit"), "stagingArea"):
            print ("use wit add < file/directory >... to include in what will be committed")
        else:
            # print the stagingArea files anf folders:
            for i in listdir(os.path.join(os.getcwd(), ".wit", "stagingArea")):
                print(i)

    @staticmethod
    def checkout(commit_id):
        # calling to a function that loading the data json:
        repository_data = basicFunctions.load_repository_data_json()
        # moving the repository data list and update the appropriate version hash code:
        for rep in repository_data['repositoryData']:
            if rep['path'] == os.path.join(os.getcwd(), ".wit"):
                sorted_keys = sorted(map(int, rep['commit'].keys()))
                last_hash_code = str(sorted_keys[-1])
                # if commit_id greater than last commit_id or less than zero:
                if last_hash_code < commit_id or last_hash_code < 0:
                    raise Exceptions.InvalidCommitId("Commit Id Not Valid!!!")
                rep['version_Hash_Code'] = rep['commit'][commit_id]['name']
        # calling to a function that update the repository data json:
        basicFunctions.dumps_to_repository_data_json(repository_data)
