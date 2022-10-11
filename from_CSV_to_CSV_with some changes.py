import csv
"""
text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('check.csv', 'w') as file:
    file.write(text)
"""
with open('data (1).csv', encoding='utf-8') as data, open('domain_usage.csv', 'w', newline='') as outdata:
    l = list(csv.reader(data))
    del l[0]
    lmails = [x.split('@')[1] for x in list(zip(*l))[-1]] #зипуем в кортеж по последнему столбику и генерим в список только домены
    #print(lmails)
    #lmails.sort()
    d = {}
    for el in lmails:
        d[el] = d.get(el, 0) + 1

    print(d)
    write = csv.writer(outdata, delimiter=',')
    write.writerow(['domain', 'count'])
    for k, v in sorted(sorted(d.items(), key=lambda x: x[0]), key=lambda x: x[1]): #сортровка по ключам, потом по значениям но возврат чисто кортежей или тип того
        write.writerow([k, v])
