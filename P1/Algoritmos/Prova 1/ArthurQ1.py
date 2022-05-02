for i in range(1,76):
  print('Informe o número da sua matrícula', i, ':')
  matricula = input()
  nota = float(input('Informe sua nota: '))
  if nota >= 0 and nota  <= 4.9:
    print('Você pertence a sala D')
  if nota >= 5 and nota <= 6.9:
    print('Você pertence a sala C')
  if nota >= 7 and nota <= 8.9:
    print('Você pertence a sala B')
  else:
    print('Você pertence a sala A')