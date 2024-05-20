"""JAV Config V1.0
The class handles config settings of JAV Star Name Finder.
It can save setting to a JSON file, and load from it.
It also has a few constants.
"""
import json
import os


class JAVConfig:
    def __init__(self):
        self.star_position = "파일 뒷부분"
        self.separator = "#"
        self.path_not_set = "*아직 선택되지 않음*"
        self.working_path = self.path_not_set
        self.save_file_name = "JAV_Config.json"

    def save_to_file(self):
        data = {
            "star_position": self.star_position,
            "separator": self.separator,
            "working_path": self.working_path
        }
        with open(self.save_file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)

    def load_from_file(self) -> bool:
        if os.path.isfile(self.save_file_name):
            with open(self.save_file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                if len(data["star_position"]) > 0:
                    self.star_position = data["star_position"]
                    self.separator = data["separator"]

                    if len(data["working_path"]) > 1:
                        self.working_path = data["working_path"]
                    else:
                        self.working_path = self.path_not_set
                    return True
                else:
                    return False
        else:
            return True


if __name__ == "__main__":
    JAV_config = JAVConfig()

    print(JAV_config.separator)
    print(JAV_config.working_path)

