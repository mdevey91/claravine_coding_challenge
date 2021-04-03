def find_pair(values, desired_sum):
    try:
        values_set = {int(v) for v in sorted(values) if v > 0}
    except Exception as e:  # int() throws an error for anything that can't be cast as an integer
        return None
    if len(values_set) < len(values):  # there were duplicates or a value less than 1
        return None
        
    for num in values_set:
        second_num = desired_sum - num
        if second_num in values_set:
            return [num, second_num]
            
    return None
    
print(find_pair([2,5,1,3,4,6,7, 0], 8))  # None
print(find_pair([2,5,1,3,4,6,7], 8)) # [1,7]
print(find_pair([3,3,5,6,7], 11)) # None
print(find_pair([4,2,8,25], 26)) # None