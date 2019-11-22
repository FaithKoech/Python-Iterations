# a.Write a program that prints your name 100 times.

i=0
while i<=100:
    i = i + 1
    print("Faith")


# b.Write a program that outputs 100 lines, numbered 1 to 100, each with your name on it. The output should look like the output below.
#
# 1 Your name
#
# 2 Your name
#
# 3 Your name
#
# 4 Your name
i =0
for i in range(100):
    print(i+1,"Faith")

# i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1

# c. Write a program that uses a for loop to print the numbers 8, 11, 14, 17, 20, . . . , 83, 86, 89.
for i in range (8,91, +3):
    print(i)

i = 1
while i<6:
    print(i)
    i=i+1
else:
    print("i is no longer less that 6")
