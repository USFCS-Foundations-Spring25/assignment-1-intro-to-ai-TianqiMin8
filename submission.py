import os

import MonteCarlo
import ZeroR
import perceptron

# Tianqi Min
# as I use intro-to-ai github to commit and push my code, and I noticed that this is not the right dir I should write code on when I try to submit my assignment
# So I copied and paste what I wrote in another dir to the new one.
# You can find my commit messages in: https://github.com/USFCS-Foundations-Spring25/assignment-1-intro-to-ai-TianqiMin8


print("testing Monte Carlo")
MonteCarlo.monte_carlo_approach(10)

print("testing ZeroR")
fname = "tennis.csv"
with open(fname) as f :
    data = f.readlines()
    print(ZeroR.zeroR(data))
    print(ZeroR.randR(data))
os.system("python ZeroR.py -z tennis.csv")
os.system("python ZeroR.py -r tennis.csv")

print("Testing wc")
print("python wc.py --strip test_wc")
os.system("python wc.py --strip test_wc")
print("python wc.py --strip test_wc --convert")
os.system("python wc.py --strip test_wc --convert")

print("python wc.py --strip test_wc --pfile='write.pkl'")
os.system("python wc.py --strip test_wc --pfile='write.pkl'")

print("python wc.py --strip test_wc --nonwords")
os.system("python wc.py --strip test_wc --nonwords")
print("python wc.py --strip test_wc --separator='#;.'")
os.system("python wc.py --strip test_wc --separator='#;.'")

print("")

print("testing perceptron")
perceptron.perceptron_training()

print("")