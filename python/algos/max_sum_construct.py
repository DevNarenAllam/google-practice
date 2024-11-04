
def max_construct(target, word_bank, memo):
    if target in memo:
        return memo[target]

    if target == '':
        return []

    max_array = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):]
            max_suffix_way = max_construct(suffix, word_bank, memo)
            combination = [word] + max_suffix_way
            print(max_array, get_sum(max_array), combination, get_sum(combination))
            if not max_array or get_sum(combination) > get_sum(max_array):
                max_array = combination
            print()

    memo[target] = max_array
    return max_array


word_weights = {'a': 100, 'ent': 35, 'enter': 50, 'er': 10,
            'o': 20,  'ot': 25, 'p': 45, 'pot': 70, 't': 20}


def get_sum(arr):
    return sum([word_weights[word] for word in arr])


max_combo = max_construct("enterpotentpot", word_weights.keys(), memo={})
print(max_combo, "-->", get_sum(max_combo))

