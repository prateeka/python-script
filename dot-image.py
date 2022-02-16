# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import glob
import subprocess

for f in glob.glob('/home/prateek/Downloads/*dot'):
    command="dot -v -Tjpg %s -o %s-dot.jpg" %(f,f)
    subprocess.run(command, shell=True)
    print("file name is %s " %(f))