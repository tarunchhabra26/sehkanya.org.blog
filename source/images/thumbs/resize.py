import os
from PIL import Image
resize_method = Image.ANTIALIAS
    #Image.NEAREST)  # use nearest neighbour
    #Image.BILINEAR) # linear interpolation in a 2x2 environment
    #Image.BICUBIC) # cubic spline interpolation in a 4x4 environment
    #Image.ANTIALIAS) # best down-sizing filter


max_height= 450
max_width= 450
extensions= ['JPG']

path= os.path.abspath(".")

def adjusted_size(width,height):
    if width>max_width or height>max_height:
        if width>height:
            return max_width, int (max_width * height/ width)
        else:
            return int (max_height*width/height), max_height
    else:
        return width,height

	
if __name__ == "__main__":
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path,f)):
            f_text, f_ext= os.path.splitext(f)
            f_ext= f_ext[1:].upper()
            if f_ext in extensions:
                print f
                image = Image.open(os.path.join(path,f))
                width, height= image.size
<<<<<<< HEAD
                image = image.resize(adjusted_size(max_width, max_height))
=======
                image = image.resize(adjusted_size(width, height))
>>>>>>> a317199aa424af754fa8f905f1c20a9732e5785d
                image.save(os.path.join(path,f))
