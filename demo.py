import pdfplumber 

for i in range(77, 108): 
    with pdfplumber.open('/Users/laurenmccarey/math308/catalog_2020-21.pdf') as temp: 
        page = temp.pages[i]
        # print(page.extract_words())
        text = page.extract_text()
        text = str(text)
        print(text.split('\n'))
        print(text)
        break
