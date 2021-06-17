#!/usr/bin/env python
# coding: utf-8

# In[27]:


def agregar_lista(lista):
    for i in lista:
        if i in frecuencia:
            frecuencia[i] += 1
        else:
            frecuencia[i] = 1

def leerArchivo():
    lista = []
    archi = open('archivo.txt','r')
    linea = archi.read()
    while linea != "":
        lista = linea.split()
        linea = archi.readline()
    archi.close()
    agregar_lista(lista)
    
frecuencia = {}
leerArchivo()

for j in frecuencia:
    print("(" + j + ", " + str(frecuencia[p]) + ")")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




