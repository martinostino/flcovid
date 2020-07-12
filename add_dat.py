import matplotlib.pyplot as plt
import numpy as np

myfile = open("fl_dat.csv","a")
#everything = myfile.readlines()

date = input("What is the date? (mm-dd)")
num_pos = input("How many positive cases?")
rate_pos = input("What is the positive rate?")
statement = "{},{},{}\n".format(date,num_pos,rate_pos)
myfile.write(statement)
print("Data inputted. Thank You!")

myfile.close()