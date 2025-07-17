f = open("demofile.txt")
#print(f.readline())
#f.close()

#Return the 5 first characters of the file:

with open("demofile.txt") as f:
  print(f.read(5))