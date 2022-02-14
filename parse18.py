import pdfplumber 

text = ''
for i in range(62, 90): 
# for i in range(62, 64): 
    with pdfplumber.open('/Users/laurenmccarey/math308/catalog_2018-19.pdf') as temp: 
        page = temp.pages[i]
        text = page.extract_text()
    with open ('catalog_2018-19.txt', 'a') as f: 
        f.write(text)

# with open ('catalog_2018-19.txt', 'w') as f: 
#      f.write(corpus)

# lines = []
# with open ('catalog_2018-19.txt') as f: 
#     lines = f.readlines()

# for line in lines: 
#     print('\n')
#     print(line.split(',', maxsplit=2))
