from competencias import *
from validaciones import *
import random


# OPCION 1 -CARGA MANUAL
def cargar_datos_manual(n):
    v = []
    for i in range(n):
        nombre = input('Ingrese el  nombre del participante :')
        while linear_search(v, nombre):
            nombre = input('Ingrese el  nombre del participante :')
        continente = validar_entre(0, 5,
                                   'Ingrese el numero que corresponde a un continente 0: América, 1: Europa, 2:Asia, 3: África, 4: Oceanía :')
        ranking = validar_entre(1, 100, 'Ingrese el numero que ranking: ')
        v.append(Competencia(nombre, continente, ranking))
    return v


# OPCION 1 -CARGA AUTOMATICA
def carga_datos_automatica(n):
    v = []
    for i in range(n):
        part = 'Mujer Maravilla', 'Batman', 'Aquaman', 'Superman ', 'Flash', 'Cybor', 'Linterna Verde ', 'Shazam', 'Iron Man', \
               'Capitan America', 'Black Widow ', 'Thor', 'Hulk', 'Spiderman', 'Bruja Escarlata', 'Doctor Strange'
        nombre = random.choice(part)
        while linear_search(v, nombre):
            nombre = random.choice(part)
        continente = random.randint(0, 4)
        ranking = random.randint(1, 100)
        v.append(Competencia(nombre, continente, ranking))
    return v


def linear_search(v, nombre):
    for i in range(len(v)):
        if v[i].nombre == nombre:
            return True
    return False


def mostrar_datos(v):
    print(get_titulos())
    print("=" * 55)
    for i in range(len(v)):
        print(to_string(v[i]))
    print("=" * 55)


# ORDENARLO POR RANKING
def ordernar(v):
    n = len(v)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if v[i].ranking < v[j].ranking:
                v[i], v[j] = v[j], v[i]


# CONTADOR POR CONTINENTE
def contandor_continente(v):
    vec = [0] * 5
    for i in range(len(v)):
        indice = v[i].continente
        vec[indice] += 1
    return vec


def cantidad_promedio(vec):
    cant = len(vec)
    sumap1 = 0
    sumap2 = 0
    p = 0
    sumat = 0
    for i in range(cant):
        sumap1 += vec[i].punto1
        sumap2 += vec[i].punto2
        sumat = sumap1 + sumap2
    if cant != 0:
        p = sumat / (cant * 2)

    return p


def mostrar_contador(vec):
    for i in range(len(vec)):
        if vec[i] != 0:
            print('Continente', i, ': tiene ', vec[i], 'Participantes')


# OCTAVOS

def copiar_paticipantes(v):
    vec = []
    for i in v[0:8]:
        vec.append(i.nombre)
    return vec


def recorrer(v):
    vac = []
    for i in range(-1, (-len(v) + 7), -1):
        vac.append(v[i].nombre)
    return vac


def generar_fixture(vec, vac, n):
    a = vec
    b = vac
    vector = []
    for i in range(n):
        equipo1 = a[i]
        punto1 = random.randint(1, 10)
        equipo2 = b[i]
        punto2 = random.randint(1, 10)
        if punto2 == punto1:
            punto2 = random.randint(1, 10)
        vector.append(Rondas(equipo1, punto1, equipo2, punto2))
    return vector


def mostrar_todo2(vector):
    for i in range(len(vector)):
        print(to_string2(vector[i]))


# CUARTO
def generar_cuarta_semi_final(vector):
    vic = []
    for i in range(len(vector)):
        if vector[i].punto1 > vector[i].punto2:
            vic.append(vector[i].equipo1)
        else:
            vic.append(vector[i].equipo2)

    return vic


def copiar_paticipantes_cuarta(vic):
    vec = []
    for i in vic[0:4]:
        vec.append(i)
    return vec


def recorrer_participantes_cuarta(vic):
    vac = []
    for i in range(-1, (-len(vic) + 3), -1):
        vac.append(vic[i])
    return vac


# SEMI
def copiar_paticipantes_semi(vic):
    vec = []
    for i in vic[0:2]:
        vec.append(i)
    return vec


def recorrer_participantes_semi(vic):
    vac = []
    for i in range(-1, (-len(vic) + 1), -1):
        vac.append(vic[i])
    return vac


# FINAL Y TERCER PUESTO
def copiar_paticipantes_final(vic):
    vec = []
    for i in vic[0:1]:
        vec.append(i)
    return vec


