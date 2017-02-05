import settingloader

class clientFileManager:
    standard_file_path = "%USERPROFILE%\\appdata\\local\\tibia"

    @staticmethod
    def getSettingFile(configFile = None):
        filePath = None
        if configFile != None:
            filePath = settingloader.getClientPath((configFile))
        if filePath != None:
            path = filePath + "\\packages\\tibia\\conf\\clientoptions.json"
        else:
            path = "%USERPROFILE%\\appdata\\local\\tibia\\packages\\tibia\\conf\\clientoptions.json"

        with open(path) as content:
            return content.read()