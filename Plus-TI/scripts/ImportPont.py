""""
    PLUS-TI TECNOLOGIA DA INFORMAÇÃO
    CSI_CARGO

    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from scripts import *


class ImportPont(RoboBase):
    def __init__(self):
        mainlog('>'*100)
        self.arquivos_pontos = pegar_arq_relogio_horario()

        if len(self.arquivos_pontos) == 0: 
            self.print(f'SEM ARQUIVO PARA PROCESSAR!'); return

        self.conf = Config()
        self.abrir_programa()
        self.abrir_tela_importacao()
        mainlog('<'*100)

    def abrir_programa(self):
        acoes.hotkey('win', 'r')
        self.escreverTela(self.conf.json['caminho_programa'])
        acoes.press('enter')

    def abrir_tela_importacao(self):
        self.esperar_tela_login()
        self.esperar_tela_sistema()
        
        for arq in self.arquivos_pontos: 
            self.esperar_tela_importacao()
            self.abrir_menu_importacao()
            self.realizar_importacoes(arq)
        self.fechando_app()

    @log
    def fechando_app(self):
        self.esperar(10)
        acoes.hotkey('ALT', 'F4')
        self.esperar(5)
        # self.executarOperacao(['lb_fechar'], tela='TELA DO SISTEMA', duplo=False, tentativas=5)
        acoes.press('enter')
        return 'FECHANDO O SISTEMA', 1
            
    def realizar_importacoes(self, arq):
        self.esperarTela(['lb_selecionar_arquivo'], True)
        self.esperar(TEMPO_ALTO)
        self.escreverTela(f'{arq}')
        self.esperarTela(TEMPO_ALTO)
        acoes.press('enter')
        for _ in range(22): acoes.press('tab')
        self.esperarTela(TEMPO_ALTO)
        acoes.press('enter')
        self.esperar(TEMPO_ALTO)
        self.esperarTela(['lb_concluido'], True)
        self.esperarTela(['bt_fechar'], True)        
        acoes.hotkey('ALT', 'F')
        self.esperar(TEMPO_ALTO)

    @log
    def esperar_tela_login(self):
        self.esperarTela(['logo_totvs2', 'lb_usuario'], True)
        self.executarOperacao(['lb_usuario', 'lb_usuario2', 'lb_usuario3'], tela='TELA LOGIN', duplo=True)
        self.esperarTela(TEMPO_BAIXO)
        self.escreverTela(self.conf.json['usuario'])
        acoes.press('tab')
        self.esperarTela(TEMPO_BAIXO)
        self.escreverTela(self.conf.json['senha'])
        self.esperarTela(TEMPO_BAIXO)
        acoes.press('enter')
        return f'ENTRANDO NO SISTEMA', 1

    @log
    def esperar_tela_sistema(self):
        self.executarOperacao(['lb_entrada_de_dados'], tela='TELA DO SISTEMA', duplo=False)
        return 'ENCONTRADO A TELA DO SISTEMA E CLICADO NO MENU DE IMPORTACAO', 1

    @log
    def esperar_tela_importacao(self):
        self.executarOperacao(['bt_importar'], tela='TELA DO SISTEMA', duplo=False)
        return "ABRINDO TELA DE IMPORTACAO", 1
    
    @log
    def abrir_menu_importacao(self):
        self.executarOperacao(['lb_importar'], 'TELA IMPORTACAO', {'lb_importar': (0, 13)}, duplo=True)
        self.esperar(TEMPO_BAIXO)
        acoes.press('tab')
        self.esperar(TEMPO_BAIXO)
        acoes.press('enter')
        return 'ROBO ENCONTROU A TELA DE IMPORTAR ARQUIVOS', 1

    def print(self, msg, tipo=1): mainlog(msg, tipo)

    def __del__(self): mainlog('FECHANDO O PROGRAMA')