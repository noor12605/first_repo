Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sum=0
>>> for i in range(1,6):
	if i==3:
		break
	sum=sum+i
	print("sum",sum)

	
sum 1
sum 3
>>> sum=0
>>> for i in range(1,6):
	if i==4:
		continue
	sum=sum+i
	print("sum",sum)

	
sum 1
sum 3
sum 6
sum 11
>>> names_tuple=('jungkook','jimin','taehyung','suga','jhope')
>>> print(names_tuple[2])
taehyung
>>> print(names_tuple[-1])
jhope
>>> # immutability of tuples
>>> names_tuple[1]='jin'
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    names_tuple[1]='jin'
TypeError: 'tuple' object does not support item assignment
>>> tuple1=(1,2,3)
>>> tuple2=('Namjoon',)
>>> combined_tuple= tuple1 + tuple2
>>> print(combined_tuple)
(1, 2, 3, 'Namjoon')
>>> tuple3=('Jin',)
>>> repeat=tuple3*5
>>> print(repeat)
('Jin', 'Jin', 'Jin', 'Jin', 'Jin')
>>> numbers=(0,1,2,3,4,6,5,7)
>>> print(numbers[2:5])
(2, 3, 4)
>>> names_tuple=('jungkook','jimin','taehyung','suga','jhope')
>>> print(names_tuple.index('suga'))
3
>>> 