from math import sqrt
from sys import argv
def s( a ,b ,c ):
	if ( b* b-4* a* c )< 0:return None ,None ,None ,None
	p=( -b+ sqrt( b *b-4 *a*c ) )/( 2 *a )
	D=( -b-sqrt( b *b-4 *a*c ) )/( 2 *a )
	if p<0:x1 ,x2=None ,None
	else:x1 ,x2=sqrt( p ) ,-sqrt( p )
	if D<0:x3 ,x4=None,None
	else:x3 ,x4 =sqrt( D ) ,-sqrt( D )
	return x1 ,x2 ,x3 ,x4
a ,b ,c=int( argv[ 1 ] ) ,int( argv[ 2 ] ) ,int( argv[ 3 ] )
print( s( a ,b ,c ) )