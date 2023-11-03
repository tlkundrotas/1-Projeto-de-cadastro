''' PROJETO 1 
Objetivo de projeto
Estamos criando um módulo de login do nosso aplicativo, e você deve obter as seguintes informações do funcionário.

Módulo 1 - Gerar registro do funcionário
Funcionalidades do módulo 1
1. Obtenha o nome do usuário
2. Obtenha a idade do usuário
3. Registre de forma automática a data do cadastro do usuário, usando a data do registro como data de registro
4. Para cada novo funcionário que é registrado na empresa, ele recebe um dos seguintes cartões, que é sorteado de forma aleatória:
   cartoes = ['R$50,00','R$250,00','R$120,00']
5. Guarde informações sobre a data de aniversário do funcionário(dd/mm/aaaa)

Módulo 2 - Gerar apresentação do usuário
Funcionalidades do módulo 2 - Mensagem de boas vindas!
Usando os dados obtidos no módulo 1, exiba as seguintes informações:
1. Olá (nome do usuário), seu registro foi concluído com sucesso no dia(data de cadastro no formato dd/mm/aaaa).
Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de (valor sorteado).
'''

#Módulo 1 - Gerar registro do funcionário
nome_ususario = input('Qual o seu nome?')
from datetime import datetime
from datetime import date
data = date.today()
data_atual = data.strftime('%d/%m/%Y')
aniversario_funcionario = datetime.strptime(input('Qual a sua data de nascimento?'),'%d/%m/%Y')
import random
cartoes = ['R$50,00','R$250,00','R$120,00']

#Módulo 2 - Gerar apresentação do usuário
print(f'Olá {nome_ususario}, seu registro foi concluído com sucesso no dia {data_atual} .Parabéns, houve um sorteio e você ganhou um cartão de compras no valor de {random.choice(cartoes)}')
