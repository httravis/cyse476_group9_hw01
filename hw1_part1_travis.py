from collections import OrderedDict

def c_az(key):
    c = ''.join(OrderedDict.fromkeys(key).keys())
    return c

az = 'abcdefghijklmnopqrstuvwxyz'
azlen = len(az)
print(az)
print(azlen)

word = "Banana"
word = word.replace(' ','').lower()
print(word)

word_index = c_az(word)
print(word_index)

w_pattern = ''
for c in range(len(word)):
    wchar = word[c]
    windex = word_index.find(word[c])
    print(c,'\t',wchar,'\t',windex,'\t',az[windex]) 
    w_pattern += az[windex] 

print(word)
print(w_pattern)