#1
s=[1,2,3,4,5]
s.append(str(12))
s[2]= int(1)
list = [11]
s.append(list)
s[3] = (tuple([11,12]))
print(s[3])
s.remove(5)
print(s.count(1))
print(s)

#2
d = dict();
d["Dimiie"] = 18
d["Veskoo"] = 5
d["Milkoo"] = 18
d[tuple([12,13])] = list[12]
print(d["Dimiie"])
d.pop("Veskoo")
dict = d.keys()
print(d)
print(dict)

#3
#Not working
def tpl_sort():
    k = (2,5,4,1,3)
    result = sorted(k)
    result = tuple(result)
    print(result)