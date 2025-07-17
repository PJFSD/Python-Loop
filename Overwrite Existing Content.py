#with open file "demofile.txt", "W") as f:
f.writen("Woops! I have delected the content")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())