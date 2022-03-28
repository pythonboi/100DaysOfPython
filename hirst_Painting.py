# Import the Cologram module 
import colorgram

getImages = colorgram.extract(r"C:\Users\admin\Documents\PyDev\100DaysOfPython\hirst.jpg", 10)

myDic = []

#print(type(getImages))
# print(getImages)


rpg = getImages[9]

#print(rpg.rgb)

for m in getImages:
    # myDic.append(m.rgb)
    red, green, blue = m.rgb.r, m.rgb.g, m.rgb.b
    myTuple = (red, green, blue)
    myDic.append(myTuple)
    #print(red, green, blue)
print(myDic)