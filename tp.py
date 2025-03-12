import json
import requests

from copy import deepcopy
from io import StringIO, BytesIO

def options():
 print('To-Do list options')
 print('1 Add task')
 print('2 Delete task')
 print('3 Modify task')
#  print('3 Print list')
 print('4 Mark task as completed')
 print('5 Exit')



def add(ttask):
    tid=input('Enter task id to add: ')
    ttitle=input('Enter task title: ')
    ttime=input('Enter task time in 24 hr format: ')
    tprio=input('Enter task priority: ')
    tcomp=input('Enter task is completed or not: ')

    y = {"id":tid, "title":ttitle, "time":ttime, "priority":tprio,"Completed":tcomp}
    print(y)
    with open('todo.json', 'r+') as f:
        jdata = json.load(f)
        # print(j_data)
        # for k in json_data['subjects']:
        jdata["list"].append(y)
        print(jdata)
        f.seek(0)
        
        f.write(json.dumps(jdata, indent=2))
    

def delete(ttask):
    tid=int(input('Enter task id to delete: '))
    # print(tid)
    # print(type(tid))
    
    with open('todo.json', 'r+') as f:
        jdata = json.load(f)
        # print(jdata)
        # key_to_remove = tid
        # # print(type(key_to_remove))
        # # print(jdata['list'][tid])  # this just deletes one key in obj. but we need to delete multiple keys so use del[]
        # removed_value =jdata.pop({['list'][tid]})
    del jdata['list'][tid-1]
    print(jdata)
   
    with open('todo.json', 'w') as f:
      json.dump(jdata, f,indent=2)
      print(jdata)



def modify(ttask):
    num=int(input('Enter task no. to edit: '))
    numb=int(input('What would you like to modify? 1. id,\n 2. title,\n 3. time,\n 4. priority,\n 5. Status '))
    # print(num-1)
    with open('todo.json', 'r+') as f:
        jdata = json.load(f)
        print(jdata['list'][(num-1)])
        if numb==1:
             tid=input('Enter modified task id: ')
             d=jdata['list'][(num-1)]
             d['id']=tid
             f.seek(0)        # reset file position to the beginning
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
            #  f.write(json.dumps(d, indent=2))
        elif numb==2:
             tid=input('Enter modified task title: ')
             d=jdata['list'][(num-1)]
             d['title']=tid
             f.seek(0)
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
        elif numb==3:
             tid=input('Enter modified task time: ')
             d=jdata['list'][(num-1)]
             d['time']=tid
             f.seek(0)
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
        elif numb==4:
             tid=input('Enter modified task priority: ')
             d=jdata['list'][(num-1)]
             d['priority']=tid
             f.seek(0)
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
        elif numb==5:
             tid=input('Enter modified task status: ' )
             d=jdata['list'][(num-1)]
             d['status']=tid
             f.seek(0)
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
        else:
            print('Wrong input')
            # continue
    

def completedtask(ttask):
    # num=int(input('Enter task no. to edit: '))
    # numb=int(input('What would you like to modify? 1. id,\n 2. title,\n 3. time,\n 4. priority,\n 5. Status '))
    # # print(num-1)
    count=int(input('Enter task to mark as completed: '))
    with open('todo.json', 'r+') as f:
        jdata = json.load(f)

        for k in jdata['list'][(count-1)]:
           d=jdata['list'][(count-1)]['Completed']
        #    print(d)
           if d=="no":
             jdata['list'][(count-1)]['Completed']='yes'
             f.seek(0)        # reset file position to the beginning
             f.write(json.dumps(jdata, indent=2))
             print(jdata)
             break
           else:
               print('Task already completed') 
               break
            #  f.write(json.dumps(d, indent=2))   
 
# f = open("song.json")
# print(f.read())
# f.write("{Now the file has more content!:p}")
# f.close()
# print(f.read())
# # print(type(f))   ##text io wrapper

# g=json.load(open('song.json'))
# print(g)
# print(type(g))  ##list type



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
    elif value==2:
       delete(ttask)
    elif value==3:
       modify(ttask)
    elif value==4:
       completedtask(ttask)
    # elif value==5:
    #   break
    else:
        print('Wrong input, Re-enter ')
        break
#         newvalue=input()
# ##        continue
#         if int(newvalue)<=index:
#             continue


        
main()        