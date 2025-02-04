import os

def delAllFile(folder):
    fileList = os.listdir(folder)

    for f in fileList:
        filePath = folder + '/'+f

        if os.path.isfile(filePath):
            os.remove(filePath)

        elif os.path.isdir(filePath):
            newFileList = os.listdir(filePath)
            for f1 in newFileList:
                insideFilePath = filePath + '/' + f1

                if os.path.isfile(insideFilePath):
                    os.remove(insideFilePath)
                    
delAllFile('./Result/DailyRunRealTimeStock/')
delAllFile('./Result/DailyFiles/')
