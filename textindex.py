def removePunctuation(s):
  "Remove all punctuation from a string"
  import string
  for c in string.punctuation:
    s= s.replace(c,"")
  return s

def addToIndex(index,word,line):
  if word not in index:
    index[word]=[line] # make new entry
  else:
    index[word].append(line)

class textindex:

  def __init__(self,filename):
    "Create a dictionary of all words, with the key being the word, and the value being the number of times the word is found"
    self.index={}
    inFile = open(filename,"r")
    pos=0
    line=inFile.readline()
    while len(line)>0:
      line=line.strip().lower()
      line=removePunctuation(line.lower())
      words=line.split()
      for word in words:
        addToIndex(self.index,word,pos)
      pos=inFile.tell()  # Next line position
      line=inFile.readline()
    return

  def wordcount(self):
    return len(self.index)

  def lookup(self,word):
    word=word.lower()
    if word in self.index:
      lines=self.index[word]
      return lines
    else:
      return []
