# There are many ways to reverse the string in the pytohn but in this code we will see the 4 methods(prakriayaa) .How to reverse the string

# Let's start with the python bultin functions and methods

# 1 is with the python builtin funciton reversed

a = "My name is AAyush basnet"


b = reversed(a)
new_string = ''
# To see the result we have to iterate is with the loop
for i in b:
    new_string += i
print(new_string)


# 2 is the anther easy way by python builtin methods 

c = 'My nmae is aayush basnert'[::-1]
print(c)


# 3 is reversing the string maually by the help of the loop
my_new_string = ''
def let_reverse(s):
    global my_new_string
    my_new_string = s+my_new_string

# passed the string in the let_reverse function as a argument
let_reverse(c)
print(my_new_string)



# 4 is by the help of the recursion 

another_string = "I will rule the world"
my_new_strings = ''
def lets_reverse(s, l):
    global my_new_strings
    # If length will be the smallert than the o then the return keybord occur.
    if l<0:
        return
    
    # passed the each char in the newString
    # [[PLEASED NOTE TO UNDERSTAND THIS RECUSION REVERSE YOOU HAVE TO UNDERSTAND HOW RECURSION WORKS]]
    my_new_strings += s[l]
    lets_reverse(s, l-1)
    return my_new_strings


# passed the string and the length of the string in the function as a arguments
l = lets_reverse(another_string, len(another_string)-1)
print(l)