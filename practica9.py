from ubidots import ApiClient

api = ApiClient(token='aw3vYXYy13i9xVl75Zt1jQAsQpde8j')

my_variable = api.get_variable('5848c8d47625422c4ec9767e')
new_value = my_variable.save_value({'value': 63})