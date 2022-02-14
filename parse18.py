# import pdfplumber 
import pandas as pd
import csv

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
    # print('\n')
    line = line.split(',', maxsplit=2)
    line = [item.strip(' \n') for item in line]

    if (len(line) == 3): 
        if ("on leave" in line[2]): 
            if ("on leave Fall 2018" in line[2]): 
                line.append('f') 
                line[2] = line[2].replace(", on leave Fall 2018", '')
            if ("on leave Spring 2019" in line[2]): 
                line.append('s')
                line[2] = line[2].replace(", on leave Spring 2019", '')
            if ("on leave 2018-2019" in line[2]): 
                line.append('y')
                line[2] = line[2].replace(", on leave 2018-2019", '') 
            print(line)
        else: 
            line.append('n')
    if (len(line) == 2): 
        line.append('none')
        line.append('n')
    if (len(line) == 1): 
        line.append("none")
        line.append("none")
        line.append('n')

    # with open('faculty2018-19.csv', 'w') as f: 
    #     writer = csv.writer(f)
    #     writer.writerows(line)





        
    
    # print(len(line))
    # print(line)