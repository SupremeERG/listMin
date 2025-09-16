#!/usr/bin/python3
import re, argparse
from time import sleep, time
from collections import OrderedDict

# user arguments and manual
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mode", help="Filtering mode to use, (\"include, exclude, cut\")\nDEFAULT: exclude", default="exclude", choices=["include","exclude", "cut"])
parser.add_argument("-p", "--patternfile", help="Read list of regexes in a file seperated by new lines (u guessed it: a wordlist)")
parser.add_argument("-s", "--saveorder", help="Save the order of the inputted wordlist (This will make the cleanup just a little longer)", action="store_true")
parser.add_argument("-l", "--lowercase", help="Makes every entry of wordlist lowercase", action="store_true")
parser.add_argument("-w", "--wordlist", help="Input wordlist", required=True)
parser.add_argument(
    "-r", "--regex", help="Regex to filter through wordlist"
)
parser.add_argument(
    "-o", "--output", help="Output file for transformed wordlist", required=True
)
args = parser.parse_args()


def validateRegex(pattern):
    """
    Validates and compiles the regex pattern provided by the user.
    If no pattern is provided, or if the pattern is invalid, the function will print an error message and exit the program.
    """
    try:
        if pattern is None and args.patternfile is None:
            print("Please specify a regex using -r or read from a list using -p")
            exit()
        if pattern is not None and args.patternfile is not None:
            print("Please only specify -r OR -p, dont use both")
            exit()
        elif args.patternfile is not None:
            pattern = ""
            with open(args.patternfile, "r") as regexPatterns:
                for regexPattern in regexPatterns:
                    if regexPattern == "\n":
                        continue
                    pattern += regexPattern.strip() + "|"
            pattern = pattern[:-1]
        re.compile(pattern)
        return pattern
    except re.error:
        print(
            "The regex pattern you entered was not valid. Please try again with a valid regex pattern"
        )
        exit()

def cleanUp(wordlist: str):    
    """
    Cleans up the wordlist by removing duplicates and stripping whitespace.
    If the saveorder option is not used, the order of the wordlist will be scrambled due to the functionality of the set() function.
    """
    wordlist = wordlist.strip() # first strip makes deduplication faster

    # remove duplicates
    wordlist = wordlist.split("\n")
    if args.saveorder is True:
        wordlist = "\n".join(OrderedDict.fromkeys(wordlist))
    else:
        wordlist = "\n".join(list(set(wordlist)))


    return wordlist.strip() + "\n"

def getLineCount(file):
    """
    Returns the number of lines in a file.
    """
    return len(open(file, "rb").readlines())

regexFilter = validateRegex(args.regex)


def main():
    outputWL = ""
    i = 0 # progression
    startTime = time()

    try:
        print("\n\n")

        # transformation algorithm
        with open(args.wordlist, "rb") as wordlist:
            i = 0
            fullLength = getLineCount(args.wordlist)
            for word in wordlist:
                word = word.decode("latin-1") # used to prevent regex searching error that seldomly occurs with utf-8
                if args.lowercase == True:
                    word = word.lower()
                if args.mode == "exclude":
                    if re.search(rf"{regexFilter}", word) == None:
                        outputWL += word
                elif args.mode == "include":
                    if re.search(rf"{regexFilter}", word) != None:
                        outputWL += word
                elif args.mode == "cut":
                    if re.sub(rf"{regexFilter}", "", word) == "":
                        continue
                    outputWL += re.sub(rf"{regexFilter}", "", word)
                i += 1
                print(
                    f"{round((i/fullLength) * 100, 2)}% Done", end="\r"
                )
    except KeyboardInterrupt: # catches ctrl+c
        print(f"\nStopping at {round((i/fullLength) * 100, 2)}%")
    finally:
        print("\n")
        endTime = time() - startTime

        
        [print(f"\rCleaning Up{'.' * x}", end="\r") or sleep(0.2) for x in range(4)]
        
        cleanedList = cleanUp(outputWL)    
        with open(args.output, "w", encoding="latin-1") as outputFile:
            outputFile.write(cleanedList)
        print(f"\n{cleanedList.count(chr(10))} lines written to {args.output} in {round(endTime, 2)} seconds")

if __name__ == "__main__":
    main()