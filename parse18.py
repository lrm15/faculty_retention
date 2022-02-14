# import pdfplumber 

# text = ''
# for i in range(62, 90): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/catalog_2018-19.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2018-19.txt', 'a') as f: 
#         f.write(text)

lines = []
with open ('catalog_2018-19.txt') as f: 
    lines = f.readlines()

for line in lines: 
    print('\n')
    line = line.split(',', maxsplit=2)
    line = [item.strip(' \n') for item in line]
    print(line)