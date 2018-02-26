# coding=utf-8
import pickle
import os
def browse(cb):
    print('name number email')
    for key in cb:
        print(key,end=' ')
        for value in cb[key]:
            print(value,end=' ')
        print(' ')
def add(cb,name,number,email):
    cb[name]=[number,email]
def delete(cb,name):
    del cb[name]
def search(cb,name):
    if name in cb:
        print(name,end=' ')
        for value in cb[name]:
            print(value,end=' ')
        print('')
    else:
        print('not exist')
contactbookfile='contactbook.data'
if os.path.getsize(contactbookfile)==False:
    contactbook={}
    f=open(contactbookfile,'wb')
    pickle.dump(contactbook,f)
    f.close()
f=open(contactbookfile,'rb')
contactbook=pickle.load(f)
f.close()
while True:
    a=input('choose 1.browse 2.add 3.delete 4.search 5.exit&save: ')
    if a=='1':
        browse(contactbook)
    elif a=='2':
        name=input('input name ')
        number=input('input number ')
        email=input('input email ')
        add(contactbook,name,number,email)
    elif a=='3':
        name=input('input the name ')
        delete(contactbook,name)
    elif a=='4':
        name=input('input the name ')
        search(contactbook,name)
    elif a=='5':
        break
    else:
        print('wrong input')
f=open(contactbookfile,'wb')
pickle.dump(contactbook,f)
f.close()
