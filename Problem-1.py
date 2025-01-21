# You are given a string str, you need to return True if  the words "cat" and "hat" appear same number of times in str, otherwise return False.


string = input("Enter a string: ").lower()
c = 0
h = 0

for i in range(len(string)):
    if string[i] == 'c' and string[i+1] == 'a' and string[i+2] == 't':
        c += 1
    elif string[i] == 'h' and string[i+1] == 'a' and string[i+2] == 't':
        h += 1

if c == h:
    print("true")
else:
    print("false") 
