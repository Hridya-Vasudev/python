def find_pairs(arr, target_sum):
    pairs = []
    complements = set()

    for num in arr:
        complement = target_sum - num
        if complement in complements:
            pairs.append((num, complement))
        complements.add(num)

    return pairs


arr = [6, 2, 3, 9, 0, 4, 5,8]
target_sum = 10
result = find_pairs(arr, target_sum)
for pair in result:
    print(f"The two numbers are {pair[0]} and {pair[1]}.")