# Python - else in Loop

# Python allows the else keyword to be used with the for and while loops too.
# The else block appears after the body of the loop. The statements in the else block will be executed after all iterations are completed.
# The program exits the loop only after the else block is executed.

i = 0
while i<7:
  print(i)
  i = i + 1
  # if i == 4:
  #   break

else:
  print("Sorry no i")

for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop")