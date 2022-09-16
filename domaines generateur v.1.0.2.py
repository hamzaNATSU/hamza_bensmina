import itertools
import dns.resolver
print('please choose type of generating ... \n 1. letters \n 2.number \n 3.both ')
type = input('insert "1" or "2" or "3" : ')
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
numlett = []
for i in letters:
    numlett.append(i)
for j in numbers:
    numlett.append(j)
domaine = input('insert the domaine (".xxx") :')
string = ''
array_string = []
string_len = int(input(' insert length of domaine : '))

if type== '1':
    for pair in itertools.product(letters, repeat = string_len):
        array_string.append(''.join(pair))
    for i in range (len(array_string)):
        array_string[i] += '.' + domaine
elif type== '2':
    for pair in itertools.product(numbers, repeat = string_len):
        array_string.append(''.join(pair))
    for i in range (len(array_string)):
        array_string[i] += '.' + domaine
elif type== '3':
    for pair in itertools.product(numlett, repeat = string_len):
        array_string.append(''.join(pair))
    for i in range (len(array_string)):
        array_string[i] += '.' + domaine
print('hi')
b = open("keywords.txt","w+")
for key in array_string:
    try:
        answers = dns.resolver.resolve(key,'A')
        b.write(key+' -----nonvalid\n')
        for ans in answers:
            print(key + ': ' + ans.to_text())
    except dns.resolver.NoNameservers:
        b.write(key+' -----nonvalid\n')
        print(key + ': checked(no ip)')
    except:
        print(key + 'erreur')
        b.write(key+' -----valid\n')
b.close()
print('succeed')
print('total keywords : ', len(array_string))
