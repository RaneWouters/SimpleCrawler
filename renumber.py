import os

images_path = './images'
images_name = os.listdir(images_path)
images_name.sort()

output_path = './images_renumbered'
if not os.path.exists(output_path):
    os.mkdir(output_path)

for i in range(len(images_name)):
    os.system('cp {} {}'.format(
        os.path.join(images_path, images_name[i]),
        os.path.join(output_path,
                     str(i).rjust(4, '0') + '.jpg')))
