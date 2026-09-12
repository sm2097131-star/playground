import json
import os
title="University Management System"
width=50
print(title.center(width))

def no_empty(prompt):
  while True:
    user=input(prompt).strip()
    if len(user)>0:
      return user
    else:
      print("You can't leave it blank")
      continue

def add_student():

  student_data={}
  if os.path.exists('myfile.json'):
   with open("myfile.json", "r") as f:
    if os.path.getsize('myfile.json')==0:
      print("File is empty")
    else:
          student_data = json.load(f)

  else:
    print('No file found!')

  while True:
      try:  

         

         user=no_empty("Enter the name of the student:").title().strip()
         
         while True:
          user_roll=no_empty("Enter roll no.:").strip()
          if user_roll in student_data:
            print("Roll is already taken")
            continue
          else:
            break
      
         user_dep=no_empty("Enter the student department:").strip()
        

         parent_name=no_empty("Enter your fathers name :").strip()
        

         stu_details={'Name.':user,
        'Department:':user_dep,
        'parents name': parent_name}


         student_data[user_roll]=stu_details
        

         user1=input("Press E to exit or P to procced:").lower().strip()

       

         if user1 =='e':
            with open('myfile.json','w') as f :
              json.dump(student_data,f,indent=2)
          
              break
          
         else:
              continue
        
        

      except ValueError:
          print("invalid input")
           
  return student_data   

def search_stu():
  if os.path.exists('myfile.json'):
    with open("myfile.json",'r') as g:
     userx=input("Enter your roll no.:")
     loaded_database=json.load(g)
     if userx in loaded_database:
     
      data=loaded_database[userx]
      print(f"Name: {data['Name.']}")
      print(f"Department: {data['Department:']}")
      print(f"Father's Name: {data['parents name']}")


     else:
      print('Record not found!')


def start():

 while True:

  try:
  
  
      userz=int(input("1.To add Student\n2.To search student\n3.View all(json file)\n4.To mark attendance\n5.Attendance count\n6.Exit program:"))
      if userz==1:
        p=add_student()
        print(p)
      elif userz==2:
        o=search_stu()
        print(o)
      elif userz==3:
       if os.path.exists('myfile.json'):
        with open('myfile.json','r') as k:
          loaded_database=json.load(k)
          print(loaded_database)
       else:
        print("No entry found!")
      elif userz==4:
        q=attendance()
        print(q)
      elif userz==5:
        g=attendancereport()
        print(g)
      elif userz==6:
        print('Thank you')
        break
      else:
        print("Invalid input")

  except ValueError:
   print("Invalid Input!")


def attendance():

  data0={}

  attendance={}
  
  user2=no_empty("Enter the date:")

  if os.path.exists('myfile2.json'):
    
   with open('myfile2.json','r') as n:
    if os.path.getsize('myfile2.json')==0:
      print("File is empty")
    else:
      data0=json.load(n)
      

  with open('myfile.json','r') as l:
    data1=json.load(l)
  if isinstance(data1,dict):
    for key in data1:
      print('Mark A for absent and P for present')
      p=no_empty(f'Roll no.{key}:').strip().lower()
      attendance[key]=p

    data0[user2]=attendance
    with open('myfile2.json','w') as m:
      json.dump(data0,m,indent=2)
  return "Thank you the Remarks are Saved "


def attendancereport():
  with open('myfile2.json','r') as i:
    data2=json.load(i)
    user3=no_empty("Enter the roll:")
    count=0
    total_keys=len(data2)
    for date in data2:
      daily_attendance=data2[date]

      if user3 in daily_attendance:
        if daily_attendance[user3]=='p':
          count+=1
          pass
    

    print(f'The student attendance count is {count}')
    print(f'Attendance percentage:{(count/total_keys)*100}')

p=start()
print(p)






  

    
        
          

       



#   pass

