#!/usr/bin/python3
import re, argparse
from time import sleep,time

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", help="Input wordlist", required=True)
parser.add_argument(
    "-r",
    "--regex",
    help="Regex to filter through wordlist",
    required=True
)
parser.add_argument("-o", "--output", help="Output file for transformed wordlist", required=True)
args = parser.parse_args()

# variables
outputWL = ""
i = 0
startTime = time()


# functions
def validateRegex():
    pass # validate regex and make sure there is no problem with them
    # if the regex is invalid the script will run it anyway but return everything from the original wl
    # so if it is invalid stop the script and say so

def cleanUp(wordlist: str):
    wordlist = wordlist.strip()

    wordlist += "\n"
    return wordlist

# main script
try:
    print("\n\n")
    with open(args.wordlist, "r") as wordlist:
        wordlist = wordlist.readlines()
        i=0
        fullLength = len(wordlist)
        for word in wordlist:
            print(f"{round(((i/fullLength) * 100), 2)}% Done", end="\r") # chang this to show a percentage
            if re.search(fr"{args.regex}", word) == None:
                outputWL += word
            i+=1
except KeyboardInterrupt as err:
    pass
finally:
    endTime = time() - startTime
    print("\n")

    for x in range(0, 5):
        print("Exiting" + "." * x, end="\r")
        sleep(0.05)

    cleanedList = cleanUp(outputWL)    
    with open(args.output, "w") as outputFile:
        outputFile.write(cleanedList)
        print(f"{(cleanedList.count(chr(10)))} lines writtent to {args.output} in {round(endTime,2)} seconds")
