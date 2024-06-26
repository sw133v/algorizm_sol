import sys
def sol_29965():
    n = int(sys.stdin.readline().strip())
    tempData = dict({
        "M":[],
        "J":[],
    })
    
    for _ in range(n):
        p, score = sys.stdin.readline().strip().split()
        tempData[p].append(int(score))
    
    avgM, avgJ = None, None
    
    if tempData["M"] == []:
        avgM = 0
    else:
        avgM = sum(tempData["M"])/len(tempData["M"])
    
    if tempData["J"] == []:
        avgJ = 0
    else:
        avgJ = sum(tempData["J"])/len(tempData["J"])
        
    if avgM == avgJ:
        print("V")
    if avgM > avgJ:
        print("M")
    if avgJ > avgM:
        print("J")

sol_29965()