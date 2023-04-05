import PyPDF2

pdfs = []
x = int(input("How many pdfs do you want to merge? : "))
for _ in range(x):
    name = input("Enter pdf name: ")
    pdfs.append(name)
    
merger = PyPDF2.PdfMerger()

for pdf in pdfs:
    pdfile = open(pdf,'rb')
    pdfReader = PyPDF2.PdfReader(pdfile)
    merger.append(pdfReader)
pdfile.close()
merger.write('merged.pdf')