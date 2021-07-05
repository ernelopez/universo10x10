# -*- coding: latin-1 -*-
# http://effbot.org/tkinterbook/canvas.htm

import tkinter as Tk
from sys import stdout, exit
from random import randint
from itertools import repeat

tamanio = 10
cantColores = 4
universo = [[[ 0 for x in range(tamanio)] for y in range(tamanio) ] for z in range(cantColores) ]
univInic = [[[ 0 for x in range(tamanio)] for y in range(tamanio) ] for z in range(cantColores) ]
cabezal = [0,0] 
cabInic = [0,0]
colores = ['R','V','A','N']
direcciones = ['S','E','N','O']

#------------------------------------------------------------
# parámetros ventana gráfica
#------------------------------------------------------------

mp = 500 #media pantalla
anchoPantalla = 2 * mp
altoPantalla  = mp
root = Tk.Tk()
root.title('ENTRADA y SALIDA')
c = Tk.Canvas(root, width=anchoPantalla, height=altoPantalla)
c.pack()	

color = ["#33f","#f04","#0f0","#f70","#fff","#b99","#000"]  
# 0=azul, 1=rojo, 2=verde, 3=anaranjado, 4=blanco, 5=grisTopo, 6=negro

fontBolas = 8
fontLineas = 12
fontTitulos = 14
fontBoom = 150

offset = 10
ladoCelda = 15
entreCeldas = 3

#---- constantes de sintonización de la imágen ---------------
ep0 = 42 # ajuste horizontal de títulos
ep2 = 3 # ajuste vertical de títulos
ep1 = 18 # ajuste horizontal de números verticales de línea
ep3 = 8 # ajuste vertical de números verticales de línea
ep4 = 4 # ajuste vertical de números horizontales superiores de columna
#-------------------------------------------------------------

#-------------------------------------------------------------
#  Funciones de arranque 
#-------------------------------------------------------------
 
def Inicio():
	inicUniv()
	return 0
	
#-------------------------------------------------------------
		
def inicUniv():	
	cabInic[0] = cabezal[0]
	cabInic[1] = cabezal[1]
	for i in range(tamanio):
		for j in range(tamanio):
			for k in range(cantColores):
				univInic[k][j][i] = universo[k][j][i]
				
	
#-------------------------------------------------------------
#  Funciones Primitivas básicas 
#-------------------------------------------------------------
 
def Mover(d):
	global cabezal
	if d == 'E':
		if cabezal[0] < tamanio - 1:
			cabezal[0] += 1
		else:
			bum()
			exit( 0 )
	elif d == 'O': 		
		if cabezal[0] > 0:
			cabezal[0] -= 1
		else:
			bum()
			exit( 0 )
	elif d == 'S':  		
		if cabezal[1] < tamanio - 1:
			cabezal[1] += 1
		else:
			bum()
			exit( 0 )
	elif d == 'N': 		
		if cabezal[1] > 0:
			cabezal[1] -= 1
		else:
			bum()
			exit( 0 )
	else:
		print('Error: Mover(d) se llama con parametros O (oeste), E (este), S (sur), N (norte)')
		exit( 0 )

#-------------------------------------------------------------

def Poner( color ):
	if color == 'R':
		universo[0][cabezal[0]][cabezal[1]] += 1
	elif color == 'V':	
		universo[1][cabezal[0]][cabezal[1]] += 1
	elif color == 'A':	
		universo[2][cabezal[0]][cabezal[1]] += 1
	elif color == 'N':	
		universo[3][cabezal[0]][cabezal[1]] += 1
	else:
		print('Error: Poner(c) se llama con parametros R (rojo), A (azul), V (verde), N (negro)')
		exit( 0 )	
		
	# if color in colores:
	# que universo se refencie por colores
 
 #-------------------------------------------------------------

