from input_module import take_input
from process_module import process
from output_module import give_output
import welcome
import os

os.system("CLS")
#welcome message
welcome.greet()

while(True):
    i=take_input()
    o=process(i)
    give_output(o)