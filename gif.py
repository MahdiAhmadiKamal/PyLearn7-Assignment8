import os
import imageio

file_list = sorted (os.listdir ("PyLearn7-Assignment8/gif_images_2"))

IMAGES = []
for file_name in file_list:
    
    file_path = "PyLearn7-Assignment8/gif_images_2/" + file_name
    image = imageio.imread (file_path)
    IMAGES.append (image)

imageio.mimsave ("PyLearn7-Assignment8/my_output_2.gif", IMAGES)