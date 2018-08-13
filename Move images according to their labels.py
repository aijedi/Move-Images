
# coding: utf-8
import pandas as pd

df = pd.read_csv('a.csv')

import cv2

for img in df['image name']:
    img_file = cv2.imread(img)

for i in df.loc[df['bmi_label']==1]:
    img = cv2.imread(i)

import os

bmi_group = ["underweight", "normal", "overweight", "obese"]
for img_file in os.listdir('images'):
    try:
        group_no = int(df[df['image name']==img_file]["bmi_label"].values[0])
        src = "images/" + img_file
        dest = str(bmi_group[group_no-1]) + "/" + img_file
        os.rename(src, dest)
    except:
        print(df[df['image name']==img_file]["bmi_label"].values)

