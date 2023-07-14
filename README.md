# listMin
listMin is a simple python script that can minimize/simplify wordlists using regular expressions. It is common for hackers to have a wordlist with too many words in it: so I created this script to help solve that problem
## Installation
```
git clone https://github.com/SupremeERG/listMin.git \
cd listMin \
sudo chmod +x listMin.py \
cp listMin.py /usr/bin/listMin
``` 
## Usage
```
listMin -w /usr/share/seclists/Fuzzing/6-digits-000000-999999.txt -r 0 -o new.txt // Gets rid of any 6 digit string containing 0

listMin -w -r "
```

regex with one pattern

regex with two patterns
