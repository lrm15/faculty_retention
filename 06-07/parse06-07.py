import pdfplumber 
import pandas as pd
import csv
from pathlib import Path 

# text = ''
# for i in range(395, 409): 
#     with pdfplumber.open('/Users/laurenmccarey/math308/06-07/catalog_2006-07.pdf') as temp: 
#         page = temp.pages[i]
#         text = page.extract_text()
#     with open ('catalog_2006-07.txt', 'a') as f: 
#         f.write(text)

lines = []
with open ('catalog_2006-07.txt') as f: 
    lines = f.readlines()


degree_list = ["b.a.", "b.s.", "ph.d", "b.f.a", "a.b", "b.m", "ba", "c.a.p.e.s", "bachelors", "a.m", "s.b", "b.mus", "m.a", "b.c", "ed.m", "b.comm", "m.f.a"]
degs = []

count = 0 
new_lines = []
i = 0 
for i in range(len(lines)): 
    line = lines[i]
    line = line.lower()

    # check whether each line starts with a degree - if so, mark with semicolon and store index in degs 
    for item in degree_list: 
        if (line[0:len(item)] == item): 
            line = line.replace(item, ";" + item)
            count += 1
            degs.append(i)
    
    new_lines.append(line)

    i += 1

j = 0
merged = []
while (j < len(new_lines)): 
    if (not j in degs) and ((j + 1) in degs): 
        x = [new_lines[j], new_lines[j + 1]]
        # print(new_lines[j].join(new_lines[j + 1]))
        print(' '.join(x).replace("\n", ""))
        # merged.append(new_lines[i] + new_lines[j])

    j = j + 1


            
# new_lines = []
# with open('temp.txt') as f: 
#     new_lines = f.readlines()

# i = 0 
# for i in range(len(new_lines) - 1):


#     for j in range(len(new_lines)): 
        
#         if (new_lines[j][0] == ";"): 
#             new_lines[i] = new_lines[i] + new_lines[j]

#         j += 1

#     print(new_lines[i])
#     i += 1
   

# new_lines = []
# with open ('catalog_temp.txt') as f: 
#     new_lines = f.readlines()

# print(new_lines)

# for line in new_lines: 
#     if line[0] == ";": 
#         print(line)
