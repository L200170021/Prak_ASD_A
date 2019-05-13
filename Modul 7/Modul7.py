#######============Nama = Adnan Shafry Ari Purnama Aji===========#########
#######=====================NIM = L200170021 ===================#########
#######=====================Kelas = A ==========================#########
#######=====================Modul = 7===========================#########


import re

##no 1
file = open("KamenRider.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
p = r"me\w+"
string = re.findall(p, teks)
print("No. 1")
print(string)


##no 2
file = open("KamenRider.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
d = r"di\w+"
string = re.findall(d, teks)
print("""

No. 2""")
print(string)


##no 3
file = open("KamenRider.txt", "r", encoding = 'latin1')
teks = file.read()
file.close()
e = r"di\s\w+"
string = re.findall(e, teks)
print("""

No. 3""")
print(string)


##no 4a
f = open('KEI.html', 'r', encoding='latin1')
teks = f.read()
f.close()
pola = r'([\w+]+)</a></td>'
tampil = re.findall(pola, teks)
print("""

No. 4a""")
print(tampil)


##no 4b
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
string = re.findall(r'title="([\w+]+)">',teks)
##
string = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
list = []
for i in string:
    list.append((i[0], float(i[1])))
print("""

No. 4b""")
print(tampil)
print(list)

