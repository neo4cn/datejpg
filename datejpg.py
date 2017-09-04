import os

def readfilelist():
  list = os.listdir(r"c:\\")
  print (list)
  for file in list:
    print (file)
  return

readfilelist()