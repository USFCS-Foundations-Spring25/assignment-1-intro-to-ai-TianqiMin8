import argparse
import os
import pickle
import sys
import re

from string import punctuation

def wordfreq(fname, stripPunc, toLower, nonwords, separator, wordDict) :
    # wordDict = {}
    with open(fname) as f:
        ## let's just get all the words at once.
        if separator:   # step 4
            regex_pattern = "["
            for s in separator:
                regex_pattern += s
            regex_pattern +="]"

            words = re.split(regex_pattern,f.read())    # CITE: https://docs.python.org/3/library/re.html#re.split
        else:
            words = f.read().split()
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if toLower :
                word = word.lower()
            if nonwords:
                if not word.isalpha():
                    word = ""
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    return wordDict

if __name__== '__main__':
    if len(sys.argv) < 2:
        print("Usage: wc {--strip --convert --pfile=outfile} file")
        sys.exit(-1)
    # fname = sys.argv[-1]

    # strip = '--strip' in sys.argv
    # convert = '--convert' in sys.argv
    parser = argparse.ArgumentParser()  # step 1
    parser.add_argument("path")
    parser.add_argument("--strip",action="store_true")
    parser.add_argument("--convert", action="store_true", help="change the str to lowercase")
    parser.add_argument("--nonwords", action="store_true", help="remove non-alphebatic strings")

    parser.add_argument("--pfile", type=str) # TODO step3
    parser.add_argument("--separator", type=str) # step 4

    args = parser.parse_args()


    wd={}
    for r,d,f in os.walk(args.path) :
        # wd = wordfreq(args.path, stripPunc=strip, toLower=convert)
        for file in f:  # step 2
            full_name = os.path.join(r, file)
            try:
                # open(full_name,"r",encoding='utf-8')    # CITE: google for how to only read text file
                wd = wordfreq(full_name, args.strip, args.convert, args.nonwords,args.separator, wd)
            except:
                print(f"Cannot open {full_name}")

    pickled = False
    # for arg in sys.argv:
    if args.pfile:
            ofile = args.pfile
            pickle.dump(wd, open(ofile, 'wb'))   # TODO: what is write as an object?
            pickled = True
    if not pickled:
        print(wd)