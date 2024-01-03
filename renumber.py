import os

images_path = './images'
images_name = os.listdir(images_path)
images_name.sort(key=lambda x: int(x.split('.')[0]))

for i in range(len(images_name)):
    os.rename(os.path.join(images_path, images_name[i]), os.path.join(images_path, str(i) + '.jpg'))
