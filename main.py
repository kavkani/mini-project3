def african_ref():
    pmd = open('referees.csv', encoding='utf-8')
    pmd1 = pmd.readlines()
    return pmd1


lst1 = african_ref()
africn_ref_lst = []
for i in lst1:
    lst1.append(i[:-1].split(','))

print(lst1)