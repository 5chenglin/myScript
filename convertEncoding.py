import os
import sys
import chardet

def ConvertFormat(file):
    fileName = os.path.splitext(file)
    print('coonvert {0}.{1}'.format(fileName[0], fileName[1]))
    if ('.txt' not in fileName[1]):
        return
    
    with open(file, "rb+") as f:
        content = f.read()
        encode = chardet.detect(content)['encoding']

        if (encode != 'utf-8'):
            try:
                gbk_Content = content.decode(encode)
                utf_byte = bytes(gbk_Content, encoding="utf-8")
                f.seek(0)
                f.write(utf_byte)
            except IOError:
                print('convert {0}.{1} fail !!!!'.format(fileName[0], fileName[1]))

    return


def ReadDir(dir):
    for file in os.listdir(dir):
        file = os.path.join(dir, file)
        ConvertFormat(file)

    return

def main():
    ReadDir("D:/DATA/")

if __name__ == "__main__":
    main()

