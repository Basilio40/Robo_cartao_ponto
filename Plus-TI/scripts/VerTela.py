from os import getcwd
from time import sleep
from pyautogui import locateOnScreen, locateCenterOnScreen, click, doubleClick, Point, ImageNotFoundException

from scripts.Log import Log

class VerTela:
    def __init__(self):
        pre = r'\recursos'
        self.telas = {
            'lb_senha': getcwd() + pre + r'\lb_senha.png',
            'lb_fechar': getcwd() + pre + r'\lb_fechar.png',
            'bt_fechar': getcwd() + pre + r'\bt_fechar.png',                       
            'logo_totvs': getcwd() + pre + r'\logo_totvs.png',
            'lb_usuario': getcwd() + pre + r'\lb_usuario.png',
            'lb_usuario2': getcwd() + pre + r'\lb_usuario2.png',           
            'lb_usuario3': getcwd() + pre + r'\lb_usuario3.png',    
            'lb_importar': getcwd() + pre + r'\lb_importar.png',
            'bt_importar': getcwd() + pre + r'\bt_importar.png',
            'lb_concluido': getcwd() + pre + r'\lb_concluido.png',
            'lb_menu_sistema': getcwd() + pre + r'\lb_menu_sistema.png',
            'lb_entrada_de_dados': getcwd() + pre + r'\lb_entrada_de_dados.png',            
            'lb_selecionar_arquivo': getcwd() + pre + r'\lb_selecionar_arquivo.png'
        }

        v = lambda: True
        f = lambda: False
        eb = lambda: 'ERRO EM CONECTAR NO BANCO DE DADOS!'

        self.acoes = {'verificar': [v, f], 'erroBanco': [eb, f]}

    def procurarObjTela(self, obj, acao):
        try: return self.acoes[acao][0]() if(locateOnScreen(self.telas[obj])) else self.acoes[acao][1]()
        except ImageNotFoundException as e: Log(f'NAO FOI POSSIVEL ENCONTRAR A IMAGEM {obj}')
        except Exception as erro: Log(f'ERRO EM PROCURAR OBJETO: {erro}'); sleep(1); return False

    def clicarObjTela(self, obj, posicoes=False, duplo=False):
        try:
            cli = locateCenterOnScreen(self.telas[obj], grayscale=True)
            if(None != cli): 
                if(duplo): doubleClick(cli if posicoes == False else Point(posicoes[obj][0] + cli.x, posicoes[obj][1]+ cli.y))
                else: click(cli if posicoes == False else Point(posicoes[obj][0] + cli.x, posicoes[obj][1]+ cli.y))
                return True
            return False
        except ImageNotFoundException as e: Log(f'NAO FOI POSSIVEL ENCONTRAR A IMAGEM {e} {obj}')
        except Exception as erro: Log(f'ERRO EM CLICAR OBJETO OBJETO: {erro}'); return False
