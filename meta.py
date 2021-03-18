# import argparse 
# from PIL import Image
# from PIL.ExifTags import TAGS


# def getMetaData(imgname, out):
#         try:
#                 metaData = {}
#                 imgFile = Image.open(imgname)
#                 print("Getting meta data...")   
#                 info = imgFile._getexif()
#                 if info:
#                         print("Found meta data!")
#         #перебор данных в словаре с метаданными
#                         for (tag, value) in info.items():
#                                 tagname = TAGS.get(tag, tag)
#                                 metaData[tagname] = value
#                                 if not out:
#                                         print(tagname, value)
#         #если указано имя файла то выводим в файл
#                                 if out:
#                                         print("Outputting to file...")
#                                 with open(out, 'w') as f:
#                                         for (tagname, value) in metaData.items():
#                                                 f.write(str(tagname)+"\t"+str(value)+"\n")
#         #если произошла ошибка выводим сообщение о ней
#         except Exception as e:
#                 print("Failed",str(e))

# if __name__ == '__main__':
#         getMetaData('documents/file_5.jpg', "result")


# from PIL import Image, ExifTags
# img = Image.open("documents/file_5.jpg")
# exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
# print(exif)

dic = {"1" : "a",
    "2" : "b",
    "3" : "c"}

print(dic.get("6"))