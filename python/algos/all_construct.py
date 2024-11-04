from pprint import pprint
def all_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]
    
    if target == '':
        return [[]]
    
    final_array = []
    
    for word in word_bank:
        if target.startswith(word) == True:
            suffix = target[len(word):]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = list(map(lambda way: [word]+way, suffix_ways))
            if target_ways:
                final_array.extend(target_ways)
                
    memo[target] = final_array
    return final_array 

word_weights = {'a': 100, 'ent': 35, 'enter': 50, 'er': 10,
            'o': 20,  'ot': 25, 'p': 45, 'pot': 70, 't': 20}

def get_sum(arr):
    return sum([word_weights[word] for word in arr])

all_arrays =  all_construct("enterpotentpot", [ "a", "p","ent", "enter","ot", "o", "t", "pot", "er"], memo={})
for arr in sorted(all_arrays, key=lambda a: get_sum(a), reverse=True):
    print(arr, "->", get_sum(arr))