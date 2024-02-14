#Check the string comntains more or equal to three vowels, if any print 'yes' else print 'no'
def has_three_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
        if count >= 3:
            return True
    return False

# Example usage
input_string = "Hello, how are you?"
if has_three_vowels(input_string):
    print("yes")
else:
    print("no")
