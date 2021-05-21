""""
    PLUS-TI TECNOLOGIA DA INFORMAÇÃO
    CSI_CARGO

    GREGORIO HONROATO: GREGORIO.HONORATO@PLUS-TI.COM.BR
    WHATSAPP: (19) 99250-9913

"""

from os.path import isfile, isdir
from os import makedirs, getcwd
from ast import literal_eval

from scripts.Log import *

class Config:
    def __init__(self):
        r"""
            GERA OS ARQUIVOS DE APONTAMENTO
            NÃO ESQUEÇA DE DEFINIR 'r' ANTES DOS CAMINHOS EXTENSOS 
            EX: r'C:\Users\Gregorio\Documents\TRABALHOS\PROJETOS\DOCUMENTO DE IMPORTACAO\log.txt'
        """
        self.estado = False
        self.json = {'pasta_txt_ponto': {'caminho': '', 'tipo': 'pst'},
                     'usuario': 'mestre', 'senha': 'CSIsb2021',
                     'caminho_programa': r'C:\totvs\CorporeRM\RM.Net\RM.exe'}
        
        self.arquivo_config = getcwd() + '\\config.json'
        
        self.lerJson()
        self.verificar_arquivosPastas()

    def verificar_arquivosPastas(self):
        """ ANTES DE INICIAR O SCRIPT ELE VERIFICA SE TODOS ARQUIVOS E PASTAS EXISTE """
        for pst in self.json: 
            if self.json[pst]['tipo'] == 'pst': 
                if self.json[pst]['caminho'] ==  '': 
                    mainlog(f'PRECISA CONFIGURAR O {self.arquivo_config} {pst}', 4); return False
                self.criar_pasta(self.json[pst]['caminho'])
                
            if self.json[pst]['tipo'] == 'arq':
                if not isfile(self.json[pst]['caminho']): 
                    mainlog(f'PRECISA CONFIGURAR O {self.arquivo_config} {pst}', 4); return False
                
        self.estado = True
        
    def criar_pasta(self, pst):
        ' CRIA A PASTA SE NAO EXISTIR '
        try:
            if not isdir(pst): 
                makedirs(pst); self.print(f'CRIANDO A PASTA {pst}'); return True
        except Exception as e: self.print(f'ERRO EM CRIAR A PASTA {pst}: {e}', False)
        return False

    def lerJson(self):
        """ E GUARDA O ARQUIVO AS CONFIGURAÇÕES EM MEMÓRIA """
        if(isfile(self.arquivo_config)):
            with open(self.arquivo_config, 'r', 
                      encoding='utf-8', errors='ignore') as arq:
                self.json = literal_eval(arq.read())
        else: self.criarConfig()

    def criarConfig(self):
        """CRIAR OS ARQUIVOS VAZIOS"""
        with open(self.arquivo_config, 'w', encoding='utf-8', errors='ignore') as arq:
            arq.write(f"{str(self.json)}")

    def print(self, msg, tipo=True):
        mainlog(msg, tipo)
