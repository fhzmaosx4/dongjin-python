#-*- coding: utf-8 -*-

dic1={}

dic2=dict()

dic = {'name':'pey','phone':'0119993323','birth':'1118'}

a= {1:'hi'}

b= {'a':[1,2,3]}

print(dic['name'])

 

a={1:'a'}

 

a[2]='b'

a['name']='pey'

a[3]=[1,2,3]

 

 

a={'name':'pey','phone':'0119993323','birth':'1118'}

b=a.keys()

print(b)

 

b=list(a.keys())

 

a={'name':'pey','phone':'0119993323','birth':'1118'}

b=a.values()

print(b)

 

b=list(a.values())

#group1={'ȫ�浿':{'���׶�':'5.0','�ϻ�':'4.5'}}

#group1.get('ȫ�浿')

#group2={'��浿':{'���׶�':'2.2','�ϻ�':'3.0'}}

#Dictionary �ڷ��� �������� �Ф�

 

 

 

 

answer=input("Would you like express shipping?")

if answer and "yes,Yes" :

        print("That will be an extra $10")

pocket=['paper','cellphone','money']

 

#if 'money' in pocket:

#    print("�ýø� Ÿ�� ����")

#else:

#    print("�ɾ")

#utf-8 ���� ����

 

#for i in range(1,10):

#    for j in range(1,10):

#        print('%d X %d = %d' %(i %j %i*j, end=" "))

#    print('')

 

#�Ф� �����ܵ� ���Ѵ� ���� ���� Steps Ȱ���ϰ�,%�� �ڿ� ��ȣ �ѹ��� ����

 

 

import turtle

for steps in range(4):

    turtle.forward(100)

    turtle.right(90)

    for moresteps in range(4):

        turtle.forward(20)

        turtle.right(90)

 

import turtle

nSides = 5

for steps in range(nSides) :

    turtle.forward(100)

    turtle.right(360/nSides)

    for moresteps in range(nSides) :

        turtle.forward(50)

        turtle.right(360/nSides)

 

import turtle

for steps in ['red','blue','green','black']:

    turtle.color(steps)

    turtle.forward(100)

    turtle.right(90)

 

prompt = """"

1.Add

2.Del

3.List

4.Quit

 

Enter number:"""

 

number = 0

while number !=4:

    print(prompt, end="")

    number = int(input())
