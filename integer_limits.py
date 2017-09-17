# Copyright 2017 LingxiuGe glxlily@bu.edu
Table = "{:<6} {:<22} {:<22} {:<22}"
print(Table.format('Bytes','Largest Unsigned Int','Minimum Signed Int','Maximum Signed Int'))
for x in range (1,9):
	print(Table.format(x, 2**(8*x) - 1, -2**(8*x-1), 2**(8*x -1)-1))