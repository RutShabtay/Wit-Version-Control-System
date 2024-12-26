import json
import os
import shutil
from os import listdir
from os.path import isfile, isdir, exists
import Exceptions
import basicFunctions
import wit



class commandLine(wit):

    @classmethod
    def wit_init(cls, current_path):
        if not basicFunctions.is_exists(current_path, ".wit"):
            basicFunctions.create_a_new_folder(current_path, ".wit")
            folder_path = os.path.join(current_path, ".wit")
            with open('repositoryData.json', 'r') as data:
                repository_data = json.load(data)

            new_rep = {
                "path": folder_path,
                "version_Hash_Code": "",
                "commit": {}
            }

            repository_data['repositoryData'].append(new_rep)
            with open('repositoryData.json', 'w') as data:
                update_json_data = json.dumps(repository_data, indent=2)
                data.write(update_json_data)
        else:
            raise Exceptions.FileExistsError("Reinitialized existing wit repository.")

    @classmethod
    def wit_add(cls, current_path, name):
        full_path_wit = os.path.join(current_path, ".wit")
        full_path_name = os.path.join(current_path, name)
        if not basicFunctions.is_exists(current_path, ".wit"):
            raise Exceptions.WitNotExistsError("fatal: not a wit repository (or any of the parent directories): .wit")
        if (not basicFunctions.is_exists(current_path, name)):
            raise Exceptions.NotValidPathSpec("pathspec" + name + "didn't match any file.")
        if (not basicFunctions.is_exists(full_path_wit, "stagingArea")):
            basicFunctions.create_a_new_folder(full_path_wit, "stagingArea")

        if isdir(full_path_name):
            if basicFunctions.is_exists(os.path.join(full_path_wit, "stagingArea"), name):
                shutil.rmtree(os.path.join(full_path_wit, "stagingArea", name))
            shutil.copytree(full_path_name, os.path.join(full_path_wit, "stagingArea", name))
        else:
            basicFunctions.create_a_new_file(current_path, name)

    @classmethod
    def wit_commit_m_message(cls, current_path, commit_message):

        if not basicFunctions.is_exists(os.path.join(current_path, ".wit"), "stagingArea"):
            print("nothing added to commit but untracked files present (use wit add to track)")
        else:
            basicFunctions.add_version_to_commit_list(os.path.join(current_path, ".wit"), commit_message)
            shutil.rmtree(os.path.join(current_path, ".wit", "stagingArea"))


    @classmethod
    def wit_log(cls, current_path):
        if not basicFunctions.is_exists(os.path.join(current_path,".wit"),"commit"):
            print("fatal: your current branch 'master' does not have any commits yet")

        with open('repositoryData.json', 'r') as data:
         repository_data = json.load(data)
         for rep in repository_data['repositoryData']:
             if rep['path'] == os.path.join(current_path, ".wit"):
                   for commit_id,commit in rep['commit'].items():
                    print (commit_id + ": " + commit['message']  + " : " + commit['name'])
             break

    @classmethod
    def wit_status(cls,current_path):
         if not basicFunctions.is_exists(os.path.join(current_path,".wit"),"stagingArea"):
             print ("use wit add < file/directory >... to include in what will be committed")
         else:
             for i in listdir(os.path.join(current_path,".wit","stagingArea")):
                 print(i)

    @classmethod
    def wit_checkout(cls,current_path,commit_id):
        with open('repositoryData.json', 'r') as data:
         repository_data = json.load(data)
        for rep in repository_data['repositoryData']:
             if rep['path'] == os.path.join(current_path, ".wit"):
                 rep['version_Hash_Code']=rep['commit'][commit_id]['name']
        with open('repositoryData.json', 'w') as data:
            data.write(json.dumps(repository_data, indent=2))

