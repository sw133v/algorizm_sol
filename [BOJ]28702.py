import sys
def sol_28702():
    def fizzBuzz(inputData):
        res = ""
        if inputData % 3 == 0:
            res += "Fizz"
        if inputData % 5 == 0:
            res += "Buzz"
        if res == "":
            res = inputData
        
        return res
            
    data = []
    for _ in range(3):
        tempInput = sys.stdin.readline().strip()
        try:
            data.append(int(tempInput))
        except ValueError:
            data.append(tempInput)
        
    tempList = []
    for i in range(3):
        if(type(data[i])==str):
            continue
        tempList = [i, data[i]]
    tempInputData = tempList[1] + 3 - tempList[0]
    print(fizzBuzz(tempInputData))
        
    
sol_28702()