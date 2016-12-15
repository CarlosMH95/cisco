from ubidots import ApiClient
import random
import time

api = ApiClient(token='Sm5ihUyNjAoPy7FZMsVhgLS07VzFxp')
my_variable = api.get_variable('5851e90276254275d62f5fc9')

dato = 100

while dato > 0:
    dato = random.randrange(40, 80)
    print (dato)
    new_value = my_variable.save_value({'value': dato})
time.sleep(2)