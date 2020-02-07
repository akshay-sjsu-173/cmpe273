import os, time
from heapq import merge

def sortNumbers(fl):
    content = open(inputDir + fl, "r").read().split("\n")
    content.remove('')
    listOfNumbers = [int(x) for x in content]
    listOfNumbers.sort()
    time.sleep(1) #Sleep is being used to display proficiency of async over sync operations
    return listOfNumbers

inputDir,sortedList = "input/", []

allInputFiles = [fl for fl in os.listdir(inputDir) if os.path.isfile(os.path.join(inputDir, fl))]
result = []
for fl in allInputFiles:
    result.append(sortNumbers(fl))
for i in range(len(result)):
    sortedList = list(merge(sortedList, result[i]))
fl = open("output/sorted.txt", "w+")
for i in sortedList:
    fl.write(str(i)+"\n")
