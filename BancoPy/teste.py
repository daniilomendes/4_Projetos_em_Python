from models.cliente import Cliente
from models.conta import Conta


danilo: Cliente = Cliente('Danilo Mendes', 'danilo@gmail.com', '123.123.123-12', '30/01/2000')
angelina: Cliente = Cliente('Angelina Lina', 'angelina@gmail.com', '789.789.789.78', '08/07/1989')

'''print(danilo)
print(angelina)'''

contad: Conta = Conta(danilo)
contaa: Conta = Conta(angelina)

print(contad)
print(contaa)
