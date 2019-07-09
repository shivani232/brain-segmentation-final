from PIL import Image
path = "mona3.png" # Your image path 
img = Image.open(path)
members = [(0,0)] * 9
# print img.width
newimg = Image.new("RGB",(img.width,img.height),"white")
for i in range(1,img.width-1):
    for j in range(1,img.height-1):
        members[0] = img.getpixel((i-1,j-1))
        members[1] = img.getpixel((i-1,j))
        members[2] = img.getpixel((i-1,j+1))
        members[3] = img.getpixel((i,j-1))
        members[4] = img.getpixel((i,j))
        members[5] = img.getpixel((i,j+1))
        members[6] = img.getpixel((i+1,j-1))
        members[7] = img.getpixel((i+1,j))
        members[8] = img.getpixel((i+1,j+1))
        members.sort()
        newimg.putpixel((i,j),(members[4]))
newimg.save('mona4.png')
