""""
    PLUS-TI TECNOLOGIA DA INFORMAÇÃO
    CSI_CARGO

    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from datetime import datetime
import pyautogui as acoes
from os import walk

acoes.FAILSAFE = False

from scripts.Log import log
from scripts.RoboBase import *
from scripts.Config import Config
from scripts.VerTela import VerTela
from scripts.Agendamento import pegar_arq_relogio_horario

__version__ = '1.0'