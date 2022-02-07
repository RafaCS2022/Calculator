from tkinter import *

root=Tk()
root.title('Calculadora')

# root.iconbitmap('calculadora.ico')
miframe=Frame(root)
miframe.pack()


##### CREAMOS LA VARIABLE PARA LA FUNCION

numero_pantalla=StringVar()

###### CREAMOS LA PANTALLA PARA LA CALCULADORA

pantalla=Entry(miframe,textvariable=numero_pantalla)

pantalla.grid(row=1,column=1,padx=10,pady=10,columnspan=4) ### columnspan para que ocupe todas las columnas
pantalla.config(background='black',fg='#00FF00',justify='right')

##### LA FUNCION PARA PULSAR BOTONES

def numero_pulsado(num):

    lista=[1,2,3,4,5,6,7,8,9]
    lista1=[str(i) for i in lista]

    if len(numero_pantalla.get()) == 1 and numero_pantalla.get() != '0':
        if num in lista1:
            numero_pantalla.set(numero_pantalla.get()+num)
        else:
            if  num =='c':
                #numero_pantalla.set((numero_pantalla.get())[:-1])
                numero_pantalla.set('0')
            elif num == 'ce' :
                numero_pantalla.set('0')

            elif num == '0':
                #if len(numero_pantalla.get()) == 1 and numero_pantalla.get() == '0':
                numero_pantalla.set(numero_pantalla.get() + num)
            elif num == '.':
                numero_pantalla.set(numero_pantalla.get() + num)
            elif num == '-':
                numero_pantalla.set(num + numero_pantalla.get())

    elif len(numero_pantalla.get()) == 1 and numero_pantalla.get() =='0':
        if num in lista1:
            numero_pantalla.set(num)
        elif num == '.':
            numero_pantalla.set(numero_pantalla.get() + num)
        else:
            numero_pantalla.set(numero_pantalla.get())

    else:
        if num in lista1 or num=='0':
            numero_pantalla.set(numero_pantalla.get() + num)
        elif num=='c':
            numero_pantalla.set((numero_pantalla.get())[:-1])
        elif num=='ce':
            numero_pantalla.set('0')
        elif num == '.':
            if (numero_pantalla.get()).count('.')==0:
                numero_pantalla.set(numero_pantalla.get() + num)
            elif (numero_pantalla.get()).count('.') > 0:
                numero_pantalla.set(numero_pantalla.get())
        elif num == '-':
            if (numero_pantalla.get()).count('-')==0:
                numero_pantalla.set( num + numero_pantalla.get())
            elif (numero_pantalla.get()).count('-') > 0:
                numero_pantalla.set((numero_pantalla.get())[1:])

####### FUNCION PARA LAS OPERACIONES##########


numero_resultado=[]


def operaciones(operacion):

    numero_resultado.append(numero_pantalla.get())
    numero_resultado.append(operacion)
    numero_pantalla.set('0')

def resultado(num):

    global numero_resultado
    resultado=str()
    numero_resultado.append(numero_pantalla.get())

    for i in numero_resultado:
        resultado= resultado + i
    numero_pantalla.set(eval(resultado))

    numero_resultado=[]

####### FILA1 BOTONES #####

boton7=Button(miframe,text='7',width=3,command=lambda:numero_pulsado('7'))
boton7.grid(row=2,column=1,sticky='w')
boton8=Button(miframe,text='8',width=3,command=lambda:numero_pulsado('8'))
boton8.grid(row=2,column=2,sticky='w')
boton9=Button(miframe,text='9',width=3,command=lambda:numero_pulsado('9'))
boton9.grid(row=2,column=3,sticky='w')
botondiv=Button(miframe,text='/',width=3,command=lambda:operaciones('/'))
botondiv.grid(row=2,column=4,sticky='w')

####### FILA2 BOTONES #####

boton4=Button(miframe,text='4',width=3,command=lambda:numero_pulsado('4'))
boton4.grid(row=3,column=1,sticky='w')
boton5=Button(miframe,text='5',width=3,command=lambda:numero_pulsado('5'))
boton5.grid(row=3,column=2,sticky='w')
boton6=Button(miframe,text='6',width=3,command=lambda:numero_pulsado('6'))
boton6.grid(row=3,column=3,sticky='w')
botonrest=Button(miframe,text='-',width=3,command=lambda:operaciones('-'))
botonrest.grid(row=3,column=4,sticky='w')

####### FILA3 BOTONES #####

boton1=Button(miframe,text='1',width=3,command=lambda:numero_pulsado('1'))
boton1.grid(row=4,column=1,sticky='w')
boton2=Button(miframe,text='2',width=3,command=lambda:numero_pulsado('2'))
boton2.grid(row=4,column=2,sticky='w')
boton3=Button(miframe,text='3',width=3,command=lambda:numero_pulsado('3'))
boton3.grid(row=4,column=3,sticky='w')
botonmas=Button(miframe,text='+',width=3,command=lambda:operaciones('+'))
botonmas.grid(row=4,column=4,sticky='w')

####### FILA3 BOTONES #####

botonmasm=Button(miframe,text='+/-',width=3,command=lambda:numero_pulsado('-'))
botonmasm.grid(row=5,column=1,sticky='w')
boton0=Button(miframe,text='0',width=3,command=lambda:numero_pulsado('0'))
boton0.grid(row=5,column=2,sticky='w')
botoncoma=Button(miframe,text='.',width=3,command=lambda:numero_pulsado('.'))
botoncoma.grid(row=5,column=3,sticky='w')
botonigual=Button(miframe,text='=',width=3,bg='yellow',command=lambda:resultado('='))
botonigual.grid(row=6,column=4,sticky='w')


########FILA 4 BOTONES ######
botonc=Button(miframe,text='DEL',width=3,bg='#3399FF',command=lambda:numero_pulsado('c'))
botonc.grid(row=6,column=1,sticky='w')

botonce=Button(miframe, text='CE',width=3,bg='#FF3300',command=lambda:numero_pulsado('ce'))
botonce.grid(row=6,column=2,sticky='w')

botonx=Button(miframe,text='x',width=3,command=lambda:operaciones('*'))
botonx.grid(row=5,column=4,sticky='w')


root.mainloop()