#write a python program to check all the characters in a string is unique,
def are_all_characters_unique(string):
    # Create an empty set to store encountered characters
    unique_chars = set()

    for char in string:
        # If the character is already in the set, it is not unique
        if char in unique_chars:
            return False

        # Add the character to the set
        unique_chars.add(char)

    # All characters in the string are unique
    return True

# Example usage
input_string = "OpenAI"
if are_all_characters_unique(input_string):
    print("All characters in the string are unique")
else:
    print("String contains duplicate characters")
