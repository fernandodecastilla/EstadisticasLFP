# Importamos librerías de código necesarias para la práctica
from selenium import webdriver # Permite ejecutar eventos click sobre elementos html
from bs4 import BeautifulSoup
import csv, time

# Constantes
url_raiz = 'http://www.laliga.es/estadisticas/jugadores/'
id_enlace = 'DataTables_Table_0_next' # ID del elemento html sobre el que hacer click
clase_fin_enlace = 'paginate_button next disabled' # Clase que deshabilita el link del elemento anterior

# Funciones
def ConstruirURL(totales, jornada, competicion, tipo, posicion):
    totales = 'totales=' + totales
    if(jornada != ''):
        jornada = '&jornada=J-' + jornada
    competicion = '&competicion=' + competicion
    tipo = '&tipo=' + tipo
    if(posicion != ''):
        posicion = '&posicion=' + posicion
    return url_raiz + totales + jornada + competicion + tipo + posicion

def NavegarURL(url):
    time.sleep(5) # No necesario si sólo se descarga un fichero de datos por ejecución
    driver = webdriver.Chrome()
    driver.set_window_position(-10000,0) # Ocultar ventana del navegador web
    driver.get(url)
    time.sleep(10) # Necesario para permitir al servidor web obtener las consultas solicitadas
    soup = BeautifulSoup(driver.page_source, 'lxml') # No ejecutamos prettify y mejoramos el coste temporal
    return driver, soup

def PulsarBoton(driver, soup, link_id):   
    driver.find_element_by_id(link_id).click() # Evento click
    soup = BeautifulSoup(driver.page_source, 'lxml') # Traspaso del código html a BeautifulSoup
    return driver, soup

def ObtenerCabeceraTabla(soup, datos):
    cabeceras = soup.find(id='DataTables_Table_0').find('thead').find('tr').find_all('th')
    for i in range(len(cabeceras)):
        cabeceras[i] = cabeceras[i].text
    datos.append(cabeceras)
    return datos

def ObtenerDatosTabla(soup, datos):
    filas = soup.find(id='DataTables_Table_0').find('tbody').find_all('tr')
    for fila in filas:
        valores = fila.find_all('td')
        for i in range(len(valores)):
            valores[i] = valores[i].text
        datos.append(valores)
    return datos

def QuedanTablas(soup): # La condición es cierta mientras no exista la clase en cuestión en el código html
    return soup.find(attrs={'class':clase_fin_enlace}) is None

def ExportarCSV(datos, nombreFichero):
    salida = open(nombreFichero, 'w', newline='', encoding='utf-8')
    writer = csv.writer(salida, delimiter=';') # Tomamos ';' como delimitador para evitar confusión con los valores decimales (con comas)
    for registro in datos:
        writer.writerow(registro)
    salida.close()

def EjecutarScraping(nombreFichero='futbolistasLFP.csv', totales='totales', jornada='', competicion='laliga-santander', tipo='clasicas', posicion=''):
    url_to_scrape = ConstruirURL(totales, jornada, competicion, tipo, posicion)
    driver, soup = NavegarURL(url_to_scrape)
    datos = []
    datos = ObtenerCabeceraTabla(soup, datos)
    datos = ObtenerDatosTabla(soup, datos)
    
    while(QuedanTablas(soup)):
        driver, soup = PulsarBoton(driver, soup, id_enlace)
        datos = ObtenerDatosTabla(soup, datos)
    driver.close()
    ExportarCSV(datos, nombreFichero)



'''
SIGNIFICADO DE CADA PARÁMETRO:
    nombreFichero:
        Nombre que tendrá el fichero CSV a generar.
        Por defecto, 'futbolistasLFP.csv'
    totales:
        Por defecto, se seleccionan estadísticas acumuladas hasta una jornada,
        o bien, se especifica una jornada en concreto.
    jornada:
        Seleccionar jornada.
        Por defecto, se toma la última jornada hasta la fecha (a 9 de abril, el máximo es '31').
    competicion:
        Por defecto, se selecciona la primera división,
        o bien, se especifica la segunda división.
    tipo:
        Por defecto, se obtienen estadísticas clásicas,
        o bien, se selecciona entre diferentes tipos de estadísticas a obtener.
    posición:
        Por defecto, se muestran todos los futbolistas,
        o bien, se filtra por demarcación de los jugadores.

VALORES POSIBLES DE CADA PARÁMETRO:
    totales = 'totales' | 'x-partido'
    jornada = '' | '1' | ... | '38'                         
    competicion = 'laliga-santander' | 'laliga-123'
    tipo = 'clasicas' | 'defensivas' |'ofensivas' | 'disciplina' | 'eficiencia' | 'portero'
    posicion = '' | 'porteros' | 'defensas' | 'medios' | 'delanteros'
'''
# CÓDIGO PRINCIPAL A EJECUTAR

# Ejemplo 1: Estadísticas clásicas de todos los jugadores de primera división acumuladas hasta la última jornada disputada
EjecutarScraping()

# Ejemplo 2: Estadísticas clásicas de los delanteros de primera división acumuladas hasta la última jornada disputada
EjecutarScraping(nombreFichero='delanterosGeneral.csv',
                 posicion='delanteros')

# Ejemplo 3: Estadísticas sobre eficiencia de los delanteros de primera división acumuladas hasta la última jornada disputada
EjecutarScraping(nombreFichero='delanterosEficiencia.csv',
                 tipo='eficiencia',
                 posicion='delanteros')









# Creamos una tupla con el nombre de cada atributo que conformará el conjunto de datos
ATRIBUTOS = ('Nombre', 'Equipo', 'Minutos', 'Jugados', 'Entero', 'Titular', 
             'Sustituido', 'Amarillas', 'Rojas', 'DobleAmarilla', 'Goles', 
             'GolesPenalti', 'GolesPP', 'GolesEnc')