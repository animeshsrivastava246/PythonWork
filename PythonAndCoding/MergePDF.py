import PyPDF2,sys
inputs=sys.argv[1:]
def pdf_combiner(pdf_list):
    merged=PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        print(pdf)
        merged.append(pdf)
    merged.write('Combined PDF.pdf')
pdf_combiner(inputs)