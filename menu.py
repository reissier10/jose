# jose


import os
import time


#cliente
#Funções 
    #Função cadastrar-------------------------------------------------
def cadastrar():
    nome_empresa = input('Digite o nome da empresa: ')
    cnpj = input('Digite sua cnpj: ')
    uf = input('Insira sua UF: ')
    t = int(input('Digite seu telefone: '))
    e = input('Digite seu email: ')
    agenda = open('%s_%s.txt' %(nome_empresa,cnpj),'a')
    agenda.write('%s %s,%s, %d, %s\n'%(nome_empresa, cnpj, uf, t, e))
    agenda.close()
    
    
    #----------------------------------------------------------------
    
def menu_cliente
    print(' MENU')
    print('1. Cadastrar')
    print('2. Editar')
    print('3. Listar')
    print('0. Sair')
    op = 1
    while op!=0:
        op = int(input('\nDigite a opção: '))
        if op==1:            
            cadastrar()            
        elif op==2:
            print("Desculpa, essa opção ainda não foi programada")
        
        elif op==3:
            ("Desculpa, essa opção ainda não foi programada")            
        elif op==0:
            print('Programa finalizado.')
            break
        else:
            print('Opção incorreta, tente novamente. ')
menu_cliente()


