import pyrebase

DB_URL = ""
contenedor = "simos"
def obtenerBasedeDatos():

    config = {
        "apiKey": " AIzaSyD1JMfM3s_b5uAxRW8CVtqtMorRcYgtAec",
        "authDomain": "practica26-12e9c.firebaseapp.com",
        "databaseURL": "https://databaseName.firebaseio.com",
        "storageBucket": "practica26-12e9c.appspot.com"
    }

    firebase = pyrebase.initialize_app(config)

    pass

def grabarEventos(evento):
    db=obtenerBasedeDatos()
    results=db.child(contenedor).child(evento)
    pass

# config = {
#   "apiKey": " AIzaSyD1JMfM3s_b5uAxRW8CVtqtMorRcYgtAec",
#   "authDomain": "practica26-12e9c.firebaseapp.com",
#   "databaseURL": "https://databaseName.firebaseio.com",
#   "storageBucket": "practica26-12e9c.appspot.com"
# }
#
# firebase = pyrebase.initialize_app(config)
# # Get a reference to the auth service
# auth = firebase.auth()
#
# # Log the user in
# user = auth.sign_in_with_email_and_password('cmanosalvas95@gmail.com', '123456')
# db = firebase.database()
#
# # data to save
# data = {
#     "name": "Mortimer 'Morty' Smith"
# }
#
# # Pass the user's idToken to the push method
# results = db.child("users").push(data, user['IMu6u33bdiYyOlMVVfdJlV3EfvP2'])
