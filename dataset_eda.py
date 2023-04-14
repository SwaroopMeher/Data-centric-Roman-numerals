import cv2 as cv
import os
import pandas as pd
PATH = "./Submission_4"
PATH_train = PATH + '/train/'
PATH_val = PATH + '/val/'

size_dict = {}
size_dict['ImagesCount'] = []
size_dict['Type'] = []
size_dict['Label'] = []

for file in os.listdir(PATH_train):
    if file != '.DS_Store':
        size_dict['Type'].append('train')
        size_dict['Label'].append(file)
        size_dict['ImagesCount'].append(len(os.listdir(PATH_train+file)))

for file in os.listdir(PATH_val):
    if file != '.DS_Store':
        size_dict['Type'].append('val')
        size_dict['Label'].append(file)
        size_dict['ImagesCount'].append(len(os.listdir(PATH_val+file)))

size_df = pd.DataFrame(size_dict)
print(size_df)
size_df.to_excel('File_sizes.xlsx',index=None)

