def increment(counter):
  while True:
    counter=counter+1
    if counter==10:
      break
  return counter+1
counter=0
counter=increment(counter)
print(counter)