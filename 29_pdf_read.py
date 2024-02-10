import PyPDF2

f = open('access.pdf','rb')
pdf_reader = PyPDF2.PdfReader(f)
print("pages ",len(pdf_reader.pages))


page_one_text = pdf_reader.pages[0].extract_text()
print(page_one_text)

f.close()