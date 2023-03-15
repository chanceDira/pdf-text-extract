from pypdf import PdfReader, PdfFileWriter

file_path = 'essay.pdf'
pdf = PdfReader('essay.pdf')

with open('essay_v2.text', 'w') as f:
    for page_num in range(len(pdf.pages)):
        pageObj = pdf.pages[page_num]
        try:
            txt = pageObj.extract_text()
            print(''.center(100, '-'))
        except:
            pass
        else:
            f.write('Page {0}\n'.format(page_num + 1))
            f.write(''.center(100, '-'))
            f.write(txt)
    f.close()

