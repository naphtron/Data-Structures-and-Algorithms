def canConstruction(target,wordbank):
    table = [False]*(len(target)+1)
    table[0] = True #it's always possible to create empty string
    for i in range(0, len(target)+1):
        if table[i]==True:
            for word in wordbank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] = True
    return table[-1]

def countConstruct(target, wordbank):
    table = [0]*(len(target)+1)
    table[0] = 1 # one way to pick empty string. Pick nothing
    for i in range(0, len(target)+1):
     
        if table[i] > 0:
            for word in wordbank:
                if target[i:i+len(word)] == word:
                    table[i+len(word)] += table[i]
                    

    return table[-1]


def allConstruct(target, wordbank):
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]  # represents way to make an empty string

    for i in range(len(target) + 1):
        print(f'\nIteration {i}')
        for word in wordbank:
            if target[i:i+len(word)] == word:
                new_combinations = [comb + [word] for comb in table[i]]
                table[i + len(word)].extend(new_combinations)
                print(f'Word {word} \nTable {table}\n')
                """
                or

                table[i + len(word)] += [*new_combinations]

                also

                table[i + len(word)] = [*table[i + len(word)], *new_combinations]

                """
                
    # return table


print(allConstruct('purple',['purp', 'p', 'ur', 'le','purpl']))
print(allConstruct('abcdef',['ab', 'abc', 'cd', 'def','abcd']))
print(allConstruct('starter',['st', 'ter', 'at', 'er','rter']))

# print(countConstruct('purple',['purp', 'p', 'ur', 'le','purpl']))
# print(countConstruct('abcdef',['ab', 'abc', 'cd', 'def','abcd']))
# print(countConstruct('starter',['st', 'ter', 'at', 'er','rter']))
# print(countConstruct('beatbox',['bea', 'eat', 'ox', 'at','t','b']))
# print(countConstruct('enterapotentpot',['a', 'p', 'ent','enter','ot','o','t']))


# print(canConstruction('abcdef',['ab', 'abc', 'cd', 'def','abcd']))
# print(canConstruction('starter',['st', 'ter', 'at', 'er','rter']))
# print(canConstruction('beatbox',['bea', 'eat', 'ox', 'at','t','b']))