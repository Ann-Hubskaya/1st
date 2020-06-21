i = input('Enter your message ')
s = i.find('h')
e = i.rfind('h')
st = i[:s+1]
en = i[e:]
f = i[s+1:e]
print(st + f.replace('h', 'H') + en)

