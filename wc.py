import argparse
import os
import pickle
import sys
import re
# import argparse, follow the steps in assignment, use parse_args...
from string import punctuation
# two ways of import packages, not recommend to do from ... import *, as may have name problems
# Aim: word counting the dir, should be able to run in any dir

def wordfreq(fname, stripPunc, toLower,nonwords,separator) :
    wordDict = {}
    with open(fname) as f:  # assume it can open as a txt file
        ## let's just get all the words at once.
        words = re.split(separator, f.read())
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if nonwords:
                if not word.isalpha():   # CITE: https://docs.python.org/3/library/stdtypes.html#str.isalpha
                    word = ""
            if toLower :
                word = word.lower()
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__== '__main__':
    if len(sys.argv) < 2:
        print("Usage: wordfreq {--strip --convert -pfile=outfile} file")
        sys.exit(-1)

    parser = argparse.ArgumentParser()
    parser.add_argument("root_name")
    # parser.add_argument('--save', action="save_file")
    args = parser.parse_args()

    strip = '--strip' in sys.argv
    convert = '--convert' in sys.argv
    nonwords = '--nonwords' in sys.argv
    separator = '--separator' in sys.argv

    print(args.root_name)
    wd = {}
    for r,d,f in os.walk(args.root_name) :
        # wd = wordfreq(fname, stripPunc=strip, toLower=convert, nonwords=)
        for file in f:
            full_name = os.path.join(r, file)
            try:
                open(full_name,"r",encoding='utf-8')    # CITE: google for how to only read text file
                wd = wordfreq(full_name, strip, convert, nonwords, separator)
            except:
                print(f"Cannot open {full_name}")

    pickled = False
    for arg in sys.argv:
        if arg.startswith('--pfile'):
                ofile = arg.split('=')[1]
                pickle.dump(wd, open(ofile, 'w'))
                pickled = True
        if not pickled:
            print(wd)





