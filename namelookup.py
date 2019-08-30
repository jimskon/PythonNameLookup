#!/usr/bin/env python3
# namelookup.py - Program to display name statistics
# James Skon, 2019
#!/usr/bin/env python

import cgi;
import cgitb
cgitb.enable()


from sortedcontainers import SortedDict
filePath="/home/class/SoftDev/namedata/"

class NameInfo:
  """
  Class to store information about the 
  Statistics of names.
  For each name type, there is a dict
  for each name, there is a list of name %, cumulative %, rank
  """
  def __init__(self, num):
    """ 
    create a NameInfo Structure
    num is the number of types of names
    """
    self.nameData=[]
    for i in range(num):
      self.nameData.append([])
  def addNames(self, nameFile, index):
    """
    create a new list of names with data
    given an index within range of 0..num-1
    """
    names = open(filePath+nameFile)
    nameDict=SortedDict()
    for line in names:
      line=line.strip()
      data=line.split()
      numData=data[1:]
      nameDict[data[0]]=numData
    self.nameData[index]=nameDict
    return
  def lookup(self,name,index):
    """
    lookup name in specified index
    return list of [%,%cum,rank] if in list
    else return none
    """
    return self.nameData[index].get(name)

  def lookup10(self,name,index):
    """
    lookup name in specified index
    return list of [%,%cum,rank] if in list
    else return none
    """
    i=self.nameData[index].bisect_right(name)
    low = max(0,i-5)
    high = min(len(self.nameData[index]),i+5)
    result=""
    for j in range(low,high):
      result+=self.nameData[index].peekitem(j)[0]+","
      result+=self.nameData[index].peekitem(j)[1][0]+","
      result+=self.nameData[index].peekitem(j)[1][2]+","
    result=result[:-2]  
    return result


def print_header():
    print ("""Content-type: text/html\n""")

def main():
  nameInfo=NameInfo(3)
  nameInfo.addNames('dist.female.first',0)
  nameInfo.addNames('dist.male.first',1)
  nameInfo.addNames('dist.all.last',2)

  form = cgi.FieldStorage()
  if (form.getvalue("name") and form.getvalue("type_select")):
      print_header()
      name=form.getvalue("name").upper()
      ltype=form.getvalue("type_select")
      index=2
      if ltype=="female":
        index=0
      elif ltype=="male":
        index=1
      data=nameInfo.lookup10(name,index)
      print(data)
  else:
      print("Error in submission")
        
main()
