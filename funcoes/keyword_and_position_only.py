#hibrido

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Uno", 1999, "WIL-1999", marca="Fiat", motor="1.6", combustivel="Gasolina")

#criar_carro(modelo="Uno", ano=1999, placa="WIL-1999", marca="Fiat", motor="1.6", combustivel="Gasolina")
