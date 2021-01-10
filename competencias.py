class Competencia:

    def __init__(self, nombre, continente, ranking):
        self.nombre = nombre
        self.continente = continente
        self.ranking = ranking


def to_string(competencia):
    list = ' '
    list += '{:<22}  '.format(str(competencia.nombre))
    list += '{:<20}  '.format(str(competencia.continente))
    list += '{:<20}  '.format(str(competencia.ranking))
    return list


class Rondas:
    def __init__(self, equipo1, punto1, equipo2, punto2):
        self.equipo1 = equipo1
        self.punto1 = punto1
        self.equipo2 = equipo2
        self.punto2 = punto2


def to_string2(rondas):
    list = ' '
    list += '{:<30}  '.format('Equipo 1: ' + str(rondas.equipo1))
    list += '{:<15}  '.format('Puntos 1: ' + str(rondas.punto1))
    list += '{:<5}  '.format('VS ')
    list += '{:<30}  '.format('Equipo 2: ' + str(rondas.equipo2))
    list += '{:<35}  '.format('Puntos 2: ' + str(rondas.punto2))
    return list


def get_titulos():
    renglon = '\n'
    renglon += '{:<20}'.format("Nombre")
    renglon += ' '
    renglon += '{:<20}'.format("Continente")
    renglon += '  '
    renglon += '{:<20}'.format("Ranking")

    return renglon


def get_podio():
    renglon = '\n'
    renglon += '{:>20}'.format("Nombre")
    renglon += ' '
    renglon += '{:>20}'.format("Continente")
    renglon += '  '
    renglon += '{:>20}'.format("Ranking")

    return renglon
