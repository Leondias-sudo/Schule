import csv
import os

def GetFilePath(in_Path : str) -> list[str]:
    Files:list[str] = os.listdir(in_Path)
    NewList:list[str] = []
    for file in Files:
        if file.endswith(".csv"):
            NewList.append(file)

    return NewList

def SelectFile(in_List:list) -> str:
    try:
        index:int = GetIndexOfFileList()
        if index is not None:
            return str(in_List[index])
        SelectFile(in_List)
    except IndexError as e:
        print("Diesen Index gibt es nicht")
        SelectFile(in_List)

def GetIndexOfFileList()-> int:
    index = input("Wähle Datei mit dem Index ")
    try:
        return int(index)
    except Exception as e:
        print("Bitte eine Zahl Eingeben")
        GetIndexOfFileList()

def ReadCsv(in_Path:str, in_File:str) -> list[float]:
    with open(in_Path+'/'+in_File, 'r') as csvDatei:
        csvReaderObject = csv.reader(csvDatei)
        listcsvs:list[int] = []

        for row in csvReaderObject:
            for v in row:
                for c in v:
                    try:
                        if int(c):
                            listcsvs.append(c)
                            print(f"{c}")
                    except:
                        continue
    return listcsvs

def GetAverage(in_List:list[float]) -> float:
    tempList:list[int] = []
    for v in in_List:
        tempList.append(int(v))
    
    return sum(tempList) / len(tempList) 

PATH:str = "/home/leon/Schule/Programieren/Python/LF8/CSV Datei Einlesen"

ListFiles:list[str] = GetFilePath(PATH)

for file in ListFiles:
    print(file)
 
ListValues:list[float] = ReadCsv(PATH, SelectFile(ListFiles))

print(f"{GetAverage(ListValues)}")