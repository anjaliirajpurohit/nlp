import re

def sheep(s):
    # Changed \z to $ to correctly mark the end of the string
    pattern = r'^ba{2,}!$'
    
    # re.match automatically checks from the beginning, but the ^ is good practice
    if re.match(pattern, s):
        return True
    else:
        return False
    
tests = ['baa!', 'baaa!', 'ba!', 'b!', 'cbaa!']

for t in tests:
    print(t, "--", sheep(t))