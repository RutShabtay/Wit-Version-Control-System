import json
import os.path
import shutil
from os.path import isfile, isdir

from repository import repository

import basicFunctions

from idlelib.IOBinding import encoding

from basicFunctions import is_exists


class wit:
    repository_list = []

    with open("repositoryData.json", 'r') as data:
        repository_data = json.load(data)

        for data in repository_data['repositoryData']:
            new_repository = repository(
                data['path'],
                data['stagingArea'],
                data['commit']
            )

            repository_list.append(new_repository)

    @classmethod
    def wit_init(cls, current_path):
        if not basicFunctions.is_exists(current_path, ".wit"):
            basicFunctions.create_a_new_folder(current_path, ".wit")
            folder_path = os.path.join(current_path, ".wit")
            new_repository = repository(folder_path, "", [])
            cls.repository_list.append(new_repository)
            with open('repositoryData.json', 'r') as data:
                repository_data = json.load(data)

            new_rep = {
                "path": new_repository.path,
                "stagingArea": new_repository.staging_area,
                "commit": new_repository.commit
            }

            repository_data['repositoryData'].append(new_rep)
            with open('repositoryData.json', 'w') as data:
                update_json_data = json.dumps(repository_data, indent=2)
                data.write(update_json_data)

        else:
            print("Reinitialized existing wit repository.")

    @classmethod
    def wit_add(cls, current_path, name):
        if not basicFunctions.is_exists(current_path, ".wit"):
            raise Exception("fatal: not a wit repository (or any of the parent directories): .wit")
        if (not basicFunctions.is_exists(current_path, name)):
            raise Exception("pathspec" + name + "didn't match any file.")
        if (not basicFunctions.is_exists(os.path.join(current_path,".wit"), "stagingArea")):
            basicFunctions.create_a_new_folder(os.path.join(current_path,".wit"),"stagingArea")


        if isdir(os.path.join(current_path,name)):
            if basicFunctions.is_exists(os.path.join(current_path,".wit","stagingArea"),name):
                shutil.move(os.path.join(current_path,name),os.path.join(current_path,".wit","stagingArea",name))
            else:
                shutil.copytree(os.path.join(current_path,".wit","stagingArea",name),os.path.join(current_path,name))



