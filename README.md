# listMin
listMin is a simple python script that can minimize/simplify wordlists using regular expressions. It is common for hackers to have a wordlist with too many words or duplicate strings in it so I created this script to help solve that problem


## Installation
```
git clone https://github.com/SupremeERG/listMin.git && \
cd listMin && \
sudo chmod +x listMin.py && \
sudo ln -s listMin.py /usr/bin/listMin
``` 
## Usage
`listMin --help`

`listMin -w WORDLIST -r REGEX_PATTERN -o OUTPUT_FILE`

```
listMin -w /usr/share/seclists/Fuzzing/6-digits-000000-999999.txt -r 0 -o new.txt // Gets rid of any 6 digit string containing 0

listMin -w /usr/share/wordlists/rockyou.txt -r "pass" -o /usr/share/wordlsits/rockyou.txt // Gets rid of any string containing "pass" and replaces rockyou with that output.
```

## Wiki

[Help](https://github.com/SupremeERG/listMin/wiki/Help)

[List of Common Regexes](https://github.com/SupremeERG/listMin/wiki/Regexpressions#common-regex-patterns)
<!-- add link to regex wiki page -->
