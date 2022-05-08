import PyPDF2

pdf = open('meupdf.pdf', 'rb')
pdf_lido = PyPDF2.PdfFileReader(pdf)
pdf_pagina = pdf_lido.getPage(0)
texto = pdf_pagina.extractText()

print(texto)
