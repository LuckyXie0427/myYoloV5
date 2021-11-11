import xml.etree.ElementTree as ET
import os
import cv2

def process_labels(label_id):

    in_file = open(DATASET_PATH + 'labels/%s' % (label_id)) #
    label_id = label_id.replace('.txt', '')
    out_file = open('./processed_labels/%s.txt' % (label_id), 'w')
    data = in_file.readlines()
    for line in data:
        if line[0] == '0':
            out_file.write(line)
        elif line[0] == '1':
            out_file.write(line)

def make_label_txt():
    """在labels文件夹下创建image_id.txt，对应每个image_id.xml提取出的bbox信息"""
    filenames = os.listdir(DATASET_PATH + 'labels')
    for file in filenames:
        process_labels(file)

if __name__ == '__main__':
    DATASET_PATH = "E:\\team_work\detectionTest\yolov5\myCode\\"
    make_label_txt()