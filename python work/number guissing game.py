import random 
num=random.randint(1,100)
dif=input("Choose your difficulty (E/M/H): ").lower()
print("")
if dif =='e':
  attempt=10
elif dif=='m':
  attempt=7
elif dif=='h':
  attempt=5
else :
  print("Invalid difficulty , difficulty set to Med")
  attempt=7
  print('')
  

c=0


while c<attempt:
 
  print(f"It's is your {c+1} attempt ")
  print(f"Attempts left: {attempt - c}")
  try:
    
    user=int(input("Guess(1-100):"))
    print('')
    c+=1

    dist=abs(user-num)
    
    
    if user > num:
      print("High")
    elif user < num:
      print("Low")
    if 0<dist <= 5:
      print("But you're very close!")
    elif 6<dist < 12:
      print("But you're close!")

    if num==user:
      print(f"And You Guessed it right!! {num}")
      break
  except ValueError:
    print("Enter a valid no.")
else:
    print(f"Game Over :( , the number was {num}")
    