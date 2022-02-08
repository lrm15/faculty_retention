import pdfplumber 

for i in range(77, 108): 
    with pdfplumber.open('/Users/laurenmccarey/math308/catalog_2020-21.pdf') as temp: 
        page = temp.pages[i]
        print(page.extract_text())
        break
