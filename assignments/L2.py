def print_line(i):
    for c in range(0,i):
        print("*", end="")
    print("")
        

print("Enter a number : ", end="")
n = int(input())

'''
Examples:
=============
input: 1
output: 

=============
input: 2
output: 
*
=============
input: 5
output: 
*
**
**
*
=============
input: 10 
output: 
*
**
*
****
*
****
*
**
*
'''

for i in range(0, n):
    # Add your code below this line