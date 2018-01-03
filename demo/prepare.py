# coding:utf-8
'''
    Author:minning
    Date:2018/1/3
    代码目的：
    
'''


def getdata(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            if line != '\n':
                linelist = line.split(':')
                content = linelist[1]
                data.append(content)

    print len(data)
    return data


if __name__ == "__main__":
    filepath = '../data/chatPair.csv'
    data = getdata(filepath)
