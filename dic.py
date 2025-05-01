Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
p_info={'Name':'Noor','age':19,'F_name':'Arshad','Semester':3,'degree':'BBA','Hobby':'reading','university':'Comsat','gender':'Female','city':'lahore','contact':03418610360}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
p_info={'Name':'Noor','age':19,'F_name':'Arshad','Semester':3,'degree':'BBA','Hobby':'reading','university':'Comsat','gender':'Female','city':'lahore','contact':3418610360}
#display information
print(p_info['age'])
19
#accessing value
new_points=p_info['Hobby']
print(new_points)
reading
#add new key-value pair
p_info['']=BBA
KeyboardInterrupt
p_info['CGPA']=3.16
print(p_info)
{'Name': 'Noor', 'age': 19, 'F_name': 'Arshad', 'Semester': 3, 'degree': 'BBA', 'Hobby': 'reading', 'university': 'Comsat', 'gender': 'Female', 'city': 'lahore', 'contact': 3418610360, 'CGPA': 3.16}
#Modifying values
>>> p_info['age']=20
>>> print(p_info)
{'Name': 'Noor', 'age': 20, 'F_name': 'Arshad', 'Semester': 3, 'degree': 'BBA', 'Hobby': 'reading', 'university': 'Comsat', 'gender': 'Female', 'city': 'lahore', 'contact': 3418610360, 'CGPA': 3.16}
>>> del p_info['contact']
>>> print(p_info)
{'Name': 'Noor', 'age': 20, 'F_name': 'Arshad', 'Semester': 3, 'degree': 'BBA', 'Hobby': 'reading', 'university': 'Comsat', 'gender': 'Female', 'city': 'lahore', 'CGPA': 3.16}
>>> #keys
>>> print(p_info.key())
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(p_info.key())
AttributeError: 'dict' object has no attribute 'key'. Did you mean: 'keys'?
>>> print(p_info.keys())
dict_keys(['Name', 'age', 'F_name', 'Semester', 'degree', 'Hobby', 'university', 'gender', 'city', 'CGPA'])
>>> #values
>>> print(p_info.values())
dict_values(['Noor', 20, 'Arshad', 3, 'BBA', 'reading', 'Comsat', 'Female', 'lahore', 3.16])
>>> #items
>>> print(p_info.items())
dict_items([('Name', 'Noor'), ('age', 20), ('F_name', 'Arshad'), ('Semester', 3), ('degree', 'BBA'), ('Hobby', 'reading'), ('university', 'Comsat'), ('gender', 'Female'), ('city', 'lahore'), ('CGPA', 3.16)])
>>> #pop
>>> removed_items=p_info.pop('city')
>>> print(removed_items)
lahore
>>> print(p_info)
{'Name': 'Noor', 'age': 20, 'F_name': 'Arshad', 'Semester': 3, 'degree': 'BBA', 'Hobby': 'reading', 'university': 'Comsat', 'gender': 'Female', 'CGPA': 3.16}
>>> #clear
>>> p_info.clear()
>>> print(p_info)
{}
