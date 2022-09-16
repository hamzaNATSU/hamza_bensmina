import dns.resolver
b = open("keywords.txt","r")
x = open('domaines.txt','w+')
for key in b.read().splitlines():
    try:
        answers = dns.resolver.resolve(key,'A')
        x.write(key+' ---------nonvalid\n')
        for ans in answers:
            print(key+ ': ' + ans.to_text())
    except dns.resolver.NoNameservers:
        print(key + ' '+'disponible\n')
        x.write(key+' ---------disponible\n')
    except:
        print(key + ' '+'disponilble')
        x.write(key+' ---------dispo\n')
x.close()
b.close()
