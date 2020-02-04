import docx

def createDoc(fileName: str):
    file = open(fileName,'r')
    fileList = list(file)
    questions = list(filter(lambda x: True if(x!='\n') else False,fileList))
    doc = docx.Document()
    for x in range(len(questions)):
        doc.add_paragraph('Question: '+str(x+1)+":")
        doc.add_paragraph(questions[x])
        doc.add_paragraph('')

    doc.save('assignment.docx')  

createDoc('questionFile')