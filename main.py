from flow_chart import *


# opens, clears, and writes heading to process tracking file
w = open('fullprocess.txt', 'w')
w.write('Full process:\n\n')
w.close()

#runs the program
run(start)    #if you changed the name of the first step from start, also change this to call the first step

