import cv2
import os

from pathlib import Path    
from glob import glob
from tqdm import tqdm
import shutil
def convert_images(input_folder,output_folder):
    # Path(output_folder).mkdir(parents=True, exist_ok=True)
    input_files = glob(os.path.join(input_folder, "*"))
    for f in input_files:
        image = cv2.imread(f, cv2.IMREAD_GRAYSCALE)
        # quantize
        image = (image // 43) * 43
        image[image > 43] = 255
        cv2.imwrite(os.path.join(output_folder, os.path.basename(f)), image)

if __name__ == "__main__":
    folder_name = "./Submission_4/train"
    folders_output = glob(f"{folder_name}/*")
    folders_input = [folder+'\\augmented' for folder in folders_output]
    # folders_input,folders_output = ['./Submission_4\\train\\ix\\Manual'], ['./Submission_4\\train\\ix\\']
    for inp,out in tqdm(zip(folders_input,folders_output)):
        convert_images(inp,out)
    for f in folders_input:
        try:
            shutil.rmtree(f)
        except:
            print(f)
    # img_dir  = './test/train/'
    # img_augmentation(img_dir)
        