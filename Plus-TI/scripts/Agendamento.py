""""
    PLUS-TI TECNOLOGIA DA INFORMAÇÃO
    CSI_CARGO

    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from datetime import datetime
from glob import glob

from scripts.Log import *

'''
    TURNOS DO QUAL O ROBO INTERPRETA AS PASTA DE PONTO
    1º TURNO 06:00-07:59
    ADM      08:00-10:00
    2º TURNO 14:01-22:00
    3º TURNO 22:01-06:00
'''

PASTA_RAIZ = r'C:\robo-cartao-de-ponto'

def pegar_arq_relogio_horario():
    SCHEMA_PASTAS = {}

    dd = datetime.now().strftime('%Y-%m-%d')
    
    for x in range(6, 9): SCHEMA_PASTAS[str(x) if x > 10 else '0' + str(x)] = PASTA_RAIZ + '\\' + '1-turno-download' +'\\'+ dd + '\\*.txt' # 1 TURNO
    for x in range(8, 15): SCHEMA_PASTAS[str(x) if x > 10 else '0' + str(x)] = PASTA_RAIZ +'\\'+ 'adm-download' + '\\' + dd + '\\*.txt' # TURNO ADM
    for x in range(14, 23): SCHEMA_PASTAS[str(x)] = PASTA_RAIZ +'\\'+ '2-turno-download' + '\\' + dd + '\\*.txt' # 2 TURNO
    for x in range(22, 23): SCHEMA_PASTAS[str(x)] = PASTA_RAIZ +'\\'+ '3-turno-download' + '\\' + dd + '\\*.txt' # 3 TURNO
    for x in range(0, 6): SCHEMA_PASTAS['0' + str(x)] = PASTA_RAIZ +'\\'+ '3-turno-download' + '\\' + dd + '\\*.txt' # TURNO
    mainlog(f"PEGANDO OS ARQUIVOS DA PASTA {SCHEMA_PASTAS[str(datetime.now().strftime('%H'))]} ({dd})")
    return glob(SCHEMA_PASTAS[str(datetime.now().strftime('%H'))])



