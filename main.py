def ref_reader():
    lst = open('referees.csv', encoding='utf-8')
    lst1 = lst.readlines()

    pmd = []
    for i in lst1:
        pmd.append(i[:-1].split(','))

    ref_codes = []
    for j in pmd[1:]:
        ref_codes.append(j[3])

    return ref_codes


def african_ref_detect():
    ref_code_input_from_def = ref_reader()
    african_ref_years = []
    for i in range(len(ref_code_input_from_def)):
        if i == 'Egypt':
            african_ref_years.append(i)
        if i == 'Libya':
            african_ref_years.append(i)
        if i == 'Morocco':
            african_ref_years.append(i)
        if i == 'Tunisia':
            african_ref_years.append(i)
        if i == 'Algeria':
            african_ref_years.append(i)
        if i == 'Niger':
            african_ref_years.append(i)
        if i == 'Benin':
            african_ref_years.append(i)
        if i == 'Senegal':
            african_ref_years.append(i)
        if i == 'Côte dIvoire':
            african_ref_years.append(i)
        if i == 'Ghana':
            african_ref_years.append(i)
        if i == 'Gambia':
            african_ref_years.append(i)
        if i == 'Mauritius':
            african_ref_years.append(i)
        if i == 'Seychelles':
            african_ref_years.append(i)
        if i == 'Zambia':
            african_ref_years.append(i)
        if i == 'Ethiopia':
            african_ref_years.append(i)

    return african_ref_years

print(african_ref_detect())

def y_ref():
    referee_appearances = open('referee_appearances.csv')

