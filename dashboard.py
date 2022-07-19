# -*- coding: utf-8 -*-


######## Librerías ########
import streamlit as st
import pandas as pd
import numpy as np #Para utilizar las funciones de agregación, es necesario utilizar numpy
import matplotlib.pyplot as plt #Para realizar gráficas

######## Funciones ########
    
    
    
######## Página principal ########
st.write("Hola mundo en streamlit")

#Ejemplo 5 - Figura 5
fig5 = plt.figure()

# Configurar parámetros generales de las gráficas
plt.rcParams.update({'font.size': 10})
plt.rcParams["figure.figsize"] = (6, 4) #Tamaño de las figuras; si se necesita, puede declararse antes de cada figura

#Datos de la gráfica
a = 0
b = 2
points = 11
x = np.linspace(a,b,points)
f1 = x
f2 = x**2
f3 = np.exp(x)

#Se agregaron nombres a las series y color
plt.plot(x,f1, label = "x", lw=1, marker='*' ,color = "magenta") 
plt.plot(x,f2, label = "x^2", lw=1, marker='.', color = "red")
plt.plot(x,f3, label = "e^x", lw=0.5, linestyle="--" , marker='s', color = "#1BD3DA")

#Título de la gráfica
plt.title("Ejemplo de diferentes tipos de gráfica")

#Etiquetas de los ejes
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()

#Mostrar etiquetas de los datos
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, shadow=True, ncol=3)

st.pyplot(fig5)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)


map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

st.map(map_data)

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
    
