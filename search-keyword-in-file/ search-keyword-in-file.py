from email import charset
import re
import codecs


def add_(file, readtype, charset):

  arq = codecs.open(file, readtype, charset)
  readfile = arq.read()
  arq.close()
  return readfile
  

def seach_in_file(readfile, text):

  result = [_ for _ in re.findall(text, readfile)]
  return result


def remove_list_keyword(result, keyreplace):

  formattedlist = []

  for i in result:
    i = str(i)
    string = i.replace(keyreplace, "")
    formattedlist.append(string)

  return formattedlist


file = "test.html" 
readtype = "r"
charset = "utf-8"

readfile = add_(file, readtype, charset)
result = seach_in_file(readfile, "meta...")

print("old list: " , result)


result = remove_list_keyword(result, "meta")

print("new list: ",result)
