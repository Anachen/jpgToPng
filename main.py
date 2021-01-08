from PIL import Image
import os,sys
self_path = os.path.abspath(os.getcwd())
source_path = self_path +"\\"+ sys.argv[1]

def get_pic_name(source):
    for file in os.listdir(source):
        yield file

def save_to():
    new_path = self_path + sys.argv[2]
    if not os.path.exists(new_path):
        os.mkdir(new_path)
    return new_path

def save_as(file,folder):
    png = ".PNG"
    jpg = ".JPG"
    try:
        name, ext = os.path.splitext(file)
        if ext == jpg:
            img = Image.open(source_path + file)
            img.save(folder + name + png)
    except:
        print("Can not be saved")



def convert_to_png():
    pic_generator = get_pic_name(source_path)
    new_folder = save_to()
    while True:
        try:
            pic = next(pic_generator)
            save_as(pic,new_folder)

        except StopIteration as err:
            print(err)
            break

convert_to_png()
