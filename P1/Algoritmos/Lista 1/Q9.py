# Crie um programa que pergunta o nome do usuário e o ano de nascimento do usuário e
# calcula qual idade ele tem (ou terá, se ainda não fez aniversário neste ano). Ex.: Nome =
# Carlos, Ano = 1999. O programa mostra a mensagem: “Carlos tem 20 anos”.

nome = str(input('Qual o seu nome?  '))
ano_nascimento = float(input('Qual o ano de nascimento?   '))
ano_atual = float(input('Digite o ano atual '))
idade = ano_atual - ano_nascimento
print(nome,',sua idade é  ',idade)