import asyncio, os
from heapq import merge

async def sortNumbers(fl):
    content = open(inputDir + fl, "r").read().split("\n")
    content.remove('')
    listOfNumbers = [int(x) for x in content]
    listOfNumbers.sort()
    await asyncio.sleep(1)
    return listOfNumbers

async def main():
    sortedList = []
    allInputFiles = [fl for fl in os.listdir(inputDir) if os.path.isfile(os.path.join(inputDir, fl))]
    result = await asyncio.gather(*(sortNumbers(fl) for fl in allInputFiles))
    for i in range(len(result)):
        sortedList = list(merge(sortedList, result[i]))
    fl = open("output/async_sorted.txt", "w+")
    for i in sortedList:
        fl.write(str(i) + "\n")

if __name__ == "__main__":
    inputDir = "input/"
    asyncio.run(main())
