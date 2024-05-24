import random # Biblioteca para utilizar o random

print("===----------------------------------===")
print("===     JOGO DO NÚMERO SECRETO       ===")
print("===----------------------------------===")

dificuldade = input("Você quer jogar na dificuldade dificil, médio ou fácil? [d,m,f]:") # Pergunta qual a dificuldade que o usuário pretende jogar
tentativas_maximas = 5 # Número de tentativas máximas ideal

if dificuldade == "d": # Se a dificuldade for díficil
  tentativas_maximas = 3 # Número de tentativas máximas
elif dificuldade == "m": # Se a dificuldade for médio
  tentativas_maximas = 5 # Número de tentativas máximas
elif dificuldade == "f": # Se a dificuldade for fácil
  tentativas_maximas = 10 # Número de tentativas máximas 
else: # Se não for nenhuma das alternativas digitadas, executa essa linha de código:
  print("Você não definiu a dificuldade, sua dificuldade foi alterada para mediano\n") # Mostra que a alternativas digitada não é válida, utiliza um número padrão para as tentativas

numero_secreto = random.randint(1, 100) # Código para gerar um número aleatório entre 1 e 100
tentativas = 1 # Tentativas no usuário

while tentativas <= tentativas_maximas: # Enquanto o número de tentativas do usuário for menor ou igual ao número máximo de tentativas, executa essa linha de código
  print("Tentativa", tentativas, "de", tentativas_maximas) # Para mostrar o número de tentativas
  numero_usuario = int(input("Chute o número secreto:")) # Para digitar o número secreto

  if numero_secreto == numero_usuario: # Se o número secreto for igual ao número do usuário, executa essa linha de código
    print("Você acertou!\n") # Mostra que o usuário acertou
    break # quebra o código, para a execução do programa
  elif numero_secreto > numero_usuario: # Se o número secreto for maior que o número do usuário, executa essa linha do código
    print("O número secreto é maior!\n") # Mostra que o número secreto é maior
  else: # Se não for nenhuma das opções, executa essa linha de código
    print("O número secreto é menor!\n") # Mostra que o número secreto é menor

  # tentativas = tentativas + 1
  tentativas += 1 # Adiciona mais uma tentativa

if tentativas > tentativas_maximas: # Se o número de tentativas for maior que o número máximo de tentativas, executa essa linha de código
  print("Você perdeu as suas tentativas! O número secreto era", numero_secreto) # Mostra que você perdeu as tentativas, além de mostrar o número secreto
else: # Se não for menor do que as tentativas_máximas, executa essa linha de código
  print("Parabéns, você ganhou o jogo!") # Mostra que você venceu no jogo