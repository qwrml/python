from address import Address
from mailing import Mailing

to_address = Address('12345', 'Москва', 'Ленина', '10', '25')
from_address = Address('56789', 'Томск', 'Пушкина', '5', '12')

mailing = Mailing(to_address = to_address, from_address = from_address, cost = 50, track = 'Tr123456')
print(mailing)
