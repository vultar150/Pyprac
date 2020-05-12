'''
'''

def mulf(*vars):
	'''Returns vars[0] * vars[1] * ...
>>> modul.mulf(1,2)
2
>>> modul.mulf(1,2, 3)
6
>>> modul.mulf()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/vladimirryabchenkov/Documents/progs/Python/python_practicum/20200428/src/doct/modul/__init__.py", line 6, in mulf
    v = vars[0]
IndexError: tuple index out of range
>>>
'''
	v = vars[0]
	for i in vars[1:]:
		v *= i
	return v