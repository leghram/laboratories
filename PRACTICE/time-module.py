
#print("this is the time module in python ")

# for comand in ((sys.argv)):
#   if comand in option_list[3]:
#     print(option_list)
#   else:
#     print("nothin")

# meetings = []
# for path in list_files(DIR_PATH):
#     with open(path, 'r', encoding='UTF-16') as file:
#         meeting = process_file_data(file)
#         meetings.append(meeting)

# print(meetings)


from turtle import position


print("_________________")

position = 1
with open("tags.csv","r") as file_tags:
  
  print(file_tags.readline())
  print(">>>>>>>>>>>>>>")
  for line in file_tags:
    print(file_tags.readline())
  #print(file_tags.read())

  #for line in file_tags:
