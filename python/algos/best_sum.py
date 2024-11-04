def best_sum(target_sum, numbers, memo=None):
    if memo is None: memo = {}
    if target_sum in memo: return memo[target_sum]
    if target_sum == 0: return []
    if target_sum < 0: return None
    
    shortest = None
    for num in numbers:
        
        remainder = target_sum - num
        
        remainder_result = best_sum(remainder, numbers, memo)
        
        if remainder_result is not None:
            combination = [*remainder_result, num]
            
            if shortest is None or (len(combination) < len(shortest)):
                shortest = combination
        
    memo[target_sum] = shortest 
    return shortest

print(best_sum(7, [2,3]))
print(best_sum(7, [5,3,4,7]))
print(best_sum(7, [2,4]))
print(best_sum(8, [2,3,5]))
print(best_sum(300, [7,14]))
print(best_sum(200,[1]))
print(best_sum(1000,[2,4]))
