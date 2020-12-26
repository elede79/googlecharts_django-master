from django.shortcuts import render
import numpy as np

import matplotlib as mpl
from scipy.signal import find_peaks
#ranrange is imported to create random numbers
from random import randrange

import cv2


#json is imported so that Python objects can be converted to JSON strings using 
# json.dumps
import json

def obtiene_vector_serie(largo_dest, pos_y, vector_origxy, vector_dest):
    #Largo_dest: largo del vector destino
    #pos_y: posicion donde se insetara el valor en el destino
    #se instertara en 0 y en pos_y, el resto null
    vector_dest[0] = vector_origxy[0]
    
    for i in range(1,largo_dest+1):
        
        if i == pos_y: 
            vector_dest[i] = vector_origxy[1]
        else: 
            vector_dest[i] = -1#'null'
  
    return vector_dest
  

def obtiene_vector(ini_null, fin_null, indice_v, vector_origx, vector_origy, vector_dest):
    #print(len(vector_origx))
    j=0
    while j <= len(vector_origx): 
  
        if (j == ini_null):
            vector_dest[j] = vector_origy[indice_v]
        else: 
            vector_dest[j] = -1#'null'

        vector_dest[0] = vector_origx[indice_v]
        j +=1   

    return vector_dest

def creaMatriz_curva(n,listapuntos):
    '''
    Esta función crea una matríz  con n filas y 2 columnas.
    @param n : Número de filas.
    @param listapuntos : Los puntos de y que representan la curva
    devo agregar el valor x que es un incremental de  0 a largo de la lista
    
    @return: devuelve una matriz n por m
    @rtype: matriz (lista de listas)
    ''' 
    matriz = []
    for i in range(n):
        #a = [0]*m
        a = [i,listapuntos[i]]
        matriz.append(a)
    return matriz


#no la uso pero la dejo porque parece importante tenerla
def creaMatriz(n,m):
    '''
    Esta función crea una matríz vacía con n filas y n columnas.
    @param n : Número de filas.
    @param m : Número de columnas
    @type n: int
    @type m: int
    @return: devuelve una matriz n por m
    @rtype: matriz (lista de listas)
    '''
    matriz = []
    for i in range(n):
        a = [0]*m
        matriz.append(a)
    return matriz


def home(request):
    """
    Function responsible for rendering the homepage
    """

    #h_var : The title for horizontal axis
    h_var = 'X'

    #v_var : The title for horizontal axis
    v_var = 'Y'

    #data : A list of list which will ultimated be used 
    # to populate the Google chart.
    data = [[h_var,v_var]]
    """
    An example of how the data object looks like in the end: 
        [
          ['Age', 'Weight'],
          [ 8,      12],
          [ 4,      5.5],
          [ 11,     14],
          [ 4,      5],
          [ 3,      3.5],
          [ 6.5,    7]
        ]

    The first list will consists of the title of horizontal and vertical axis,
    and the subsequent list will contain coordinates of the points to be plotted on
    the google chart
    """

    #The below for loop is responsible for appending list of two random values  
    # to data object
    for i in range(0,11):
        data.append([randrange(101),randrange(101)])

    #h_var_JSON : JSON string corresponding to  h_var
    #json.dumps converts Python objects to JSON strings
    h_var_JSON = json.dumps(h_var)

    #v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = json.dumps(v_var)

    #modified_data : JSON string corresponding to  data
    modified_data = json.dumps(data)

    #Finally all JSON strings are supplied to the charts.html using the 
    # dictiory shown below so that they can be displayed on the home screen
    return render(request,"charts.html",{'values':modified_data,\
        'h_title':h_var_JSON,'v_title':v_var_JSON})


