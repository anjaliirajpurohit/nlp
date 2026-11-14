import re

def extract_data(file_path):
    with open(file_path,'r') as f:
        text = f.read()

    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}',text)


    #\. means look for a dot coz just . means any charactre in re 
    phones = re.findall(r'\b\d{10}\b',text)#\b is boundary 
    
    dates = re.findall(r'\b\d{2}-\d{2}-\d{4}\b',text)

    print(emails)
    print(phones)
    print(dates)

extract_data('demo.txt')