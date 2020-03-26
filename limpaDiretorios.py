###
# Autor: Marcelo Santana Camacho
# Afiliação: Campus de Salinópolis/UFPA
# 26 de março de 2020
# Descrição: Rotina para limpar diretórios vazios do sistema de arquivos.
###
import os
from tkinter import ttk, filedialog

Path = filedialog.askdirectory(title = 'Escolha o diretorio para limpar:')
Diretorios = os.listdir(Path)
for dir in Diretorios:
    fullPath=Path+'/'+dir
    if( os.path.isdir(dir) ):
        print(fullPath+' é um diretorio')
        if not os.listdir(dir):
            print('Deve ser deletado!!')
            os.rmdir(dir)
        else:
            print('>> Mantido!!')
    else:
        print(dir+' não é um diretório')
