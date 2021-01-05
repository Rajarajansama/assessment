l = [['a','b','c'],
	 ['d','e','f'],
	 ['g','h','i']
	]

print("before transposing matrix ")
for i in range(len(l)):
	ll = l[i]
	for j in range(len(ll)):
		print(l[i][j], end=' ')
	print()
print()
print("After transposing matrix ")
for i in range(len(l)):
	ll = l[i]
	for j in range(len(ll)):
		print(l[j][i], end=' ')
	print()
	
