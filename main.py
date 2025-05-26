def distinct(arr):
    result = []
    for i in arr:
        if i not in result:
            result.append(i)
    return result
print(distinct([1,1,2]))