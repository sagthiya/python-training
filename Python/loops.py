#While loop
i = 1

while(i<51):
    print(i)
    i +=1 # or i = i + 1


#For loops
for i in range(4):
    print(i)
print("\n")

# for with else
print("for with loop")
l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!
print("\n")

# For Loop with Lists
print("For Loop with Lists")
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

# For Loop with Tuples
print("\n")
print("For Loop with Tuples")
t = (6, 231, 75, 122)
for i in t:
    print(i)

# For Loop with Strings
print("\n")
print("For Loop with Strings")
s = "ranjit"
for i in s:
    print(i)