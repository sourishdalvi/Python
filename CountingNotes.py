amount=int(input('Please enter the amount of money you would like to withdraw'))
notes500=amount//500
notes100=(amount%500)//100
notes50=((amount%500)%100)//50
print("Number of 500rs notes are",notes500)
print("Number of 100rs notes are",notes100)
print("Number of 50rs notes are",notes50)

