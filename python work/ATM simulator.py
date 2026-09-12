def read_balance():
  try:
    with open('myfile2.txt', 'r') as f:
      content = f.read()
      return int(content)
  except FileNotFoundError:
    with open('myfile2.txt', 'w') as e:
      e.write('1000')
      return 1000

def new_balance(active_balace):
  with open('myfile2.txt', 'w') as g:
    g.write(f'{active_balace}')

active_balace = read_balance()

while True:
  user0 = input('Deposit/Withdraw/Balance Check/C:').lower().strip()
  if user0 == 'deposit':
    user2 = int(input('Enter Amt. to be deposited:'))
    if user2 <= 0:
     print("Amount must be positive")
     continue
    active_balace += user2
    new_balance(active_balace)
    print('Deposited Successfully')
    print(f'Current Balance: ${active_balace}')
  elif user0 == 'withdraw':
    user3 = int(input('Enter the amount:'))
    if user3 <= 0:
     print("Amount must be positive")
     continue
    if active_balace >= user3:
      active_balace -= user3
      new_balance(active_balace)
      print('Withdrawn Successfully')
      print(f'Current Balance: ${active_balace}')
    else:
      print('insufficient balance')
  elif user0 == 'balance check':
    print(f'Current Balance: ${active_balace}')
  elif user0 == 'c':
    break
  else:
    print('Invalid input')
    