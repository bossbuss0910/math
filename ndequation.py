# -*- coding: utf-8 -*-
import numpy 

'''
2x1+5x2=17
5x1-2x2=-1 の連立方程式を求める
'''

def inver(a1,a2,b1,b2):
	mat=numpy.matrix([[a1,a2],[b1,b2]])
	return mat.I

def ans(con1,con2,inver_mat):
	con_vec=numpy.matrix([[con1],[con2]])
	return numpy.dot(inver_mat,con_vec)

ans_mat=ans(17,-1,inver(2,5,5,-2))

for index,num in enumerate(ans_mat):
	print "x{0}={1}".format(index,num)
