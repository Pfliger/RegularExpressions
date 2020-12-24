from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding='utf8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)


fix_contact = []
for row in contacts_list:
    fio = f'{row[0].strip()} {row[1].strip()} {row[2].strip()}'.split()
    while len(fio) < 3:
        fio.extend([''])
    regex = r"(\+7|8)?\s*\(*(\d{3})\-*\)*\s*(\d{3})\-*(\d{2})[-\s]?(\d{2})[\s]?\(*([доб.]*)\s*(\d+)*\)*"
    subst = "+7(\\2)\\3-\\4-\\5 \\6\\7"
    row[5] = re.sub(regex, subst, row[5])
    fio.extend(row[3:])
    fix_contact.append(fio)

for row in fix_contact:
    for item in fix_contact:
        if row != item and row[0] == item[0] and row[1] == item[1]:
            row[2] = item[2] if item[2] else row[2]
            row[3] = item[3] if item[3] else row[3]
            row[4] = item[4] if item[4] else row[4]
            row[5] = item[5] if item[5] else row[5]
            row[6] = item[6] if item[6] else row[6]
            fix_contact.remove(item)

pprint(fix_contact)

with open("phonebook.csv", "w", encoding='utf8', newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(fix_contact)
