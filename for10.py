# Alphabet Design

n=int(input("Enter the value"))
for i in range(n+1,0,-1):
	for j in range(i):
		print(chr(65+j), end=" ")
	print()