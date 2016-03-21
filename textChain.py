import random
import re
prefixLen = 2

def parseToChain(s):
    chain = dict()
    wee = re.findall(r"[\w',;_.-]+",s)
    for i in range(0,len(wee)-2):
        prefix = wee[i]+" "+wee[i+1]
        suffix = wee[i+2]
        if prefix not in chain:
            chain[prefix] = list()
        #if suffix not in chain[prefix]: #we want doulbe entries for the statistics
        chain[prefix].append(suffix)
    
    return chain
    
def mergeChains(c1,c2):
    for prefix in c2:
        if prefix in c1:
            for suffix in c2[prefix]:
                c1[prefix].append(suffix)
        else:
            c1[prefix] = c2[prefix]
    return c1
    
def mergeAppendChain(c,s):
    return mergeChains(c,parseToChain(s))
    
def generateTextFromChain(c,seed="",maxiterations=10):
    result = ""
    startPrefix = ""
    startText = ""
    if seed == "" or seed not in c:
        startPrefix = random.choice(list(c.keys()))
    else:
        startPrefix = seed
    iterations = random.randrange(maxiterations)
    result = startPrefix + " "
    for i in range(iterations):
        suffix = random.choice(c[startPrefix])
        result += suffix + " "
        possibleKeys = list()
        startPrefix = startPrefix.split(' ', 1)[1] + " " + suffix
        if startPrefix not in c:
            break
    return result