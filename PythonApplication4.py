#coding:cp949
#���ڵ� ��带 cp949�� ���ִ°�. ���̽�� vs�� ȣȯ������.
"""
def main():
    names = ["greenjoa1","greenjoa2", "greenjoa3"]
    newName = input("Enter last guest : ")
    names.append(newName)
    printNames(names)
    return

def printNames(names):
 for name in names:
    print(name)
    return
main()

def main():
 names=getNames()
 printNames(names)
 return
def getNames():
 names = ["greenjoa1","greenjoa2", "greenjoa3"]
 newName = input("Enter last guest : ")
 names.append(newName)
 return names
def printNames(names):
 for name in names:
    print(name)
    return
main()
def main():
 names=getNames()
 printNames(getNames())
 return
def sum_and_mul(a,b):
 return a+b, a*b
# Ʃ�÷� ��ȯ��
data = sum_and_mul(3, 4)
sum, mul = sum_and_mul(3, 4)

def sum_and_mul(a,b):
    return a+b, a*b
sum,mul = sum_and_mul(10,30)
print(sum,mul)

def say_myself(name, old, man=True):
 print("���� �̸��� %s �Դϴ�." % name)
 print("���̴� %d���Դϴ�." % old)
 if man:
    print("�����Դϴ�.")
 else:
    print("�����Դϴ�.")
say_myself("greenjoa", 23)
say_myself("greenjoa", 23, False)


def printData(data):
    for item in data:
        print(item)

data=["ȫ�浿",["�ϻ�","���׶�"],"��浿",["�ϻ�"]]
printData(data)


def printData(data,level=0):
    for item in data:
        if isinstance(item,list):
            printData(item, level+1)
        else :
            print(item)
#����Լ��� ����Ʈ �ȿ� ����Ʈ �ߺ��������� ����ϴ� ���

data=["ȫ�浿",["�ϻ�","���׶�",["Ȳ����","���¹�","������"]],"��浿",["�ϻ�"]]
printData(data)
"""
"""
def printData(data,level=0): #
    for item in data:
        if isinstance(item,list):
            printData(item, level+1)
        else :
            for i in range(level):
                print("\t",end="")
            print(item)
            """#import������ printdata.py�� ������
"""
import printData
#����Լ�
data=["ȫ�浿",["�ϻ�","���׶�",["Ȳ����","���¹�","������"]],"��浿",["�ϻ�"]]
printData.printdata(data)
"""
import os
#help(os.mkdir)
#print(os.getcwd()) #���� �۾��ϴ� ���丮 ǥ��
#os.mkdir("sample")
os.chdir(".//sample")
#print(os.getcwd())
os.system("python setup.py sdist") #��ġ���� �����
#os.system("python setup.py install") #��ġ�ϱ�

