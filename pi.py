# Version 1
# Very time cosuming, but it works no doubt!

decimals = 10000
PI = [0 for i in range(decimals)]
temp = [0 for i in range(decimals)]

def div(n):
	global temp
	dividend = 1
	i = 0
	temp = [0 for i in range(decimals)]

	while True:
		while dividend < n:
			dividend *= 10
			i += 1

		temp[i] = (dividend - dividend%n)//n
		dividend = dividend % n

		if dividend == 0 or i >= decimals-100:
			break
	return temp


def add(sa):
	#global PI, temp
	#print(temp)
	if sa == 1:
		if temp[0] == 1:
			PI[0] += 1

		for i in range(len(temp)-1,0,-1):
			PI[i] += temp[i]

		for i in range(len(PI)-1,1,-1):
			if PI[i] >= 10:
				PI[i] = PI[i] - 10
				PI[i-1] += 1
		
		if PI[1] >= 10:
			PI[1] = PI[1] - 10
			PI[0] += 1

	elif sa == -1:
		if temp[0] == 1:
			PI[0] -= 1

		for i in range(len(temp)-1,0,-1):
			PI[i] -= temp[i]

			if PI[i] < 0:
				PI[i-1] -= 1
				PI[i] += 10

	return PI

def mul(M):
	p = 0

	for i in range(len(M)-1,0,-1):
		M[i] = M[i]*4 + p
		if M[i] > 9:
			p = (M[i] - M[i]%10)//10
			M[i] = M[i]%10
		else:
			p = 0
	M[0] = M[0]*4 + p

	return M

def show(PI):
	print(PI[0],end=".")

	for i in range(1,len(PI)):
		print(PI[i],end="")

p = decimals

for i in range(p):
	temp = div(2*i + 1)
	PI = add((-1)**i)  #(-1)**i

PI = mul(PI)

show(PI)
