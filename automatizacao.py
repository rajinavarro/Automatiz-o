from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pandas as pd
import requests
from bs4 import BeautifulSoup


login = str(input('Digite seu login: '))
senha = str(input('Digite sua senha: '))


chrome = webdriver.Chrome()
chrome.get('https://qacademico.ifce.edu.br/qacademico/index.asp?t=1001')

campo_busca = chrome.find_element_by_id('txtLogin')
campo_busca.send_keys(login)
campo_busca = chrome.find_element_by_id('txtSenha')
campo_busca.send_keys(senha)
campo_busca.send_keys(Keys.ENTER)

chrome.get('https://qacademico.ifce.edu.br/qacademico/index.asp?t=2045')



#Estabelecendo conexão com o servidor
req = requests.get('https://qacademico.ifce.edu.br/qacademico/index.asp?t=2032')

if req.status_code == 200:
    print('Requisição bem sucedida!!')
    content = req.content

#Extraindo tabelas
soup = BeautifulSoup(content, 'html.parser')
table = soup.find(name = 'table')

#Acessando tabelas como String via Pandas
tabel_str = str(table)

df = pd.read_html(tabel_str)[0]

#labels das tabelas
df.info()

print(df)