#! /usr/bin/python
# -*- coding:UTF-8 -*-
# Convert cityscape dataset to pascal voc format dataset
# 2. convert '.txt' to '.xml'

import os, sys
import glob
from PIL import Image

# VEDAI 图像存储位置
src_img_dir = "/home/cse-305/dataset/safety_helmet_paper/images/"
# # VEDAI 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "/home/cse-305/dataset/safety_helmet_paper/labels/"
src_xml_dir = "/home/cse-305/dataset/safety_helmet_paper/xml/"

img_Lists = glob.glob(src_img_dir + '/*.jpg')

img_basenames = []  # e.g. 100.jpg
for item in img_Lists:
    img_basenames.append(os.path.basename(item))

img_names = []  # e.g. 100
for item in img_basenames:
    temp1, temp2 = os.path.splitext(item)
    img_names.append(temp1)

for img in img_names:
    im = Image.open((src_img_dir + img + '.jpg'))
    width, height = im.size

    # open the crospronding txt file
    gt = open(src_txt_dir + '/' + img + '.txt').read().splitlines()
    # gt = open(src_txt_dir + '/gt_' + img + '.txt').read().splitlines()

    # write in xml file
    # os.mknod(src_xml_dir + '/' + img + '.xml')
    xml_file = open((src_xml_dir + '/' + img + '.xml'), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC</folder>\n')
    xml_file.write('    <filename>' + str(img) + '.jpg' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    # write the region of image on xml file
    for img_each_label in gt:
        spt = img_each_label.split(' ')  # 这里如果txt里面是以逗号‘，’隔开的，那么就改为spt = img_each_label.split(',')。
        xml_file.write('    <object>\n')

        if spt[0] == '0':
            item = 'head'
        else:
            item = 'helmet'

        xml_file.write('        <name>' + item + '</name>\n')
        xml_file.write('        <pose>Unspecified</pose>\n')
        xml_file.write('        <truncated>0</truncated>\n')
        xml_file.write('        <difficult>0</difficult>\n')
        xml_file.write('        <bndbox>\n')

        center_x = round(float(spt[1].strip()) * width)
        center_y = round(float(spt[2].strip()) * height)
        bbox_width = round(float(spt[3].strip()) * width)
        bbox_height = round(float(spt[4].strip()) * height)
        xmin = str(int(center_x - bbox_width / 2))
        ymin = str(int(center_y - bbox_height / 2))
        xmax = str(int(center_x + bbox_width / 2))
        ymax = str(int(center_y + bbox_height / 2))

        xml_file.write('            <xmin>' + xmin + '</xmin>\n')
        xml_file.write('            <ymin>' + ymin + '</ymin>\n')
        xml_file.write('            <xmax>' + xmax + '</xmax>\n')
        xml_file.write('            <ymax>' + ymax + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')
    xml_file.write('</annotation>')



