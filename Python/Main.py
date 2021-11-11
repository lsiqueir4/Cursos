import pandas as pd
from twilio.rest import Client

# -*- coding: utf-8 -*-

#instalar biblioteca: pip install "nome da biblioteca"
#Saber quais bibliotecas estao instaladas: pip freeze

# pandas
# openpyxl
# twilio

# Passo a passo de solução

# abrir 6 arquivos excel
lista_meses = ['janeiro' ,'fevereiro','março', 'abril', 'maio', 'junho'] # toda lista fica entre []

# Your Account SID from twilio.com/console
account_sid = "ACa2616ef68e11cffd2078e26661d7aebd"
# Your Auth Token from twilio.com/console
auth_token  = "a443de9898fcd8fdef02d81d4e21e543"

client = Client(account_sid, auth_token)

for mes in lista_meses: #for variavel in lista
    tabela_vendas = pd.read_excel(f'C:/Users/Viamar/Desktop/CURSO PYTHON/Aula Pyton Hash/{mes}.xlsx') #comando para o pandas fazer a leitura do arquivo excel
    if (tabela_vendas['Vendas'] > 55000).any(): #se algum valor da coluna vendas >55000
        vendedor = tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] # .loc ajuda a localizar linha na tabela
        vendas =  tabela_vendas.loc [tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] #.values só pega o valor, nao a tabela inteira
        print(f'no mês de {mes} , alguém bateu a meta! Vendedor: {vendedor} Vendas: {vendas}')
        message = client.messages.create(
            to="+5511956663035", 
            from_="+17472342316",
            body=f"no mês de {mes} , alguém bateu a meta! Vendedor: {vendedor} Vendas: {vendas}")
        print(message.sid)
        

    
# Para cada arquivo:
# Verificar se algum valor na coluna vendas >55k

# Se for >55k ->Envia um SMS com nome, mes e vendas do vendedor
# Caso não seja >55k nao fazer nada

