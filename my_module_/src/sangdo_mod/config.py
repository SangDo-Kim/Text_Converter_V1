"""Config V1.1
The class handles config settings.
It can save setting to a JSON file, and load from it.
Config class doesn't have any attribute except for filename to save (config.json).
You can make a subclass to add attributes to save and load.
Example:
class MyConfig(Config):
    def __init__(self):
        super().__init__()
        self.source_folder = ""
        self.target_folder = ""
        self.pattern = ""

Config.load_from_file() return True or False to notify if loading was successful.

V1.1:
- Change Config class. Now users need to subclass it and add attributes

V1.11:
- Config class can now receive config filename. Still, default value is "config.json".

V1.12:
- When opening a json file, now encoding='utf-8'.

"""
import json


class Config:
    def __init__(self, filename="config.json"):
        self.filename = filename

    def save_to_file(self):
        attributes_dict = self.__dict__
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(attributes_dict, file, ensure_ascii=False, indent="\t")

    def load_from_file(self) -> bool:
        try:
            with open(self.filename, "r", encoding='utf-8') as file:
                attributes_dict = json.load(file)
            for key, value in attributes_dict.items():
                setattr(self, key, value)
            return True
        except FileNotFoundError:
            return False


if __name__ == "__main__":
    class MyConfig(Config):
        def __init__(self):
            super().__init__()
            self.source_folder = ""
            self.target_folder = ""
            self.pattern = ""


    my_config = MyConfig()
    my_config.source_folder = "D:/"
    my_config.target_folder = "E:/"
    my_config.pattern = "*.*"
    print(my_config.__dict__)
    my_config.save_to_file()

    my_config.source_folder = "D:/test"
    print(my_config.__dict__)

    my_config.load_from_file()
    print(my_config.__dict__)


