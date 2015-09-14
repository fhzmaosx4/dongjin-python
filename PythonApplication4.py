#coding:cp949
#인코딩 모드를 cp949로 해주는것. 파이썬과 vs의 호환성위해.
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
# 튜플로 반환함
data = sum_and_mul(3, 4)
sum, mul = sum_and_mul(3, 4)

def sum_and_mul(a,b):
    return a+b, a*b
sum,mul = sum_and_mul(10,30)
print(sum,mul)

def say_myself(name, old, man=True):
 print("나의 이름은 %s 입니다." % name)
 print("나이는 %d살입니다." % old)
 if man:
    print("남자입니다.")
 else:
    print("여자입니다.")
say_myself("greenjoa", 23)
say_myself("greenjoa", 23, False)


def printData(data):
    for item in data:
        print(item)

data=["홍길동",["암살","베테랑"],"고길동",["암살"]]
printData(data)


def printData(data,level=0):
    for item in data:
        if isinstance(item,list):
            printData(item, level+1)
        else :
            print(item)
#재귀함수로 리스트 안에 리스트 중복되있을때 출력하는 방법

data=["홍길동",["암살","베테랑",["황정민","류승범","유아인"]],"고길동",["암살"]]
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
            """#import용으로 printdata.py로 내보냄
"""
import printData
#재귀함수
data=["홍길동",["암살","베테랑",["황정민","류승범","유아인"]],"고길동",["암살"]]
printData.printdata(data)
"""
import os
#help(os.mkdir)
#print(os.getcwd()) #현재 작업하는 디렉토리 표시
#os.mkdir("sample")
os.chdir(".//sample")
#print(os.getcwd())
os.system("python setup.py sdist") #설치파일 만들기
#os.system("python setup.py install") #설치하기

