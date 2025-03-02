
from copy import deepcopy

def options():
 print('To-Do list options')
 print('1 Add task')
 print('2 Delete task')
 print('3 Print list')
 print('4 Mark task as completed')
 print('5 Exit')
 
 


def add(ttask):
     taskname=input('Enter task to add ')
     ttask.append(taskname)
##     continue
##     print(ttask)



def delete(ttask):
     taskname=input('Enter task to delete ')
     if taskname in ttask:
       ttask.remove(taskname)
     else:
       print('Wrong task entered')

##     tasknumber=int(input('Enter no. of task to delete '))
##     if 0<=tasknumber and tasknumber <=len(ttask):
##         ttask.pop(tasknumber)
##      


def printlist(ttask):
    print('The list is: ')
    for t in ttask:
      print(t)
##    print('The list is \n',ttask)


def completedtask(ttask):
   ttask=['a','b','c','d']
   temp=deepcopy(ttask)
##   print(temp)
   ctask=int(input('Enter completed task no. '))
   ttask[ctask]='Completed'
##   print(ttask)
##   print(temp)
   for t in range(len(ttask)):
        print(temp[t], '\t', ttask[t])
##   for t in ttask:
##       print(t)
##  
  

def main():
##  print('hi')
  ttask=[]
  index=len(ttask)
  
  while True:
    value=options()

    print('Enter your choice ')
    value=int(input())
##    print(type(value))
    if value==1:
     add(ttask)
    elif int(value)==2:
     delete(ttask)
    elif value==3:
       printlist(ttask)
    elif value==4:
       completedtask(ttask)
    elif value==5:
      break
    else:
        print('Wrong input, Re-enter ')
        newvalue=input()
##        continue
        if int(newvalue)<=index:
            continue


        
main()        

