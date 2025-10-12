new_file = open('New_File.txt', 'x')
new_file.close()
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my__file.txt")
else:
    print('Th efile does not exist')
my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Penguin and I am 1 yr old.")
my_file.close()
os.remove('Codingal.txt')