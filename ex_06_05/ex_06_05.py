str = 'X-DSPM-Confidence: 0.8475'

name = str.find(':')
# print(name)
map = str[name+2 :]
value = float(map)
print(value)
