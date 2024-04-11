  for i in (1, 10):
    print(i)
 for i in range(1, 11):
    print(i, end=" ")
# pedir ao usuario para dar um comando de print
comando = input(' \n Por gentilega gostaria que escolhe-ce um comando de impressão: ')
if not comando:
    print('comando invalido')
    exit()
for i in range(1, 11):
    exec(f"{comando}({i})")
# mostrar se o usúario não quiser receber os numeros de 1 a 10
resposta = input("Deseja que os numeros continuem sendo de 1 a 10(sim/não): ")
if resposta.lower() == "não":
    for i in range(1, 11):
        print(i)
elif resposta.lower() == "sim":
    numero = int(input("insira um numero desejado para trocar: "))
    for i in range(1, numero + 1):
        print(i)
else:
    print('Repost invalida,por gentilesa coloque \'sim\' ou \'não\'.')