def Sacar( color ):
	if color == 'R' and universo[0][cabezal[0]][cabezal[1]] > 0:
		universo[0][cabezal[0]][cabezal[1]] -= 1
	elif color == 'R' and universo[0][cabezal[0]][cabezal[1]] == 0: 
		bum()
		exit( 0 )
	elif color == 'V' and universo[1][cabezal[0]][cabezal[1]] > 0:
		universo[1][cabezal[0]][cabezal[1]] -= 1
	elif color == 'V' and universo[1][cabezal[0]][cabezal[1]] == 0: 
		bum()
		exit( 0 )		
	elif color == 'A' and universo[2][cabezal[0]][cabezal[1]] > 0:
		universo[2][cabezal[0]][cabezal[1]] -= 1
	elif color == 'A' and universo[2][cabezal[0]][cabezal[1]] == 0: 
		bum()
		exit( 0 )
	elif color == 'N' and universo[3][cabezal[0]][cabezal[1]] > 0:
		universo[3][cabezal[0]][cabezal[1]] -= 1
	elif color == 'N' and universo[3][cabezal[0]][cabezal[1]] == 0: 
		bum()
		exit( 0 )
	else:	
		print('Error: Sacar(c) se llama con parametros R (rojo), A (azul), V (verde), N (negro)')
		exit( 0 )	
 
#-------------------------------------------------------------
# Funciones para operar con el universo 
#-------------------------------------------------------------

def VaciarUniverso( ): 
	global universo
	universo = [[[ 0 for x in range(tamanio)] for y in range(tamanio) ] for z in range(cantColores) ]

#-------------------------------------------------------------

def CargarUniverso( i, j, cantidad, color ):
	if color == 'R':  
		universo[0][i][j] += cantidad
	elif color == 'V':
		universo[1][i][j] += cantidad
	elif color == 'A':
		universo[2][i][j] += cantidad
	elif color == 'N':
		universo[3][i][j] += cantidad		
	return 0

#-------------------------------------------------------------

def MoverCabezal(i,j):
	cabezal[0] = i
	cabezal[1] = j
	
#-------------------------------------------------------------

def UniversoAzaroso( n, m ):
	VaciarUniverso()
	for i in range(n):
		a = randint(0,cantColores-1)
		b = randint(0,tamanio-1)
		c = randint(0,tamanio-1)
		d = randint(0,m)
		universo[a][b][c]=d
	cabezal[0] = randint(0,tamanio-1)
	cabezal[1] = randint(0,tamanio-1)	
	
#-------------------------------------------------------------
#  Funciones de la salida gráfica		
#-------------------------------------------------------------

def crearCelda(x,y,t,u, r,v,a,n):
	c.create_rectangle( [x, y, x+2*t+3*u, y+2*t+3*u], fill=color[5] )			 
	if a != 0:
		c.create_oval( [x+u, y+u, x+t+u, y+t+u], fill=color[0] )	
		c.create_text( x+t/2+u, y+t/2+u, font=("Purisa",fontBolas), fill=color[4], text=str(a) ) 
	if n != 0:
		c.create_oval( [x+t+2*u, y+u, x+2*t+2*u, y+t+u], fill=color[6] )	
		c.create_text( x+t+t/2+2*u, y+t/2+u, font=("Purisa",fontBolas), fill=color[4], text=str(n) )
	if r != 0:
		c.create_oval( [x+u, y+t+2*u, x+t+u, y+2*t+2*u], fill=color[1] )
		c.create_text( x+t/2+u, y+t+t/2+2*u, font=("Purisa",fontBolas), text=str(r) )
	if v != 0:
		c.create_oval( [x+t+2*u, y+t+2*u, x+2*t+2*u, y+2*t+2*u], fill=color[2] )	 
		c.create_text( x+t+t/2+2*u, y+t+t/2+2*u, font=("Purisa",fontBolas), text=str(v) )
		
#-------------------------------------------------------------

def crearFila( j, n, hoff, uni ):
	for i in range(n): 
		crearCelda(hoff+offset+2*(i+1)*(ladoCelda+2*entreCeldas),offset+2*(j+1)*(ladoCelda+2*entreCeldas),ladoCelda,entreCeldas,uni[0][i][j],uni[1][i][j],uni[2][i][j],uni[3][i][j])		
		
#----------------------------------------------------------- 

