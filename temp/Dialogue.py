
import re

import chardet


def convert_to_str(var):
    if isinstance(var, bytes):
        var = var.decode('utf-8')
    return var


# 读取文件内容并检测编码
with open(r"D:\迅雷下载\台词\S01E01.ass", "rb") as f:
    raw_data = f.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# 使用正确的编码打开文件
with open(r"D:\迅雷下载\台词\S01E01.ass", "r", encoding=encoding) as f:
    with open(r"D:\迅雷下载\台词\S01E01-c.txt", 'a', encoding='utf-8') as fx:
        for file in f:
            #file = f.readline()
            file1 = re.sub(
                r"Default.*\\N{\\fn微软雅黑}{\\fs13}", "\n\n", file)
            print(file1)
            file1 = convert_to_str(file1)
            fx.write(file1+"\n\n")
