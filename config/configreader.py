from jproperties import Properties
import os

class ConfigFileReader:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    property_file_path = os.path.join(script_directory, '../propertyfiles/Configuration.properties')

    def __init__(self):
        try:
            self.properties = Properties()
            with open(self.property_file_path, 'rb') as config_file:
                self.properties.load(config_file)
        except Exception as e:
            print(e)
            raise RuntimeError(f"Configuration.properties file not found in the location {self.property_file_path}")

    @classmethod
    def get_config_file_reader(cls):
        return cls()

    def get_url(self):
        url = self.properties.get("url")
        if url is not None:
            return url.data  # Access the value using .data
        else:
            raise RuntimeError(f"URL not found in the properties file {self.property_file_path}")

    def get_wait(self):
        wait=self.properties.get("wait")
        if wait is not None:
            return wait.data
        else:
            raise RuntimeError(f"wait not found in the properties file {self.property_file_path}")
