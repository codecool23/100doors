doors = [False] * 100
for i in range(100):
    for j in range(i, 100, i+1):
        doors[j] = not doors[j]

def every_open_doors():
    open_doors = ""
    for i in range(0, 100):
        if doors[i] == True:
            open_doors += str(i+1) + ", "
    return open_doors
    
results = every_open_doors()            
print("the following doors are open " + results)                    
    