def recorrer_participantes_final(vic):
    vac = []
    for i in range(-1, (-len(vic) + 0), -1):
        vac.append(vic[i])
    return vac


def generar_tercera(vector):
    vi = []
    for i in range(len(vector)):
        if vector[i].punto1 < vector[i].punto2:
            vi.append(vector[i].equipo1)
        else:
            vi.append(vector[i].equipo2)
    return vi


# PODIO
def resultado(vecto):
    for i in range(len(vecto)):
        if vecto[i].punto1 > vecto[i].punto2:
            ganador = vecto[i].equipo1
            segundo = vecto[i].equipo2
        else:
            ganador = vecto[i].equipo2
            segundo = vecto[i].equipo1
    return ganador, segundo


def resultado_tercera(vector):
    for i in range(len(vector)):
        if vector[i].punto1 > vector[i].punto2:
            tercero = vector[i].equipo1
        else:
            tercero = vector[i].equipo2

    return tercero


def buscar(v, ganador, segundo, tercero):
    nomp = noms = nomt = None
    for n in v:
        if n.nombre == ganador:
            nomp = n
        if n.nombre == segundo:
            noms = n
        if n.nombre == tercero:
            nomt = n
    return nomp, noms, nomt


def buscar3(v, ganador):
    res = -1
    for i in range(len(v)):
        if v[i].nombre == ganador:
            res = i
            break
    return res


def busqueda_y_modificacion(v, ganador):
    indice_donde_esta = buscar3(v, ganador)
    if indice_donde_esta != -1:
        v[indice_donde_esta].ranking = v[indice_donde_esta].ranking + 25


def busqueda_y_modificacion2(v, segundo):
    indice_donde_esta = buscar3(v, segundo)
    if indice_donde_esta != -1:
        v[indice_donde_esta].ranking = v[indice_donde_esta].ranking + 15


def busqueda_y_modificacion3(v, tercero):
    indice_donde_esta = buscar3(v, tercero)
    if indice_donde_esta != -1:
        v[indice_donde_esta].ranking = v[indice_donde_esta].ranking + 5


