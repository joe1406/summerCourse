f = open('text.csv','w')
f.write('hello\nmy name is Eissa!\n\n')
f.close()

f = open('text.csv', 'r')
lines = f.readlines()
print(lines)
f.close()

f = open('text.csv', 'w')
f.write('hello\nmy name is Mohsin!')
f.close()

f = open('text.csv', 'r')
lines = f.readlines()
print(lines)
f.close()