import PyPDF2

def getSentencesFromPage(pdfReader, pageNum, keyword):
    found_sentences = []
    pageObj = pdfReader.getPage(pageNum)
    sentences = pageObj.extractText()
    sentences_splited = sentences.split('.')
    for s in sentences_splited:
        if s.find(keyword)!=-1:
          found_sentences.append(s) 
    return found_sentences


filename = 'example.pdf'
pdfReader = PyPDF2.PdfFileReader(open(filename,'rb'))

keyword = 'lemon'
total_pages = pdfReader.getNumPages()
for i in range(total_pages):
    results = getSentencesFromPage(pdfReader, i, keyword)
    if results != []:
        for s in results:
            print('page:',i+1, '#', s.strip().replace('\n', ''))