# sample input  ("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
def count_construct(target, word_bank, memo):
    
    if target in memo: return memo[target]
    if target == '': return 1
    total_count = 0
    
    for word in word_bank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            num_ways_suffix = count_construct(suffix, word_bank, memo)
            memo[target] = num_ways_suffix
            total_count += num_ways_suffix

   
    return total_count

print(count_construct("abcdef",["abc", "cd","def"], memo={}))
print(count_construct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo={}))
print(count_construct("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo={}))
print(count_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], memo={}))
