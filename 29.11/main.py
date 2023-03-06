#1
import json

first_dictionary = {
                        "name":"Dimiie",
                        "lastname":"Dimitrov",
                        "age":18,
                        "car":"Toyota Supra",
                        "number":16
}
JSON_object = json.dumps(first_dictionary,indent = 3)
first_JSON_file = open("file.txt","w")
first_JSON_file.write(JSON_object)

#2
myfile = open("file.txt","r")

for line in myfile:
    print(line)

myfile.close()

#3
newfile = open("document.BIN", mode="w", encoding="utf-8")
for iterator in range(1):
    newfile.write("This is good")
newfile.close()
newfile = open("document.BIN", mode="r", encoding="utf-8")
print(newfile.read(4))

