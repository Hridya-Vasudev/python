tuples_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]


new_value = 100


result = [tuple(t[:-1] + (new_value,)) for t in tuples_list]


print(result)


