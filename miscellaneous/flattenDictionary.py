def flatten(parentKey, dictionary, flatDict):
  for key, value in dictionary.items():
    if not isinstance(value, dict):
      if parentKey == '':
        flatDict.update({key:value})
      else:
        flatDict.update({parentKey + '.' + key: value})
    else:
        # if it's a nested dictionary
      if parentKey == '':
        flatten(key, value, flatDict)
      else:
        flatten(parentKey + '.' + key, value, flatDict)
        
def flattenDictionary(dictionary):
  flatDict = {}
  flatten('', dictionary, flatDict)
  return flatDict

inputDict = {
            "Key1" : "1",
            "Key2" : {
                "a" : "2",
                "b" : "3",
                "c" : {
                    "d" : "3",
                    "e" : "1"
                }
            }
        }

print flattenDictionary(inputDict)

