i = input('Enter your message ')
s = i.find('h')
e = i.rfind('h')
st = i[:s]
en = i[e:]
f = i[s:e]
print(st + f.replace('h', 'H') + en)

