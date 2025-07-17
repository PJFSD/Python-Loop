import os
if os.path.exists("demofile.txt"):
    od.remove("demofile.txt")
else:
    print("The file does not exist")
