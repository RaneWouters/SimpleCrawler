import os

images_path = './images'
images_name = os.listdir(images_path)
images_name.sort()

for i in range(len(images_name)):
    os.rename(os.path.join(images_path, images_name[i]),
              os.path.join(images_path,
                           str(i).rjust(4, '0') + '.jpg'))
