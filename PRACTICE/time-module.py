
#print("this is the time module in python ")

import sys

option_list = ["option_1","option 2", "option 3","--help"]


for comand in ((sys.argv)):
  if comand in option_list[3]:
    print(option_list)
  else:
    print("nothin")



