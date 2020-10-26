a = "Calabresa"
b = "Frango c/ catupiry"
c = "Bacon"
d = "Mussarela"
print("               PIZZARIA GUANANDI II")
print("\n#####################################################")
print(" - - - - - - - - - - - Cardapio - - - - - - - - - - -")
print("#####################################################")
print("\nSelecione a opção desejada:")
print("1 - {}               3 - {}   " .format(a, c))
print("2 - {}      4 - {}" .format(b, d))

sabor = input("\nQual sabor? ")

if sabor == "1":
    print("Voce escolheu a pizza de {}." .format(a))
elif sabor == "2":
    print("Voce escolheu a pizza de {}." .format(b))
elif sabor == "3":
    print("Voce escolheu a pizza de {}." .format(c))
elif sabor == "4":
    print("Voce escolheu a pizza de {}." .format(d))



