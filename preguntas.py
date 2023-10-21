"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
file_path = "data.csv"



def read_data(path):
    with open(file_path, "r") as file:
        data = file.readlines()

    data = [line.replace("\n", "") for line in data]
    data = [line.split("\t") for line in data]

    return data


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    data = read_data(file_path)

    lista = []
    
    for i in range(0,len(data)):
        numero = int(data[i][1])
        lista.append(numero)
    
    return sum(lista)


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    data = read_data(file_path)

    lista = []
    
    for i in range(0,len(data)):
        letra = data[i][0]
        lista.append(letra)
    
    cnt = Counter(lista)
    
    keys = list(cnt.keys())
    keys.sort()
    
    lista_2 = []
    
    for j in keys:
        query = (j, cnt[j])
        lista_2.append(query) 
    
    return lista_2


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    data = read_data(file_path)

    list_a, list_b, list_c, list_d, list_e = [[],[],[],[],[]]
    
    lista = [list_a, list_b, list_c, list_d, list_e]
    
    text = "ABCDE"
    
    lista_2 = []
    
    for i in range(0,len(data)):
        if data[i][0] == "A":
            a = int(data[i][1])
            list_a.append(a)
            
        elif data[i][0] == "B":
            b = int(data[i][1])
            list_b.append(b)
            
        elif data[i][0] == "C":
            c = int(data[i][1])
            list_c.append(c)
            
        elif data[i][0] == "D":
            d = int(data[i][1])
            list_d.append(d)
            
        else:
            e = int(data[i][1])
            list_e.append(e)
    
    for i in range(0,len(lista)):
        tupla = (text[i], sum(lista[i]))
        lista_2.append(tupla)
    
    return lista_2


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    data = read_data(file_path)
    dict_count = {}
    for line in data:
        month = line[2].split("-")[1]
        dict_count[month] = dict_count.get(month, 0) + 1
    list_count = sorted([(k, v) for k, v in dict_count.items()])
    
    return list_count


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    data = read_data(file_path)

    list_a, list_b, list_c, list_d, list_e = [[],[],[],[],[]]
    
    lista = [list_a, list_b, list_c, list_d, list_e]
    
    text = "ABCDE"
    
    lista_2 = []
    
    for i in range(0,len(data)):
        if data[i][0] == "A":
            a = int(data[i][1])
            list_a.append(a)
            
        elif data[i][0] == "B":
            b = int(data[i][1])
            list_b.append(b)
            
        elif data[i][0] == "C":
            c = int(data[i][1])
            list_c.append(c)
            
        elif data[i][0] == "D":
            d = int(data[i][1])
            list_d.append(d)
            
        else:
            e = int(data[i][1])
            list_e.append(e)
    
    for i in range(0,len(lista)):
        tupla = (text[i], max(lista[i]), min(lista[i]))
        lista_2.append(tupla)
    
    return lista_2


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    data = read_data(file_path)

    aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj = [],[],[],[],[],[],[],[],[],[]
      
    response = []
    
    let = []
    num = []
        
    for i in range(0, len(data)):
        both = data[i][4].split(",")
        
        l = [j.split(":",1)[0] for j in both]
        let.append(l)
        
        m = [k.split(":",1)[1] for k in both]
        num.append(m)
    
    for i in range(0,len(num)):
       for j in range(0,len(num[i])):
           num[i][j] = int(num[i][j]) 
    
    for i in range(0,len(let)):
        for j in range(0,len(let[i])):
            if let[i][j] == "aaa":
                a = int(num[i][j])
                aaa.append(a)
                
            if let[i][j] == "bbb":
                b = int(num[i][j])
                bbb.append(b)
                
            if let[i][j] == "ccc":
                c = int(num[i][j])
                ccc.append(c)
                
            if let[i][j] == "ddd":
                d = int(num[i][j])
                ddd.append(d)
                
            if let[i][j] == "eee":
                e = int(num[i][j])
                eee.append(e)
                
            if let[i][j] == "fff":
                f = int(num[i][j])
                fff.append(f)
                
            if let[i][j] == "ggg":
                g = int(num[i][j])
                ggg.append(g)
                
            if let[i][j] == "hhh":
                h = int(num[i][j])
                hhh.append(h)
                
            if let[i][j] == "iii":
                ii = int(num[i][j])
                iii.append(ii)
                
            if let[i][j] == "jjj":
                j = int(num[i][j])
                jjj.append(j)
                
    lista = [aaa,bbb,ccc,ddd,eee,fff,ggg,hhh,iii,jjj]

    names = ["aaa","bbb","ccc","ddd","eee","fff","ggg","hhh","iii","jjj"]
                                     
    for i in range(0,len(names)):
        tup = (names[i], min(lista[i]), max(lista[i]))
        response.append(tup)

    return response


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    data = read_data(file_path)

    lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9 =[[],[],[],[],[],[],[],[],[],[]]
    
    lista = [lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9]
    
    lista_2 = []
    
    text = "0123456789"
    
    for i in range(0, len(data)):
        if data[i][1] == "0":
            zero = data[i][0]
            lista0.append(zero)
        
        elif data[i][1] == "1":
            one = data[i][0]
            lista1.append(one)
            
        elif data[i][1] == "2":
            two = data[i][0]
            lista2.append(two)
            
        elif data[i][1] == "3":
            three = data[i][0]
            lista3.append(three)
            
        elif data[i][1] == "4":
            four = data[i][0]
            lista4.append(four)
            
        elif data[i][1] == "5":
            five = data[i][0]
            lista5.append(five)
            
        elif data[i][1] == "6":
            six = data[i][0]
            lista6.append(six)
            
        elif data[i][1] == "7":
            seven = data[i][0]
            lista7.append(seven)
            
        elif data[i][1] == "8":
            eight = data[i][0]
            lista8.append(eight)
            
        else:
            nine = data[i][0]
            lista9.append(nine)
            
    for i in range(0, len(text)):
        tupla = (i, lista[i])
        lista_2.append(tupla)
    
    return lista_2


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    data = read_data(file_path)

    lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9 =[[],[],[],[],[],[],[],[],[],[]]
    
    lista = [lista0, lista1, lista2, lista3, lista4, lista5, lista6, lista7, lista8, lista9]
    
    lista_2 = []
    
    text = "0123456789"
    
    for i in range(0, len(data)):
        if data[i][1] == "0":
            zero = data[i][0]
            lista0.append(zero)
        
        elif data[i][1] == "1":
            one = data[i][0]
            lista1.append(one)
            
        elif data[i][1] == "2":
            two = data[i][0]
            lista2.append(two)
            
        elif data[i][1] == "3":
            three = data[i][0]
            lista3.append(three)
            
        elif data[i][1] == "4":
            four = data[i][0]
            lista4.append(four)
            
        elif data[i][1] == "5":
            five = data[i][0]
            lista5.append(five)
            
        elif data[i][1] == "6":
            six = data[i][0]
            lista6.append(six)
            
        elif data[i][1] == "7":
            seven = data[i][0]
            lista7.append(seven)
            
        elif data[i][1] == "8":
            eight = data[i][0]
            lista8.append(eight)
            
        else:
            nine = data[i][0]
            lista9.append(nine)
    
    for i in range(0,len(lista)):
        lista[i] = sorted(list(set(lista[i])))
        
    
    for i in range(0, len(text)):
        tupla = (i, lista[i])
        lista_2.append(tupla)
    
    return lista_2


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
   data = read_data(file_path)
        
    aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj = [], [], [], [], [], [], [], [], [], []
    
    lista = [aaa, bbb, ccc, ddd, eee, fff, ggg, hhh, iii, jjj]
    
    total = []
    
    keys = ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj"]
    
    for i in range(0, len(data)):
        if "aaa" in data[i][4]:
            a = 1
            aaa.append(a)
    
    for i in range(0, len(data)):
        if "bbb" in data[i][4]:
            b = 1
            bbb.append(b)
            
    for i in range(0, len(data)):
        if "ccc" in data[i][4]:
            c = 1
            ccc.append(c)
            
    for i in range(0, len(data)):
        if "ddd" in data[i][4]:
            d = 1
            ddd.append(d)
    
    for i in range(0, len(data)):
        if "eee" in data[i][4]:
            e = 1
            eee.append(e)

    for i in range(0, len(data)):
        if "fff" in data[i][4]:
            f = 1
            fff.append(f)

    for i in range(0, len(data)):
        if "ggg" in data[i][4]:
            g = 1
            ggg.append(g)

    for i in range(0, len(data)):
        if "hhh" in data[i][4]:
            h = 1
            hhh.append(h)

    for i in range(0, len(data)):
        if "iii" in data[i][4]:
            i = 1
            iii.append(i)

    for i in range(0, len(data)):
        if "jjj" in data[i][4]:
            j = 1
            jjj.append(j)            
          
    for i in range(0, len(lista)):
        t = len(lista[i])
        total.append(t)
    
    dic = {keys[i]: total[i] for i in range(len(keys))}
    
    return dic


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    data = read_data(file_path)

    elem4 = []
    elem5 = []
    
    final = []
    
    for i in range(0, len(data)):
        number = data[i][3].count(",") + 1
        elem4.append(number)
    
    for i in range(0, len(data)):
        number2 = data[i][4].count(",") + 1
        elem5.append(number2)
            
    for i in range(0, len(data)):
        f = (data[i][0], elem4[i], elem5[i])
        final.append(f)
    
    return final


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    data = read_data(file_path)
    
    a,b,c,d,e,f,g = [],[],[],[],[],[],[]
    
    general = [a,b,c,d,e,f,g]
    
    name = "abcdefg"
    
    for i in range(0,len(data)):
        if "a" in data[i][3]:
            numa = int(data[i][1])
            a.append(numa)
        
        if "b" in data[i][3]:
            numb = int(data[i][1])
            b.append(numb)
            
        if "c" in data[i][3]:
            numc = int(data[i][1])
            c.append(numc)
            
        if "d" in data[i][3]:
            numd = int(data[i][1])
            d.append(numd)
            
        if "e" in data[i][3]:
            nume = int(data[i][1])
            e.append(nume)
            
        if "f" in data[i][3]:
            numf = int(data[i][1])
            f.append(numf)
            
        if "g" in data[i][3]:
            numg = int(data[i][1])
            g.append(numg)
            
    dic = {name[i]: sum(general[i]) for i in range(len(name))}
    
    return dic


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
   data = read_data(file_path)

    dict_count = {}

    for line in data:
        letter = line[0]
        dict_ = {
            string.split(":")[0]: string.split(":")[1] for string in line[4].split(",")
        }
        sum_vals = sum([int(v) for v in dict_.values()])

        dict_count[letter] = dict_count.get(letter, 0) + sum_vals
    dict_count = {k: v for k, v in sorted(dict_count.items(), key=lambda item: item[0])}
    
    return dict_count
