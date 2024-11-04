# sample input  ("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
def can_construct(target, word_bank, memo={}):
    
    if target in memo: return memo[target]
    if target == '': return True
    
    for word in word_bank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True
    memo[target] = False    
    return False

print(can_construct("abcdef",["abc", "cd","def"], memo={}))
print(can_construct("skateboard",["bo", "rd", "ate", "t", "ska", "sk", "boar"], memo={}))
print(can_construct("enterpotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], memo={}))
print(can_construct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"], memo={}))