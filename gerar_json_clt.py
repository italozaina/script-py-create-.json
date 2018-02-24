# encoding=utf8  
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

import os
import json

# Carrega um json e mostra os dados
# data = json.load(open('teste.json'))
data = json.load(open('louvores2018.json'))


f = open('clt.json','w')
json = """[
"""
for louvor in data:  
    titulo = louvor['title'].upper().strip()

    # conta quantos arquivos serão criados verificando as estrofes
    arquivos = louvor['content'].split('\n\n')
    num = len(arquivos)
#     json +="""
#     {
# """
#     json += '        "description":"'+titulo+'",\n'
#     json += '        "product":"'+str(num)+'"'
#     json +="""
#     },"""

    json +="""{ """
    json += '"description":"'+titulo+'", '
    json += '"product":"'+str(num)+'"'
    json +=""" },
"""    

json += """
]"""
print('Arquivo criado')
f.write(json)
f.close()