#Remove duplicate charecter from the string and return a new string with no duplicate elememts.
def remove_duplicates(string):
    unique_chars = []
    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
    return ''.join(unique_chars)

# Example usage
input_string = "Hello, how are you?"
new_string = remove_duplicates(input_string)
print(new_string)
