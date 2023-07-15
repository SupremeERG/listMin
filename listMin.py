#!/usr/bin/python3
import re, argparse, threading, concurrent.futures  # , argcomplete
from time import sleep, time

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Filtering mode to use, (\"include, exclude\")\nDEFAULT: exclude", default="exclude", choices=["include","exclude"])
parser.add_argument("-w", "--wordlist", help="Input wordlist", required=True)
parser.add_argument(
    "-r", "--regex", help="Regex to filter through wordlist", required=True
)
parser.add_argument(
    "-o", "--output", help="Output file for transformed wordlist", required=True
)
args = parser.parse_args()

# variables
outputWL = ""
i = 0
startTime = time()


# functions
def validateRegex(pattern):
    # validate regex and make sure there is no problem with them
    # if the regex is invalid the script will run it anyway but return everything from the original wl
    # so if it is invalid stop the script and say so
    try:
        re.compile(pattern)
    except re.error:
        print(
            "The regex pattern you entered was not valid. Please try again with a valid regex pattern"
        )
        exit()

def cleanUp(wordlist: str):    
    wordlist = wordlist.strip()

    # remove duplicates
    wordlist = wordlist.split("\n")
    wordlist = "\n".join(list(set(wordlist)))

    return wordlist + "\n"

def getLineCount(file):
    return len(open(file, "rb").readlines())

validateRegex(args.regex)


# main script
try:
    print("\n\n")
    with open(args.wordlist, "rb") as wordlist:
        i = 0
        fullLength = getLineCount(args.wordlist)
        for word in wordlist:
            word = word.decode("latin-1")
            # algorithm
            if args.mode == "exclude":
                if re.search(rf"{args.regex}", word) == None:
                    outputWL += word
                i += 1
            elif args.mode == "include":
                if re.search(rf"{args.regex}", word) != None:
                    outputWL += word
                i += 1
            print(
                f"{round(((i/fullLength) * 100), 2)}% Done", end="\r"
            )
except KeyboardInterrupt as err:
    pass
finally:
    print("\n")
    endTime = time() - startTime

    for x in range(4):
        print("Cleaning Up" + "." * x, end="\r")
        sleep(0.2)
        if x == 3:
            print("Cleaning Up...")
            sleep(1.6)
            print("dont worry, I did not crash on you :)  I'm still cleaning up")

    cleanedList = cleanUp(outputWL)
    with open(args.output, "w") as outputFile:
        outputFile.write(cleanedList)
    print(f"\n{cleanedList.count(chr(10))} lines written to {args.output} in {round(endTime, 2)} seconds")

