import sys

def wordcount(S):
    N = len(S.strip().split())
    return N



filename = sys.argv[0]
try:
   f = open(arg, 'r')
   text = f.read()
   print(wordcount(text))
   f.close()
except:
   print("File not available!")
S = "harshath"
print(wordcount(S))
