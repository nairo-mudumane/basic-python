import sys

args = sys.argv

def soma(n1,n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2

if args[1] == "soma":
    res = soma(float(args[2]),float(args[3]))
    print(res)
elif args[1] == "sub":
    res = sub(float(args[2]),float(args[3]))
    print(res)
    