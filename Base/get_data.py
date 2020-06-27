import os, yaml


class GetData:
    @classmethod
    def get_yame_data(self,file_name):
        with open('./Data'+os.sep+file_name)as f:
            return yaml.safe_load(f)
