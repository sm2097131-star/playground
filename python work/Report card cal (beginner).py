while True:      
      
      while True:
          s1=float(input("Enter marks obtained in Maths:"))
          if 0>s1 or s1>100:
            print('Invalid')
          else:
            break
            
      while True:
          s2=float(input("Enter marks obtained in Science:"))
          if 0>s2 or s2>100:
            print('Invalid')
          else:
            break
      
      while True:
          s3=float(input("Enter marks obtained in English:"))
          if 0>s3 or s3>100:
            print('Invalid')
          else:
            break
      
      while True:      
          s4=float(input("Enter marks obtained in Hindi:"))
          if 0>s4 or s4>100:
            print('Invalid')
          else:
            break
            
      while True:
          s5=float(input("Enter marks obtained in SST/AI:"))
          if 0>s5 or s5>100:
            print('Invalid')
          else:
            break
      
      
      total=s1+s2+s3+s4+s5
      percentage=(total/500)*100
      
      if percentage>=90:
        Grade='A'
      
      elif 90>percentage>=75:
        Grade='B'
      
      elif 75>percentage>=55:
        Grade='C'
      
      else:
        Grade="Need Improvement"
      
      print(f'Your total is {total}')
      print(f'Your % is {percentage:.3f}')
      print(f'Your Grade is : {Grade}')
  
      user=input("Do you want to exit (y/n)?")
      if user=="y":
        print("Thank You")
        break
      else:
        continue
    