import numpy as np
import pandas as pd
f=open('new.txt','a')
f.write("what are you doing\n")
f.write("new line\n")
f.write("yesss\n")
f.close()


f=open('new.txt','r')
print(f.read())

# f = open("myfile.txt", "a")
# f.write("what are you doing\n")
# f.close()

# f = open("myfile.txt", "r")
# print(f.read())
