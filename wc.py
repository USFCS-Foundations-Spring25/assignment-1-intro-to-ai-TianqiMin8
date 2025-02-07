import argparse
import os
import sys
# import argparse, follow the steps in assignment, use parse_args...
from string import punctuation
# two ways of import packages, not recommend to do from ... import *, as may have name problems
# Aim: word counting the dir, should be able to run in any dir

def wordfreq(fname, stripPunc, toLower,nonwords) :
    wordDict = {}
    try :
        # not want to do: if fname.endswith('txt'), as there's a lot of txt extendtion end without .txt
        # open for file, is either tct or binary
    # OS.System("ls")
    # OS.System("python wc.py ...")
    with open(fname) as f:  # assume it can open as a txt file
        ## let's just get all the words at once.
        words = f.read().split()
        for word in words :
            if stripPunc :
                word = word.strip(punctuation)
            if nonwords:
                word = ""
            if toLower :
                word = word.lower()
            if word in wordDict :
                wordDict[word] += 1
            else :
                wordDict[word] = 1
    except :
        # TODO skip non-text file
    return wordDict

if __name__== '__main__':
    if len(sys.argv) < 2:
        print("Usage: wordfreq {--strip --convert -pfile=outfile} file")
        sys.exit(-1)

    # TODO may need to change here
    fname = sys.argv[-1] # means give the last thing
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    strip = '--strip' in sys.argv
    convert = '--convert' in sys.argv
    for r,d,f in os.walk(path) :
        wd = wordfreq(fname, stripPunc=strip, toLower=convert, nonwords=)
    pickled = False
    for arg in sys.argv:
        if arg.startswith('--pfile'):
                ofile = arg.split('=')[1]
                pickle.dump(wd, open(ofile, 'w'))
                pickled = True
        if not pickled:
            print(wd)





