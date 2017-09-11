#!usr/bin/python
'''x=int(input('please input one number'))
y=int(input("please input y"))
if x>=90:
    if y>=90:
        print("A")
    else:
        print("???")
elif x>=80:
    print("B")
elif x>=60:
    print("C")
else:
    print("D")
print(True and True)

for x in 'abcd':
    print(x,'hello world')

for i in range(1,10,2):
    print(i,'hello world')
y=0
for x in range(1,101):
    y+=x
print(y)
for x in "hello":
    print(x)
s='hello'
for x in range(len(s)):
    print(x)
s='hello'
print(s[0])
d={1:111,2:222,5:555,3:333}
for x in d:
    print(x)
for k,v in d.items():
    print(k)
    print(v)
else:
    print('ending')
import time
for x in range(20):
    print(x)
    if x==2:
        continue
        print("hello 2222")
    if x==3:
        pass #???
    if x==5:
        exit()
    print('#'*50)
    time.sleep(1)
    if x>6:
        break
else:
    print('ending')
x=input('please input something,q for quit:')
while x!="q":
    print("hello")
    x=input('please input something,q for quit:')
    if not x:
        break
    if x=='c':
        continue
    print("one omre time")
else:
    print('ending?')
a=200
b=300
def add():
    c = a + b
    print(c)
add()

def fun():
    if True:
        print('good')
fun()
fun()
if True:
    fun()

def fun(x):
    if x<2:
        print(x," < 2 ")
    else:
        print(x," >= 2 ")
x=int(input())
fun(x)

def fun(x,y):
    if x==y:
        print(x,'=',y)
    else:
        print(x,'!=',y)
x=input('please input x:')
y=input('please input y:')
fun(x,y)

def mashine(x=3,y='奶油味'):
    print('生成一个',x,'元',y,'口味的冰激凌！')
#x=input('please input something:')
#y=input('please input something')
mashine()
x=10
t=(1,2)
def fun(x,y):
    print(x)
    print(y)
fun(t[0],t[1])
def f():
    return "hello"
x=f()
print(x)
def fun(x,y):
    print("welcome")
    return x+y
    print(x+y)
z=fun(2,3)
print(z)

def fun():
    return 'one'
    return 'two'
x=fun()
print(x)
def f(x,y):
    if x==y:
        return x==y
    else:
        return x!=y
        return 0
f(1,2)

def f(x):
    print(x)
x=f(10)
print(x)
print(("%s:%s")%('name','milo'))
def f(x,y):
    print(("%s:%s")%(x,y))
t=(1,2)
f(*t)

def f(name='name',age=0):
    print('name:%s'% name)
    print('age:%s'% age)
#f('camilla',25)
#t=(30,'milo')
#f(*t)
d={'name':'camilla','age':25}
f(**d)

def f(x,*a):
    print(x)
    print(a)
f(1,2,3,4)

def f(x,*m,**t):
    print(x)
    print(*m)
    print(**t)
f(x=1,y=2)

def f(x,y):
    return (x*y)
z=f(2,3)
print(z)

g=lambda x,y:x*y
z=g(2,3)
print(z)

g=lambda x,y:x+y
g(22,3)

l=range(1,6)

def f(x,y):
    print(x*y)
reduce(f,l)   这句话有问题

def jia(x,y):
    print(x+y)
def jian(x,y):
    print(x-y)
def chen(x,y):
    print(x*y)
def chu(x,y):
    print(x/y)
def operator(x,o,y):
    if o=="+":
        jia(x,y)
    elif o=="-":
        jian(x,y)
    elif o=="*":
        chen(x,y)
    elif o=="/":
        chu(x,y)
    else:
        pass
operator(1,'*',2)

def jia(x,y):
    print(x+y)
def jian(x,y):
    print(x-y)
def chen(x,y):
    print(x*y)
def chu(x,y):
    print(x/y)
# def operator(x,o,y):
operator={"+":jia,"-":jian,"*":chen,"/":chu}
# operator["+"](3,2)
operator.get('/')(3,2)

def a(x):
    if x<0:
        return -x
    else:
        return x
print(a(-10))

print(abs(-10))

l=(2,2,3,4,5,7)
print(max(l))
print(len(l))
print(divmod(2,5))

help(divmod)
help(pow)

s='hello world'
print(s.capitalize())
print(s.replace('hello','good'))
help(str.replace)

ss='123124'
print(ss.replace('1','x'))

help(str.split)
ip='192.168.1.123'
print(ip.split('.',2))

def f(x):
    if x>5:
        return True
l=[1,2,3,4,5,6,7]
print(filter(f,l))
'''
print('hello!')