def mostrarCabezal( hoff, cab ):
	c.create_rectangle( [hoff+offset+2*(cab[0]+1)*(ladoCelda+2*entreCeldas), offset+2*(cab[1]+1)*(ladoCelda+2*entreCeldas), hoff+offset+2*(cab[0]+1)*(ladoCelda+2*entreCeldas)+2*ladoCelda+3*entreCeldas, offset+2*(cab[1]+1)*(ladoCelda+2*entreCeldas)+2*ladoCelda+3*entreCeldas], outline=color[1], width=5 )
 
#----------------------------------------------------------- 

def mostrarNumeros( n, hoff ):
	for i in range(n):
		c.create_text( hoff+ep1+offset*2,offset*2+2*(i+1)*(ladoCelda+2*entreCeldas)+ep3, font=("Purisa",fontLineas), text=str(i) )   #vertical izq
		c.create_text( hoff+offset*2+2*(n+1)*(ladoCelda+2*entreCeldas),offset*2+2*(i+1)*(ladoCelda+2*entreCeldas)+ep3, font=("Purisa",fontLineas), text=str(i) ) #vertical der 
		c.create_text( hoff+ep3+offset*2+2*(i+1)*(ladoCelda+2*entreCeldas), ep1+ep4+offset*2, font=("Purisa",fontLineas), text=str(i) ) #horizontal arriba
		c.create_text( hoff+ep3+offset*2+2*(i+1)*(ladoCelda+2*entreCeldas), offset*2+2*(n+1)*(ladoCelda+2*entreCeldas), font=("Purisa",fontLineas), text=str(i) ) #horizontal abajo

#-------------------------------------------------------------
  
def mostrarUniverso( n ):
	c.create_text( offset+ep0+(ladoCelda+2*entreCeldas)*n, 2*offset-ep2, font=("Purisa",fontTitulos), text="Entrada" )
	mostrarNumeros( n, 0 )
	for i in range( n ):
		crearFila( i, n, 0, univInic )
	mostrarCabezal( 0, cabInic )	
	c.create_text( offset+ep0+mp+(ladoCelda+2*entreCeldas)*n, 2*offset-ep2, font=("Purisa",fontTitulos), text="Salida" )
	mostrarNumeros( n, mp )
	for i in range( n ):
		crearFila( i, n, mp, universo )
	mostrarCabezal( mp, cabezal )		

	root.mainloop()
	
#-------------------------------------------------------------
  
def bum():
	c.create_text( 500, 300, font=("Purisa",fontBoom), text="Buuum!!!" )

	root.mainloop()	

#-------------------------------------------------------------
#  Segunda generación de primitivas  
#-------------------------------------------------------------

def Repetir( f, n ):
	for i in range(n):
		f()

#-------------------------------------------------------------

def RepetirCP( f, p, n ):
	for i in range(n):
		f(p)

#-------------------------------------------------------------

def PuedeMover( d ):
	global cabezal
	if d == 'E':
		if cabezal[0] < tamanio - 1:
			pm = True
		else:
			pm = False
	elif d == 'O': 		
		if cabezal[0] > 0:
			pm = True
		else:
			pm = False
	elif d == 'S':  		
		if cabezal[1] < tamanio - 1:
			pm = True
		else:
			pm = False
	elif d == 'N': 		
		if cabezal[1] > 0:
			pm = True
		else:
			pm = False
	else:
		print('Error: Mover(d) se llama con parametros O (oeste), E (este), S (sur), N (norte)')
		exit( 0 )
	return pm	
 	
def CantBolitas( color ): 
	if color == 'R':
		cb = universo[0][cabezal[0]][cabezal[1]]
	elif color == 'V':	
		cb = universo[1][cabezal[0]][cabezal[1]]
	elif color == 'A':	
		cb = universo[2][cabezal[0]][cabezal[1]]
	elif color == 'N':	
		cb = universo[3][cabezal[0]][cabezal[1]]
	else:
		print('Error: Poner(c) se llama con parametros R (rojo), A (azul), V (verde), N (negro)')
		exit( 0 )	
	return cb	
	
#-------------------------------------------------------------
	
def Fin():
	mostrarUniverso( 10 )
	return 0	
		
#-------------------------------------------------------------
#----------------- Principal ---------------------------------		
#-------------------------------------------------------------
			
#inicUniv()

# VaciarUniverso()
# UniversoAzaroso(200,9)	
# mostrarUniverso(10)
		

