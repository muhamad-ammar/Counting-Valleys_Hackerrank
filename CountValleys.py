def countingValleys(steps, path):
    count=0
    level=0
    for x in path:
        if x=="U":
            level+=1
        else:
            level-=1
        if level==0 and x=="U":
            count+=1
    return count
steps=input("Enter Total number of steps: ")
path=input("Enter the path: ")
print(countingValleys(steps,path))