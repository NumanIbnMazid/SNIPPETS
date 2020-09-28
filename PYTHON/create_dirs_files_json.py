import json
import os

class FilesFoldersConfig:
    # requests and responses sample save directory
    req_res_parent_dir = "test_files_folders/"
    
    def get_req_res_target_dir(self, gds_name="other"):
        """
        Getter method for getting resquests and responses save directory.
        params => gds_name (string)
        return => dict => {"gds_name": {"req": "example/requests/directory/", "res": "example/response/directory/"}}
        """
        responses_target_dir = self.req_res_parent_dir + "responses/"
        requests_target_dir = self.req_res_parent_dir + "requests/"
        dirs = {}
        dirs[gds_name.lower()] = {
            "req": requests_target_dir + gds_name.lower() + "/",
            "res": responses_target_dir + gds_name.lower() + "/"
        }
        return dirs

    def create_dirs_files(self, filename):
        if not os.path.exists(os.path.dirname(filename)):
            try:
                # os.makedirs(os.path.dirname(filename))
                # __init__.py file generation
                dirs = filename.split("/")
                target_dirname = ""
                for idx, single_dir in enumerate(dirs):
                    if not idx == len(dirs) - 1:
                        target_dirname = target_dirname + single_dir + "/"
                        if not os.path.exists(os.path.dirname(target_dirname)):
                            os.makedirs(os.path.dirname(target_dirname))
                            target_filename = target_dirname + "__init__.py"
                            f = open(target_filename, "w+")
                            f.close()
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    def generate_json(self, gds="other", isReq=False, filename="test", data=None, files=None):
        """
        generate_json() => Generates json file.
        params => gds (string), isReq (boolean), filename (string), data (any), files (list)
        """
        if files == None:
            target_dir = self.get_req_res_target_dir(gds)
            data_type = "req" if isReq == True else "res"
            filename = target_dir[gds][data_type] + filename
            # create dirs and files
            self.create_dirs_files(filename=filename)
            # generate json file
            with open(filename, "w") as outfile:
                json.dump(data, outfile, indent=4)
        else:
            self.generate_JSON_files_from_list(files=files)

    def generate_JSON_files_from_list(self, files=[]):
        """
        generate_JSON_files() => Generates json files.
        params => files (list)
        """
        # loop through files
        for file in files:
            # generate json file
            self.generate_json(
                gds=file["gds"], isReq=file["isReq"], filename=file["filename"], data=file["data"], files=None
            ) 


conf = FilesFoldersConfig()

files = [
    {
        "gds": "tester", "isReq": True, "filename": "test_file_1.json", "data": {"key1": "value1", "key2": "value2"}
    },
    {
        "gds": "tester", "isReq": False, "filename": "test_file_2.json", "data": {"key3": "value3", "key4": "value4"}
    },
    {
        "gds": "tester", "isReq": False, "filename": "test_file_3.json", "data": {"key5": "value5", "key6": "value6"}
    },
]

conf.generate_json(files=files)
