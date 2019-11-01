import os
import re
import csv

oldCSVDic = {}
newCSVDic = {}
currentFile = ""

def makeNewFile(data):
    f = open(currentFile, 'w', encoding="utf-8")
    f.write(data)
    f.close()

def readCSV(wholePath, dic, isFirstKey=True):
    f = open(wholePath, "r", encoding="utf-8")
    data = csv.reader(f)
    headers = next(data)
    for row in data:
        if isFirstKey:
            dic[row[0]] = row[1]
        else:
            dic[row[1]] = row[0]

    f.close()

def replaceKey(data):
    tempData = data;
    keyRe = re.compile('{{(.+)}{(.+)}}')
    resList = keyRe.findall(tempData)
    if len(resList) > 0:
        for item in resList:
           msg = oldCSVDic.get(item[0])
           if msg:
               escapedTxt = re.escape('{{'+item[0]+'}{'+item[1]+'}}')
               targetRe = re.compile(escapedTxt)
               key = newCSVDic.get(msg)
               if key:
                tempData = targetRe.sub("{{"+key+"}}", tempData)
        makeNewFile(tempData)

def getWholeString(wholePath):
    f = open(wholePath, "r", encoding="utf-8")
    data = f.read()
    f.close()
    return data

def change(_path, _oldCSV, _newCSV, _ext):
    readCSV(_oldCSV, oldCSVDic)
    readCSV(_newCSV, newCSVDic, False)

    for (path, dir, files) in os.walk(_path):
        currentPath = path.replace("\\", "/") + "/" 
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.' + _ext:
                global currentFile
                currentFile = currentPath + filename
                replaceKey(getWholeString(currentFile))