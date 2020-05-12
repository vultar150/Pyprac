Adddddddd module
================

Dumb module

How to use
----------

Import addd module:

		>>> import addd

Mulf is for multiplying all arguments:

		>>> addd.mulf(2,3)
		6

In can multiply all:

		>>> addd.mulf(1,2,3,'*')
		'******'

It can not to multiply even:

		>>> addd.mulf(7)
		7

It can not is no multiply:

		>>> addd.mulf()
		Traceback (most recent call last):
		  File "<stdin>", line 1, in <module>
		  File "/Users/vladimirryabchenkov/Documents/progs/Python/python_practicum/20200428/src/doct/addd.py", line 20, in mulf
		    v = vars[0]
		IndexError: tuple index out of range