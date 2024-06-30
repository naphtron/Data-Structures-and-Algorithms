def best_sum(target, numbers):
    table = [None]*(target+1) #initalize the table
    table[0] = []  #set the initial value
    for i in range(0, target+1):
        if table[i] is not None:
            for num in numbers:
                if i+num<=target: #ensure it stays within bounds
                    combination = [*table[i],num]
                    if table[i+num] is None or len(table[i+num]) > len(combination): #replace value if future value is None or combination is less than stored value
                        table[i+num] = combination
        
    return table[-1]

def how_sum(target,numbers):
    table = [None]*(target+1)
    table[0] = []
    for i in range(0, target+1):
        if table[i] is not None:
            for num in numbers:
                if i+num <= target:
                    table[i+num] = [*table[i],num]

    return table[target]

def can_sum(target, numbers):
    table = [False]*(target+1)
    table[0] = True
    for i in range(0,target):
        if table[i]==True:
            for num in numbers:
                if i+num<=target:
                    table[i+num] = True
    return table[-1]



print(can_sum(8, [2,4,5,3]))
print(can_sum(18, [2,4,5,3]))
print(can_sum(17, [5,9,3]))


print("\n")


print(how_sum(8, [2,4,5,3]))
print(how_sum(18, [2,4,5,3]))
print(how_sum(17, [5,9,3]))


print("\n")



print(best_sum(8, [2,4,5,3]))
print(best_sum(18, [2,4,5,3]))
print(best_sum(17, [5,9]))
