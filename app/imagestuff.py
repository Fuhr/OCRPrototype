from pytesser import *
from PIL import Image


class imageCutter:
    def cropImages(self, UPLOAD_FOLDER, filename, coordList):
        cropList = []
        img = Image.open(UPLOAD_FOLDER+filename)        
        for coordTuple in coordList:
            cropList.append(img.crop(coordTuple))            
        return cropList
    
    def cropImage(self, UPLOAD_FOLDER, filename, x1, y1, x2, y2):
        img = Image.open(UPLOAD_FOLDER+filename)
        crop = img.crop(x1,y1,x2,y2)    
        return crop

class OCR:
    def diskImgToText(self, UPLOAD_FOLDER, filename):       
        return listifyString(image_file_to_string(UPLOAD_FOLDER, filename))

    def memImgToText(self, img):
        return listifyString(image_to_string(img))

    def memImgsToText(self, imgList):
        #List to hold lists of OCR processed text
        textList = []
        for img in imgList:
            textList.append(listifyString(image_to_string(img)))
        return textList
    
    #Splits string into list at newline char
    def listifyString(s):        
        s = s.decode('utf-8')       
        sList = s.split('\n')       
        #Remove empty fields in list
        for r_index in reversed(range(len(sList))):
            if sList[r_index] == '':
                sList.pop(r_index)
        return sList
