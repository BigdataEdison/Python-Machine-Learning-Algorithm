# coding:UTF-8
'''
Date:20180831
@author: xs
'''
import numpy as np

def generate_data():
    '''在[-4.5,4.5]之间随机生成20000组点
    '''
    # 1、随机生成数据点
    data = np.mat(np.zeros((10, 3)))
    m = np.shape(data)[0]
    x = np.mat(np.random.rand(10, 3))
    for i in xrange(m):
        data[i, 0] = x[i, 0] * 9 - 4.5
        data[i, 1] = x[i, 1] * 9 - 4.5
        data[i, 2] = x[i, 2] * 9 - 4.5
    print data
    # 2、将数据点保存到文件“test_data”中
    f = open("test_generate", "w")
    m,n = np.shape(data)
    for i in xrange(m):
        tmp =[]
        for j in xrange(n):
            tmp.append(str(data[i,j]))
        f.write("\t".join(tmp) + "\n")
    f.close()  

if __name__ == "__main__":
    generate_data()