# -*- coding: utf-8 -*-
from pathlib import Path  #从pathlib中导入Path
import os
import fileinput
import random
root_path='/home/cse-305/dataset/safety_helmet_paper/images'
train = open('./trash_train.txt','a')
test = open('./trash_test.txt','a')

rate = 0.7

def make_train_test():
    sum = 0
    for file in os.listdir(root_path):
        sum += 1

    # make train label
    out_file = open('trash_train.txt', 'w')
    pick_num = int(sum * rate)
    image_total = os.listdir(root_path)
    sample = random.sample(image_total, pick_num)
    for train_name in sample:
        out_file.write('./images/' + train_name + '\n')

    # make test label
    same = [x for x in image_total if x in sample]  # 列表中相同的内容
    diff = [y for y in (sample + image_total) if y not in same]  # 列表中不同的内容
    out_file = open('trash_test.txt', 'w')
    for test_name in diff:
        out_file.write('./images/' + test_name + '\n')

make_train_test()