# MENU
def test():
    print('\t\t\t\t\t\t\t\t\t\tTRABAJO PRACTICO 3: Sistema de Gestión de una Competencia ')
    n = validacion()
    carga = validar_entre(1, 3, "--QUIERE CARGA MANUAL O AUTOMATICA(1.Manual - 2.Automatica)?: ")
    if carga == 1:
        v = cargar_datos_manual(n)
        ordernar(v)
        mostrar_datos(v)
        input('\nPresione ENTER para continuar')
        print()
        print('1-CANTIDAD DE PARTICIPANTES POR CONTINENTE(0: América, 1: Europa, 2:Asia, 3: África, 4: Oceanía):')
        print()
        vec = contandor_continente(v)
        mostrar_contador(vec)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA OCTAVAS
        print('FIXTURE DE OCTAVOS ')
        n = 8
        vec = copiar_paticipantes(v)
        vac = recorrer(v)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('2-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN OCTAVOS ES: ', p)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA CUARTAS
        print('FIXTURE DE CUARTAS ')
        n = 4
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_cuarta(vic)
        vac = recorrer_participantes_cuarta(vic)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('3-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN CUARTAS ES: ', p)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA SEMI
        print('FIXTURE DE SEMI ')
        n = 2
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_semi(vic)
        vac = recorrer_participantes_semi(vic)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('4-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN SEMI ES: ', p)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;35m ')
        # FIXTURE DE LA FINAL
        print('FIXTURE DE LA FINAL ')
        n = 1
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_final(vic)
        vac = recorrer_participantes_final(vic)
        vecto = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vecto)
        print('=' * 105)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;34m ')
        # FIXTURE DE LA TERCER PUESTO
        print('FIXTURE  POR EL TERCER PUESTO ')
        n = 1
        vi = generar_tercera(vector)
        vec = copiar_paticipantes_final(vi)
        vac = recorrer_participantes_final(vi)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;33m ')
        # PODIO
        print('PODIO DE GANADORES')
        ganador, segundo = resultado(vecto)
        tercero = resultado_tercera(vector)
        pri, se, ter = buscar(v, ganador, segundo, tercero)
        print(get_podio())
        print('=' * 105)
        print('GANADOR    ', to_string(pri))
        print('2do PUESTO ', to_string(se))
        print('3ro PUESTO ', to_string(ter))
        print('=' * 105)
        busqueda_y_modificacion(v, ganador)
        busqueda_y_modificacion2(v, segundo)
        busqueda_y_modificacion3(v, tercero)
        ordernar(v)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;32m ')
        print('TABLA FINAL DE LOS PARTICIPANTES')
        mostrar_datos(v)
        print(' \x1b[1;30m ')
        print('¡GRACIAS !')
        opcion = input('PRESIONE LA TECLA "1" PARA INFORMACION SOBRE LOS PROGRAMADORES)\n')
        if opcion == '1':
            print(
                '\nPrograma (T.P N° 3) diseñado por los Alumnos:  \nDel Castillo - LN.:53067-1k12 \nFlores - LN.:56731- 1k16 \nOlmedo- LN.:78429-  1k1')
            print('Cátedra de Algoritmos y Estructuras de Datos 2020 - UTN Córdoba')
            input()

    else:
        v = carga_datos_automatica(n)
        ordernar(v)
        mostrar_datos(v)
        input('\nPresione ENTER para continuar')
        print(' 1-CANTIDAD DE PARTICIPANTES POR CONTINENTE(0: América, 1: Europa, 2:Asia, 3: África, 4: Oceanía):')
        print()
        vec = contandor_continente(v)
        mostrar_contador(vec)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA OCTAVAS
        print('FIXTURE DE OCTAVOS ')
        n = 8
        vec = copiar_paticipantes(v)
        vac = recorrer(v)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('2-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN OCTAVOS ES: ', p)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA CUARTAS
        print('FIXTURE DE CUARTAS ')
        n = 4
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_cuarta(vic)
        vac = recorrer_participantes_cuarta(vic)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('3-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN CUARTAS ES: ', p)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA SEMI
        print('FIXTURE DE SEMI ')
        n = 2
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_semi(vic)
        vac = recorrer_participantes_semi(vic)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        p = cantidad_promedio(vector)
        print('4-EL PUNTAJE PROMEDIO POR PARTICIPANTE EN SEMI ES: ', p)
        input('\nPresione ENTER para continuar')
        # FIXTURE DE LA FINAL
        print(' \x1b[1;35m ')
        print('FIXTURE DE LA FINAL ')
        n = 1
        vic = generar_cuarta_semi_final(vector)
        vec = copiar_paticipantes_final(vic)
        vac = recorrer_participantes_final(vic)
        vecto = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vecto)
        print('=' * 105)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;34m ')
        # FIXTURE DE LA TERCER PUESTO
        print('FIXTURE  POR EL TERCER PUESTO ')
        n = 1
        vi = generar_tercera(vector)
        vec = copiar_paticipantes_final(vi)
        vac = recorrer_participantes_final(vi)
        vector = generar_fixture(vec, vac, n)
        print('=' * 105)
        mostrar_todo2(vector)
        print('=' * 105)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;33m ')
        # PODIO
        print('PODIO DE GANADORES')
        ganador, segundo = resultado(vecto)
        tercero = resultado_tercera(vector)
        pri, se, ter = buscar(v, ganador, segundo, tercero)
        print(get_podio())
        print('=' * 105)
        print('GANADOR    ', to_string(pri))
        print('2do PUESTO ', to_string(se))
        print('3ro PUESTO ', to_string(ter))
        print('=' * 105)
        busqueda_y_modificacion(v, ganador)
        busqueda_y_modificacion2(v, segundo)
        busqueda_y_modificacion3(v, tercero)
        ordernar(v)
        input('\nPresione ENTER para continuar')
        print(' \x1b[1;32m ')
        print('TABLA FINAL DE LOS PARTICIPANTES')
        mostrar_datos(v)
        print(' \x1b[1;30m ')
        print('¡GRACIAS !')
        opcion = input('PRESIONE LA TECLA "1" PARA INFORMACION SOBRE LOS PROGRAMADORES)\n')
        if opcion == '1':
            print(
                '\nPrograma (T.P N° 3) diseñado por los Alumnos:  \nDel Castillo - LN.:53067-1k12 \nFlores - LN.:56731- 1k16 \nOlmedo- LN.:78429-  1k1')
            print('Cátedra de Algoritmos y Estructuras de Datos 2020 - UTN Córdoba')
            input()


if __name__ == '__main__':
    test()
