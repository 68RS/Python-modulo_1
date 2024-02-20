#  if, elif e else

idade = int (input("Quantos anos voce tem?"))
print("Exemplo de comando if")
if idade >= 18:
    print("Voce e maior de idade")
elif idade >=16:
    print("Somente acompnhado de um responsavel")
else: 
    print("Voce e menor de idade")

mensagem = "Pode tirar a CNH" if idade >= 18 else "Voce nao pode tirar CNH"
print(mensagem)
18188