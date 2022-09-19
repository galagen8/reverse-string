"""

Complete the function that accepts a string parameter, and reverses each word in the string. 
All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

text = "This is an example!"

def reverse_words(text):
    new_string = []
    arr = text.split()
    for x in arr:
        a = x[::-1]
        new_string.append(a)
    if text.find("  ") == -1:
        new_string = " ".join(new_string)
    else:
        new_string = "  ".join(new_string)
    return new_string


print(reverse_words(text))