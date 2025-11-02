import sys
import os

with open(sys.argv[1]) as file:
    scr = file.read()

with open("template") as file:
    rps = file.read().replace("<command>",scr.replace("\n","\\n"))

with open(os.path.splitext(os.path.basename(sys.argv[1]))[0] + ".c","w") as file:
        file.write(rps)