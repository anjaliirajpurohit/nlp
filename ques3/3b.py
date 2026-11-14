import re

def test(string):
    # Split by commas or spaces, and KEEP them in the list using ()
    merged = re.split(r'([, ]+)', string)
    
    # merged[::2] gets the words (even indices: 0, 2, 4...)
    # merged[1::2] gets the separators (odd indices: 1, 3, 5...)
    return [merged[::2], merged[1::2]]

# Hardcoding the test case for the lab output, or you can keep your input()
s = "The colors in my studyroom are blue, green, and yellow."
print("Original string:", s)

result = test(s)
print("Words:", result[0])
print("Separators:", result[1])