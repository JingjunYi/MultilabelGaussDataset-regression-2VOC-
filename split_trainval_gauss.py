import os
import numpy as np
from tqdm import tqdm



if __name__ == '__main__':

    origin_label_txt = 'E:/Multiweather/dataset/GTAV_multiweather/experiment/label_gauss.txt'
    train_txt_pth = 'train_map_gauss.txt'
    val_txt_pth = 'val_map_gauss.txt'

    with open(origin_label_txt, 'r') as f:
        label_lines = f.readlines()
        for i, label_line in enumerate(label_lines):
            label_line = label_line.strip('\n')
            if (i + 1) % 10 == 0 or (i + 1) % 10 == 9:
                with open(val_txt_pth, 'a') as f1:
                    f1.write(label_line)
                    f1.write('\n')
            else:
                with open(train_txt_pth, 'a') as f1:
                    f1.write(label_line)
                    f1.write('\n')