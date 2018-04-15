# EstadisticasLFP

El fichero 'EstadisticasLFP.py' contiene una función parametrizable sobre la que realizar todas las consultas de datos. A continuación, se expone todo el detalle de uso de la misma:

def EjecutarScraping(nombreFichero='futbolistasLFP.csv', totales='totales', jornada='', competicion='laliga-santander', tipo='clasicas', posicion='')

SIGNIFICADO DE CADA PARÁMETRO:

nombreFichero: Nombre que tendrá el fichero CSV a generar. Por defecto, 'futbolistasLFP.csv'

totales: Por defecto, se seleccionan estadísticas acumuladas hasta una jornada, o bien, se especifica una jornada en concreto.

jornada: Seleccionar jornada. Por defecto, se toma la última jornada hasta la fecha (a 9 de abril, el máximo es '31').

competicion: Por defecto, se selecciona la primera división, o bien, se especifica la segunda división.

tipo: Por defecto, se obtienen estadísticas clásicas, o bien, se selecciona entre diferentes tipos de estadísticas a obtener.

posición: Por defecto, se muestran todos los futbolistas, o bien, se filtra por demarcación de los jugadores.


VALORES POSIBLES DE CADA PARÁMETRO:

totales = 'totales' | 'x-partido'

jornada = '' | '1' | ... | '38'

competicion = 'laliga-santander' | 'laliga-123'

tipo = 'clasicas' | 'defensivas' |'ofensivas' | 'disciplina' | 'eficiencia' | 'portero'

posicion = '' | 'porteros' | 'defensas' | 'medios' | 'delanteros'
