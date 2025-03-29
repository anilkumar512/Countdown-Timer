import time

def countdown(t):
    while t:
        mins, secs= divmod(t,60)
        timer = "{:02d}:{:02d}".format(mins,secs)
        print(timer,end='\r')
        time.sleep(1)
        t-=1
    print('Timer Completed!!!')

t=int(input("Enter time in seconds:"))
countdown(t)
















'''
In Python, the divmod() function is a built-in function that takes two numbers as arguments and returns a tuple containing their quotient and remainder.
 It is particularly useful for performing both integer division and modulus operations in a single call.


The end='\r' ensures that the cursor moves back to the beginning of the line instead of moving to a new line after printing. 
This makes the countdown appear to update in place.


timer = "{:02d}:{:02d}".format(mins, secs)
is a string formatting operation that generates a string representing the countdown time in the format of "MM:SS", where:

MM is the minutes.
SS is the seconds.
Breakdown of the line:
"{:02d}:{:02d}": This is a string with placeholders {} that specify how the variables mins and secs will be formatted.

{:02d}:
: indicates the start of a format specification.
02 means the number should be at least 2 digits wide, and if it's less than 2 digits, it should be padded with leading zeros (e.g., 01, 09).
d means the value will be formatted as an integer.
: between the placeholders separates the minutes and seconds with a colon, so the final result looks like a typical time format MM:SS.
.format(mins, secs): This is the string .format() method, which replaces the placeholders with the actual values of the variables mins and secs.

mins will be substituted into the first {} placeholder.
secs will be substituted into the second {} placeholder.


time.sleep(1)
Pauses the program for 1 second, making the countdown update every second.


'''