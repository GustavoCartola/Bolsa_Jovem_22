import PyPDF2

pdf = open('meupdf.pdf', 'rb')  # Open the PDF file
pdf_reader = PyPDF2.PdfFileReader(pdf)  # Create a PDF reader object
pdf_page = pdf_reader.getPage(0)  # Get the first page
text = pdf_page.extractText()  # Extract text from the page

print(text)  # Print the extracted text
