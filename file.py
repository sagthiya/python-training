#read file
f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()


# file write
st = "Hi how you are you"

f = open("demo.txt", "w")

f.write(st)

f.close()


#APPEND text in file
st = "hello every one"

f = open("demo.txt", "a")

f.write(st)

f.close()