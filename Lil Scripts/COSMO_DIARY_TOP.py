from datetime import datetime

def is_data(dt):
    try:
        datetime.strptime(dt, '%d.%m.%Y; %H:%M')
        return True
    except:
        return False

with open('diary.txt', 'rt', encoding='utf-8') as file, open('cosmo.txt', 'w') as cosmo:
    l = [x.strip() for x in file.readlines()]
    #print(l)
    dic = {}

    for el in l:
        if is_data(el):
            block = el
            dic[block] = dic.get(block, [])
        elif not is_data(el) and el != '':
            dic[block].append(el)

    ldicsort = sorted(dic, key=lambda x: datetime.strptime(x, '%d.%m.%Y; %H:%M'))
    #print(ldicsort)
    for keyword in ldicsort:
        print(keyword, file=cosmo)
        print(*dic[keyword], sep='\n', end='', file=cosmo)
        if keyword != ldicsort[-1]:
            print('\n', file=cosmo)

print(dic)

#print(dic)