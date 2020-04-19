import PyPDF2

input_file = "PDF_files/super.pdf"
output_file = "PDF_files/super_watermarked.pdf"
watermark_file = "PDF_files/wtr.pdf"

with open(input_file, "rb") as pdf_file:
    pdf = PyPDF2.PdfFileReader(pdf_file)
    with open(watermark_file, "rb") as pdf_watermark_file:
        watermark_file = PyPDF2.PdfFileReader(pdf_watermark_file)
        watermark = watermark_file.getPage(0)
        pdfWriter = PyPDF2.PdfFileWriter()
        for i in range(0, pdf.numPages):
            pdf.getPage(i).mergePage(watermark)
            pdfWriter.addPage(pdf.getPage(i))
        
        with open(output_file, "wb") as watermarked_output:
            pdfWriter.write(watermarked_output)
