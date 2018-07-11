# coding:UTF-8
'''
Date:20160901
@author: zhaozhiyong
'''
import numpy as np

def load_data(file_name):
    '''导入训练数据
    input:  file_name(string)训练数据的位置
    output: feature_data(mat)特征
            label_data(mat)标签
    '''
    f = open(file_name)  # 打开文件
    feature_data = []
    label_data = []
    for line in f.readlines():
        feature_tmp = []
        lable_tmp = []
        lines = line.strip().split("\t")
        feature_tmp.append(1)  # 偏置项
        for i in xrange(len(lines) - 1):
            feature_tmp.append(float(lines[i]))
        lable_tmp.append(float(lines[-1]))
        
        feature_data.append(feature_tmp)
        label_data.append(lable_tmp)
    f.close()  # 关闭文件
    return np.mat(feature_data), np.mat(label_data)

if __name__ == "__main__":
    # 1、导入训练数据
    print "---------- 1.load data ------------"
    feature, label = load_data("data.txt")
    # 2、训练LR模型
    print feature
    print label
