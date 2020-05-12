'''
'''

def mulf(*vars):
	'''Returns vars[0] * vars[1] * ...
>>> mulf()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/vladimirryabchenkov/Documents/progs/Python/python_practicum/20200428/src/doct/addd.py", line 18, in mulf
    v = vars[0]
IndexError: tuple index out of range
>>> mulf(2)
2
>>> mulf(2,4,5,6)
240
>>> mulf(2,4,5,"@")
'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@'
>>>
'''
	v = vars[0]
	for i in vars[1:]:
		v *= i
	return v