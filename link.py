import os
import shutil
import time

global_data = "./data/global_data"
specific_data = "./data/specific_data"

folder_destination = '../loading_data/orderedData'

list1 = os.listdir(global_data)  # permet de parcourir le dossier et de trouver tous les fichiers
list2 = os.listdir(specific_data)

number_global_files = len(list1)
number_specific_files = len(list2)

print("The number of global files is : " + str(number_global_files))
print("The number of specific files is : " + str(number_specific_files) + '\n')

folder = '../loading_data/orderedData'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

for i in list1:
    num = list1.index(i)
    i = i.replace('_',' ')
    i = i.replace('.dat','')
    i = i.replace(i[:18],'')
    list1[num] = i;

for i in list2:
    num = list2.index(i)
    i = i.replace('_',' ')
    i = i.replace('.dat','')
    i = i.replace(i[:13], '')
    list2[num] = i;

list1_original = os.listdir(global_data)  # permet de parcourir le dossier et de trouver tous les fichiers
list2_original = os.listdir(specific_data)

for k in list1:
    for h in list2:
        if h == k:
            shutil.copy(global_data + '/'+ list1_original[list1.index(k)], folder_destination)
            time.sleep(1)
            shutil.copy(specific_data + '/'+ list2_original[list2.index(h)], folder_destination)
            time.sleep(1)

