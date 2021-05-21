""""
    PLUS-TI TECNOLOGIA DA INFORMAÇÃO
    SICALC

    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from os import getcwd
from PIL import Image
from time import sleep
import pyautogui as acoes
from PIL.ImageOps import invert

from scripts.Log import *
from scripts.VerTela import *

QUANTIDADE_TENTATIVAS = 30
TEMPO_BAIXO = 0.5
TEMPO_MEDIO = 1
TEMPO_ALTO = 2
TEMPO_GERAL = 0

class RoboBase:
    def __init__(self, log, ok, fail):
        """
            ROBOBASE: CONTEM AS INSTRUÇÕES BASICA PARA SER HERDADA NOS OUTROS SCRIPTS
        """
        self.fail = fail
        self.log = log
        self.ok = ok

    def executarOperacao(self, campos, tela, posicoes=False, duplo=False, tentativas=QUANTIDADE_TENTATIVAS):
        for _ in range(tentativas):
            for campo in campos:
                self.print(f'TENTANDO CLICAR {tela}->{campo}')
                if(VerTela().clicarObjTela(campo, posicoes, duplo)): print(f'ACHEI {campo}'); return True
            self.esperar(TEMPO_ALTO)
        return f"CLICADO {'DUAS VEZES' if(duplo) else 'UMA VEZ'} NA TELA {tela}", 1
           
    @log
    def doubleClick(self, x, y, d=0):
        try:
            acoes.doubleClick(x, y, duration=d)
            return f"CLICADO DUAS VEZES NA POSICAO ({x}, {y}, {d})", 1
        except Exception as erro: return f"ERRO AO CLICAR NA POSICAO ({x}, {y}) {erro}", 3

    @log
    def click(self, x, y, d=0):
        try:
            acoes.click(x, y, duration=d)
            f"CLICADO NA POSICAO ({x}, {y}, {d})", 1
        except Exception as erro: return f"ERRO AO CLICAR NA POSICAO ({x}, {y}, {d})  {erro}", 3

    def clickDireito(self, x, y, d=1):
        try:
            acoes.rightClick(x, y, duration=d)
            return f"CLICADO COM BOTAO DIREITO NA POSICAO ({x}, {y}, {d})", 1
        except Exception as erro: return f"ERRO AO CLICAR NA POSICAO ({x}, {y})  {erro}", 3
 
    @log
    def escreverTela(self, msg):
        acoes.write(msg)
        return f"ESCREVENDO TEXTO: {msg}", 1

    @log
    def esperar(self, tempo=TEMPO_GERAL):
        sleep(tempo)
        return f"ESPERANDO {tempo} SEGUNDOS", 1

    @log
    def esperarTela(self, telas, condicao=True):
        contagem = 0
        while(condicao if(isinstance(condicao, bool)) else condicao(contagem)):
            for t in telas:
                ver = VerTela().procurarObjTela(t['tela'], t['acao'])
                if(isinstance(ver, bool)):
                    if(ver): return f"ENCONTROU A TELA {t['tela']}!", 1

                if(isinstance(ver, str)):
                    if(ver == "ERRO EM CONECTAR NO BANCO DE DADOS!"): 
                        msg = "ERRO EM CONECTAR NO BANCO DE DADOS!"
                        self.print(msg, False)
                        raise Exception('ERRO EM CONECTAR NO BANCO DE DADOS!')
                sleep(1)
                print(f"AGUARDANDO A TELA {t['tela']} COM ACAO {t['acao']}, CONTAGEM: {contagem}")
                contagem += 1
        return f"NÂO ENCONTROU A TELA {t['tela']}!", 2

    def alterarPixels(self, img):
        for x in range(img.size[0]):
            for y in range(img.size[1]):
                img.putpixel((x, y), 255 if(img.getpixel((x, y)) == 226 or img.getpixel((x, y)) == 149) else img.getpixel((x, y)))
        return img

    def press(self, txt):
        acoes.press(txt)

    @log
    def print(self, msg, tipo=True): return msg, tipo
