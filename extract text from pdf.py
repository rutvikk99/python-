## extract text from any pdf through pyPDF2

import PyPDF2
text= PyPDF2.PdfFileReader('filename.pdf')

print(text.getNumPages()) ## to get total no of pages
str= ""
for i in range(1,11):
    str += text.getPage(i).extractText() ##extracts the texts from pdf 
    
with open("text.txt" , "w" , encoding='utf-8' ) as f: ##store in a txt file 
        f.write(str) 
