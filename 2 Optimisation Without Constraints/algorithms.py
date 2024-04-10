import numpy.linalg as nplinalg
import math

#viena gradientinio nusileidimo iteracija 
#one gradient descent iteration
def gradient_iteration(f, x, y, gamma, grad):
	x_new = x - gamma * grad[0]
	y_new = y - gamma * grad[1]
	z_new = f([x_new, y_new])
	return x_new, y_new, z_new

#gradientinis nusileidimas
#gradient descent
def gradient_descent(f, f_gradient, X0, gamma, eps):
	X = [[X0[0], X0[1], f([X0[0], X0[1]])]]
	for i in range(1000):
		grad = f_gradient(X[i])
		if grad==[0,0]:
			break
		x_new, y_new, z_new = gradient_iteration(f, X[i][0], X[i][1], gamma, grad)
		X.append([x_new, y_new, z_new])
		if nplinalg.norm(grad) < eps:
			break
	return X[-1], X

#greiciausias nusileidimas
#steepest descent
def fastest_descent(f, f_gradient ,X0, eps):
	X = [[X0[0], X0[1], f([X0[0], X0[1]])]]
	for i in range(1000):
		grad = f_gradient(X[i])
		if grad==[0,0]:
			break
		#geriausio zingsnio daugiklio paieska naudojant intervalo dalijimo pusiau algoritma
		gamma = half_optimize_for_fastest_descent(f, X[i], grad, 0, 4, 0.0001)
        #viena iteracija su geriausiu zingsniu
		x_new, y_new, z_new = gradient_iteration(f, X[i][0], X[i][1], gamma, grad)
		X.append([x_new, y_new, z_new])
		if nplinalg.norm(grad) < eps:
			break
	return X[-1], X

#intervalo dalijimo pusiau algoritmas pritaikytas greiciausiam nusileidimui
#interval halving algorithm adapted for fastest descent
def half_optimize_for_fastest_descent(f, Xi, grad, l, r, eps):
	def func(x):
		return f([Xi[0] - x * grad[0], Xi[1] - x * grad[1]])
	xm = (l + r) / 2
	fm = func(xm)
	L = r - l
	while L >= eps: 
		x1 = l + L / 4
		f1 = func(x1)
		if f1 < fm:
			r = xm
			xm = x1
			fm = f1
		else:
			x2 = r - L / 4
			f2 = func(x2)
			if f2 < fm:
				l = xm
				xm = x2
				fm = f2
			else:
				l = x1
				r = x2
		L = r - l
	return xm

#deformuojamo simplekso algoritmas
#deformed simplex algorithm
def deformed_simplex(f, X0, n, eps, alpha, beta, gamma, niu):
	def sort_simplex(X):
		return sorted(X, key=lambda x: x[-1])
	def deform_simplex(midpoint, reflection, theta):
		Deformed = [0] * (n + 1)
		for i in range(n):
			Deformed[i] = midpoint[i] + theta * (reflection[i] - midpoint[i])
		Deformed[n] = f(Deformed)
		return Deformed
	checkpoints = []
	delta_1 = (math.sqrt(n+1)+n-1)/(n*math.sqrt(2))*alpha
	delta_2 = (math.sqrt(n+1)-1)/(n*math.sqrt(2))*alpha
	X = [[0] * (n + 1) for _ in range(n + 1)]
	X[0]=[X0[0], X0[1], f(X0)]
	for i in range(1, n+1):
		for j in range(0, n):
			if i!=j+1:
				X[i][j]=X0[j]+delta_1
			else:
				X[i][j]=X0[j]+delta_2
		X[i][n]=f(X[i])
	checkpoints.append(X)

	for iteration in range(1000):
		X = sort_simplex(X)
		#Xl=X[0] geriausiais
		#Xg=X[n-1] antras pagal bloguma
		#Xh=X[n] blogiausias
  
		#X[0] best
		#X[n-1] second worst
		#X[n] worst
		if math.sqrt(sum((X[n][i]-X[0][i])**2 for i in range(n))) < eps:
			break
		#naujo tasko skaiciavimas
		#new point calculation
		Midpoint = [0] * (n + 1)
		for i in range(0, n):
			Midpoint[i]=(X[0][i]+X[n-1][i])/2
		Reflection = [0] * (n + 1)
		for i in range(0, n):
			Reflection[i]=Midpoint[i]+(Midpoint[i]-X[n][i])
		Reflection[n] = f(Reflection)
		#jeigu naujas taskas yra mazesnis nei maziausia simplekso virsune
		#if new point is smaller than the smallest vertex of the simplex
		if Reflection[n]<X[0][n]:
			#ispletimas
			#expansion
			Deformed = [0] * (n + 1)
			Deformed = deform_simplex(Midpoint, Reflection, gamma)
			if Deformed[n]<Reflection[n]:
				X[n]=Deformed
			else:
				X[n]=Reflection
		elif Reflection[n]<X[n-1][n]:
			X[n]=Reflection
		elif Reflection[n]<X[n][n]:
			#sutraukimas
			#contraction
			Deformed = [0] * (n + 1)
			Deformed = deform_simplex(Midpoint, Reflection, beta)
			if Deformed[n]<Reflection[n]:
				X[n]=Deformed
			else:
				X[n]=Reflection
		else:
			#mazinimas
			#shrinking
			Deformed = [0] * (n + 1)
			Deformed = deform_simplex(Midpoint, Reflection, niu)
			X[n]=Deformed

		#apribojimas siekiant teigiamu x1 ir x2 reiksmiu sprendziamo uzdavinio atveju
		#restriction for positive x1 and x2 values in the case of the given problem
		while any(X[n][i] < 0 for i in range(n)):
			#mazinimas
			#shrinking
			Deformed = [0] * (n + 1)
			Deformed = deform_simplex(Midpoint, Reflection, niu)
			X[n]=Deformed
		
		checkpoints.append(X)

	X = sort_simplex(X)
	return X[0], checkpoints