def max_vowels(string,size):
    max_count = 0
    vowels = set(['a','e','i','o','u'])
    l,result,count = 0,0,0
    for r in range(len(string)):
        count += 1 if string[r] in vowels else 0
        
        if r - l + 1 > size:
            count -= 1 if string[l] in vowels else 0
            l += 1
        
        result = max(result,count)
    
    return result
        
            
        

print(max_vowels("aberioerjnaowel", 5))