# Softmax in python
import numpy as np
import array
import math
import matplotlib.pyplot as plt

m = [[1.0, 1.2], [0.7, 3.0], [1.1, 2.9]]


m3 = [[1.0, 2.0, 3.0], [2.5, 3.5, 4.5]]

m2 = [3.0, 1.0, 0.2]


#m4 = np.vstack([m2, [2*i for i in m2]])

def shape(l):
	if (type(l[0]) == type([])):
		return [len(l)] + shape(l[0])
	else:
		return [len(l)]

# simple one liner, great for vectors, returns the wrong result on matrices
def softNP(x):
	return np.exp(x) / np.sum(np.exp(x))

# fixes the one liner for matrices.
def softMat(x):
	s = shape(x)
	print s
	o = []
	for i in range(s[0]):
		if len(s) > 1:
			#print x[i]
			o.append(softNP(x[i]))
		else: 
			o = softNP(x)
	return o

#takes matrices or vectors, kinda manual and slow, only uses math
def softmax(a):
	s = shape(a)
	inc = [0]*s[0]
	o = []
	for i in range(s[0]):
		if len(s) > 1:
			for j in range(s[1]):
				#print a[i][j]
				inc[i] += math.exp(a[i][j])
		else: 
			inc[0] += math.exp(a[i])
	for i in range(s[0]):
		if len(s)>1:
			o.append([])
			for j in range(s[1]):
				o[i].append(math.exp(a[i][j])/inc[i])
		else:
			o.append(math.exp(a[i])/inc[0])
	return o

#faster, uses numpy creates a nonsense variable temporarily;
# some people like this trick according to the internet very similar 
# to the above method, but uses this algebraic trick
def softmax_2(x):
    e_x = np.exp(x - np.ones_like(x))
    out = e_x / e_x.sum()
    return out

print softMat(m)
print softMat(m2)
print softMat(m3)
print softMat(m4)

# print np.abs(m)
# print np.sum(m, axis=0)
# print np.sum(m, axis=1)
# print shape(m)
# print shape(m2)
# print softmax(m)
# print softmax(m2)
# print np.sum(softNP(m), axis=1)
# print np.sum(softNP(m), axis=0)
# print softNP(m2)
# print softNP(m3)
# print softNP(m4).T
# print shape(m)