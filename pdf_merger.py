import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(f"PDF_files/{pdf}")
    
    merger.write("PDF_files/super.pdf")

pdf_combiner(inputs)

# sample code to rotate a page in a pdf document
# with open("PDF_files/dummy.pdf", "rb") as pdf_file:
#     reader = PyPDF2.PdfFileReader(pdf_file)
#     print(reader.numPages)
#     page = reader.getPage(0)
#     page.rotateCounterClockwise(90)
#     writer = PyPDF2.PdfFileWriter()
#     writer.addPage(page)
# with open("PDF_files/rotated_dummy.pdf", "wb") as new_file:
#     writer.write(new_file)
