# SOL 1 beginner
nums = [2,7,11,15]
target=int(input('Enter yout target:'))
for indx,i in enumerate(nums):
  partner=target-int(i)
  if partner in  nums:
   a=nums.index(partner)
   if a !=indx:
    print([i,partner])
    break
  
# Sol 2

def twoSum(nums, target):

      dict_nums={}
      for indx,i in enumerate(nums):
        partner=int(target)-int(i)
        if partner in dict_nums:
         val=dict_nums[partner]
         return [indx,val]
        else:
          dict_nums[i]=indx
nums = [2, 7, 11, 15,59, 51, 13, 12, 51, 36, 35, 1, 38, 77]
target = input('Enter a number:')

print(twoSum(nums, target))

  