import numpy as np #grafiko taškams
import matplotlib.pyplot as plt #grafikams
import math #matematiniams veiksmams
import time #laiko matavimui

# funckija ir jos išvestinės
def f(x):
	return (x**2 - 7)**2 / 4 - 1
def f_derivative(x):
	return x**3 - 7*x
def f_second_derivative(x):
	return 3*x**2 - 7

# auksinio pjūvio metodo konstanta
t = ( -1 + math.sqrt(5) ) / 2

# funkcija, atvaizduojanti duomenis
def plot(data):
	title, result, checkpoints = data #grafiko duomenys
	global plt_index #grafiko indeksas

	axs[plt_index].plot(x, y, color='black', label=r'$f(x) = \frac{(x^2 - 7)^2}{4} - 1$') #funkcijos atvaizdavimas
	axs[plt_index].scatter(result[0], result[1], color='red', label='Rezultatas', marker="d") #rezultato atvaizdavimas
	axs[plt_index].scatter(*zip(*checkpoints), color='blue',  label='Tikrinimo taškai', marker=".") #tikrinimo taškų atvaizdavimas
	axs[plt_index].set_xlabel('x') 
	axs[plt_index].set_ylabel('f(x)')
	axs[plt_index].set_ylim([-10,650])
	axs[plt_index].set_title(title)
	axs[plt_index].grid(True)
	axs[plt_index].legend()
	plt_index += 1

# Intervalo dalijimo pusiau metodas
def half_optimize(l, r, eps):
	function_calls = 0 #funkcijos kvietimų skaičius
	start_time = time.time() #laiko matavimo pradžia
	xm = (l + r) / 2 #vidurio taškas
	fm = f(xm) #vidurio taško reikšmė
	function_calls += 1 #funkcijos kvietimų skaičiaus padidinimas
	L = r - l #intervalo ilgis
	checkpoints = [] #tikrinimo taškai
	itteration = 0 #iteracijų skaičius

	while L >= eps: 
		x1 = l + L / 4
		x2 = r - L / 4
		f1 = f(x1)
		f2 = f(x2)
		function_calls += 2 #funkcijos kvietimų skaičiaus padidinimas
		checkpoints.extend([(x1, f1), (x2,f2)]) #tikrinimo taškų papildymas

		if f1 < fm:
			r = xm
			xm = x1
			fm = f1
		elif f2 < fm:
			l = xm
			xm = x2
			fm = f2
		else:
			l = x1
			r = x2

		L = r - l
		itteration += 1

	result = (xm, f(xm)) #rezultatas. funkcijos skaiciavimas kvieciamas vizualizacijai
	end_time = time.time() #laiko matavimo pabaiga
	title = 'Intervalo dalijimo pusiau metodas'

	#rezultatai konsolėje
	print(title) #pavadinimas
	print(f"{end_time - start_time} sekundės") #skaičiavimo laikas
	print(f"{itteration} iteracijos(ų)") #iteracijų skaičius
	print(f"{function_calls} funkcijos kvietimai") #funkcijos kvietimų skaičius
	print(f"x={result[0]} \nf(x)={result[1]} \n") #rezultatas

	for i in checkpoints:
		print(i[1])
	print (result[1])
	print ("\n")

	return title, result, checkpoints

# Auksinio pjūvio metodas
def golden_optimize(l, r, eps):
	function_calls = 0 #funkcijos kvietimų skaičius
	start_time = time.time() #laiko matavimo pradžia
	global t #auksinio pjūvio konstanta
	L = r - l #intervalo ilgis
	x1 = r - t * L 
	x2 = l + t * L
	f1 = f(x1)
	f2 = f(x2)
	function_calls += 2 #funkcijos kvietimų skaičiaus padidinimas

	checkpoints = [] #tikrinimo taškai
	itteration = 0 #iteracijų skaičius

	while L >= eps:
		checkpoints.extend([(x1, f1), (x2,f2)]) #tikrinimo taškų papildymas
		if f2 < f1:
			l = x1
			L = r - l
			x1 = x2
			f1 = f2
			x2=l+t*L
			f2 = f(x2)
		else:
			r = x2
			L = r - l
			x2 = x1
			f2 = f1
			x1 = r - t * L
			f1 = f(x1)
		function_calls += 1 #funkcijos kvietimų skaičiaus padidinimas
		itteration += 1

	result = (x1, f1) if f1 < f2 else (x2, f2) #rezultatas
	end_time = time.time() #laiko matavimo pabaiga

	title = 'Auksinio pjūvio metodas'
	#rezultatai konsolėje
	print(title) #pavadinimas
	print(f"{end_time - start_time} sekundės") #skaičiavimo laikas
	print(f"{itteration} iteracijos(ų)") #iteracijų skaičius
	print(f"{function_calls} funkcijos kvietimai") #funkcijos kvietimų skaičius
	print(f"x={result[0]} \nf(x)={result[1]} \n") #rezultatas

	for i in checkpoints:
		print(i[1])
	print (result[1])
	print ("\n")

	return title, result, checkpoints

# Niutono metodas
def newton_optimize(x1, eps):
	function_calls = 0 #funkcijos kvietimų skaičius
	start_time = time.time() #laiko matavimo pradžia
	itteration = 0 #iteracijų skaičius
	checkpoints = [] #tikrinimo taškai

	x0 = x1+eps+1 # x0 reikšmės pakeitimas į tokią, kad prasidėtų ciklas

	while abs(x1-x0)>eps:
		x0 = x1
		fx0 = f(x0) #kvieciama tik vizualizacijai
		checkpoints.append((x0, fx0))
		fdx0 = f_derivative(x0)
		fddx0 = f_second_derivative(x0)
		function_calls += 2 #funkcijos kvietimų skaičiaus padidinimas
		x1 = x0 - fdx0/fddx0
		itteration += 1

	result = (x1, f(x1)) #rezultatas
	end_time = time.time() #laiko matavimo pabaiga
	title = 'Niutono metodas'
	#rezultatai konsolėje
	print(title) #pavadinimas
	print(f"{end_time - start_time} sekundės") #skaičiavimo laikas
	print(f"{itteration} iteracijos(ų)") #iteracijų skaičius
	print(f"{function_calls} funkcijos kvietimai") #funkcijos kvietimų skaičius
	print(f"x={result[0]} \nf(x)={result[1]} \n") #rezultatas

	for i in checkpoints:
		print(i[1])
	print (result[1])
	print ("\n")
	return title, result, checkpoints


l = 0 #intervalo pradžia
r = 10 #intervalo pabaiga
eps = 10**(-4) #tikslumas

x = np.linspace(l, r, 1000) #funckijos atvaizdavimui
y = f(x) #funckijos atvaizdavimui


fig, axs = plt.subplots(1) #grafikų apibrėžimas
if not isinstance(axs, (list, np.ndarray)):
	axs = [axs]
plt_index = 0 #grafikų indeksas

plot(half_optimize(l, r, eps)) #intervalo dalijimo pusiau metodas ir jo atvaizdavimas
# plot(golden_optimize(l, r, eps)) #auksinio pjūvio metodas ir jo atvaizdavimas
# plot(newton_optimize(37, eps)) #niutono metodas ir jo atvaizdavimas

plt.tight_layout() #talpus grafikų išdėstymas

plt.show() #grafikų atvaizdavimas