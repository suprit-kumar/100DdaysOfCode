# Create a python program capable of greeting you with Good Morning,
# Good Afternoon and Good Evening. Your program should use time module to get the current hour.
# Here is a sample program and documentation link for you:

# Morning Time : 04:00:00 to 11:59:59
# Afternoon Time : 12:00:00 to 16:59:59
# Evening Time : 17:00:00 to 20:59:59
# Night Time : 21:00:00 to 03:59:59




import time
timestamp = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
if hour >= 4 and hour<12:
    print("Good Morning!!!!!!!!")
elif hour>=12 and hour<17:
    print("Good Afternoon!!!!!!!!")
elif hour>=17 and hour<21:
    print("Good Evening!!!!!!!!")
else:
    print("Good Night!!!!!")