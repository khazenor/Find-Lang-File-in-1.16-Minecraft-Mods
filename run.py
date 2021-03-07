import os
import zipfile
import configparser

def logStart(logFile):
    f = open(logFile, "w")
    f.close()

def log(mod, logFile):
    with open(logFile,"a") as f:
        f.write(f"{mod}\n")

def findLangFilesInMods(modFolder, langTag, logFile):
    mods = os.listdir(modFolder)
    logStart(logFile)
    for mod in mods:
        if ".jar" in mod:
            modDir = os.path.join(modFolder, mod)
            zip = zipfile.ZipFile(modDir, "r")
            filedirs = list(zip.NameToInfo.keys())
            for filedir in filedirs:
                if langTag in filedir:
                    log(mod, logFile)
                    break

def run():
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    modFolder = parser["configs"]["modsFolder"]
    logFile = parser["configs"]["logFileName"]
    langTag = parser["configs"]["langTag"]
    findLangFilesInMods(modFolder, langTag, logFile)


if __name__ == "__main__":
    run()