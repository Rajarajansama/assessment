l= [[10,20,30],
	 [40,50,60],
	 [70,80,90]
	]
for i in range(len(l)):
	ll = l[i]
	for j in range(len(ll)):
		if i==j:
			print(l[i][j])
