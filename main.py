import docx
from docx.shared import Inches
import os
from typing import List

def createDoc(quesfileName: str,allImages: List[str]):
    file = open(quesfileName,'r')
    fileList = list(file)
    # imageIdx = 0
    questions = list(filter(lambda x: True if(x!='\n') else False,fileList))
    doc = docx.Document()
    imageIdx = 0
    for x in range(len(questions)):
        quesParaObj = doc.add_paragraph('Question: '+str(x+1)+":")
        quesParaObj.add_run('\n')
        quesParaObj.add_run(questions[x])
        while(imageIdx<len(allImages) and allImages[imageIdx][1]==str(x+1)):
            print(allImages[imageIdx],imageIdx)
            doc.add_picture('image/'+allImages[imageIdx],width=Inches(5))
            imageIdx += 1

    doc.save('assignment.docx')  

def getImagesName() -> List[str]:
    imagesPath = os.getcwd()+"/image"
    allImages = os.listdir(imagesPath)
    allImages.sort()
    return allImages

createDoc('questionFile',getImagesName())