def home_line(request):
    """
    Function responsible for rendering the homepage
    """
    #print('prueba matriz')
    #cm=creaMatriz(2,6)
    #print(cm)
    
    #abrir la imagen
    #img = cv2.imread("Tira_1.png")

    #esta lista representa la curva del grafico de la imagem ideal
    #voy a intentar obtener los minimos de una funcion con scipy.signal
    a3 =[12,  13,  13,  14,  14,  16,  18,  24,  35,  56,  90, 129, 163,
       183, 190, 188, 177, 161, 136, 109,  81,  56,  38,  25,  19,  17,
        17,  20,  24,  29,  34,  38,  40,  40,  36,  32,  27,  24,  22,
        21,  21,  22,  23,  24,  26,  28,  30,  33,  39,  48,  59,  68,
        74,  77,  76,  71,  63,  55,  46,  40,  35,  32,  30,  29,  29,
        30,  33,  38,  47,  60,  73,  79,  79,  70,  59,  47,  39,  35,
        32,  31,  32,  34,  37,  41,  45,  46,  42,  37,  32,  30,  29,
        28,  28,  27,  27,  26,  26,  27,  28,  29,  31,  32,  33,  34,
        35,  37,  38,  40,  41,  42,  44,  45,  47,  50,  53,  55,  57,
        58,  57,  55,  51,  48,  44,  41,  38,  36,  33,  31,  29,  27,
        26,  23,  21,  19,  17,  16,  16,  15,  15,  14,  13,  13,  13]

    #prurbas
    curva=creaMatriz_curva(len(a3),a3)
    #print(curva)

    #a = np.array([2,3,4,3,2])
    x=a3
    xinv = np.array(x) *-1
    print('xinvert: ',xinv)
    xinv = list(map(int, xinv )) #  a3 *(-1)
    print('xinvert: ',xinv)
    #x=xinv
   # print('xinvert_1: ',xinv_1)
    peaks_nin_x, _a = find_peaks(xinv)
    #peaks, _ = find_peaks(x, height=0)
    p1=peaks_nin_x[0]
    p2=peaks_nin_x[1]
    peaks_nin_y = [x[p1], x[p2], x[peaks_nin_x[2]], x[peaks_nin_x[3]], x[peaks_nin_x[4]] ]
    #peaks_nin_x
    print('peaks_nin_x:', peaks_nin_x)
    #print('peaks_nin_y:', _peaks_nin_y)
    print('picos_min_y;', peaks_nin_y)

    peaks, _ = find_peaks(x, height=0)
    print('picos_x:', peaks)
    #print(peaks)
    print('picos_y;',_['peak_heights'])
    #print(_['peak_heights'])
    print('tipo peaks: ', type(peaks))
    #print(len(x))
      
    #h_var : The title for horizontal axis
    h_var = 'X'

    #v_var : The title for horizontal axis
    v_var = 'Y'

    #data : A list of list which will ultimated be used 
    # to populate the Google chart.
    #data = [[h_var,v_var]]
    data =[[0,0,0,0,0,0]]
    #data = [['a','b','c','d','e','f']] #[[0,0,0,0,0,0]]
    #print('tipo data: ', type(data))
    #The bel#ow for loop is responsible for appending list of two random values  
    # to data object
   
    #Aqui armo el vector de minimos de la grafica para pasar a la vista
    data_minimos =[[0,0,0,0,0,0]]
    #minimos_reales_x = peaks
    #minimos_reales_y = _['peak_heights']
    '''
    prueba voy a reemplazar los maximos por los minimos
    '''
    minimos_reales_x = peaks_nin_x
    minimos_reales_y = peaks_nin_y

    #Convierte en una lista de int lo que hay en minimos_reales_x
    #results = list(map(int, results)) ejemplo
    minimos_reales_x = list(map(int, minimos_reales_x)) 
    minimos_reales_y = list(map(int, minimos_reales_y))
    
    
    print('minrealx: ', minimos_reales_x)
    print('minrealy: ', minimos_reales_y)
    min1=[0,0,0,0,0,0]
    min2=[0,0,0,0,0,0]
    min3= [0]*6
    min4= [0]*6
    min5= [0]*6
    print('llamada a obt_vect')
    obtiene_vector(2,2,0,minimos_reales_x,minimos_reales_y,min1 )    
    print('min1 ',min1)
    data_minimos.extend([min1[0:6]])    
       
    obtiene_vector(3,3,1,minimos_reales_x,minimos_reales_y,min2 )   
    print('min2 ',min2)
    data_minimos.extend([min2[0:6]])
    
    obtiene_vector(4,4,2,minimos_reales_x,minimos_reales_y,min3 )   
    print('min3 ',min3)
    data_minimos.extend([min3[0:6]])

    obtiene_vector(5,5,3,minimos_reales_x,minimos_reales_y,min4 )   
    print('min4 ',min4)
    data_minimos.extend([min4[0:6]])
    #me faltas 3 posiciones mas en el vector estoy llegandoa 4 ahora  0 del inico y la del fin
    #obtiene_vector(6,6,4,minimos_reales_x,minimos_reales_y,min5 )   
    #print('min5 ',min5)
    
    print('data_ninimos: ',data_minimos)

    vmatriz1 = [0,0]

    curva_salida = [0,0,0,0,0,0] # es igual a hacer [0]*6
    for indice in range(1,len(a3)):
        vmatriz1 = curva[indice] 
        obtiene_vector_serie(5,1,vmatriz1,curva_salida)
        #print('curva salida: ',curva_salida)
        data.extend([curva_salida[0:6]])

    #print('final:')
    #print(data)    
      
    #h_var_JSON : JSON string corresponding to  h_var
    #json.dumps converts Python objects to JSON strings
    h_var_JSON = json.dumps(h_var)

    #v_var_JSON : JSON string corresponding to  v_var
    v_var_JSON = json.dumps(v_var)

    #modified_data : JSON string corresponding to  data
    modified_data = json.dumps(data)
    modified_data_minimos = json.dumps(data_minimos)

    #Finally all JSON strings are supplied to the charts.html using the 
    # dictiory shown below so that they can be displayed on the home screen
    return render(request,"charts_line.html",{'values':modified_data,\
        'values_min':modified_data_minimos,\
        'h_title':h_var_JSON,'v_title':v_var_JSON})