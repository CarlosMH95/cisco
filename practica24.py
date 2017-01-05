# def suma(a,b):
#     return a+b
#
# def imprimir(resultado):
#     print("El resultado es ",resultado)
#
# x=5
# y=15
# imprimir(suma(x,y))
# def suma(a,b):
#     return a+b
#
# def imprimir(resultado=""):
#     if not resultado:
#         print("No hay resultado")
#     else:
#         print("El resultado es ",resultado)
#
# x=5
# y=15
# imprimir(suma(x,y))
# imprimir()
#
# def resta(a,b):
#     return a-b
#
# def multiplicacion(a,b):
#     return a*b
#
# def operacion(f, a, b):
#     return f(a,b)
#
# x, y=(10,-15)
# print("Resultado 1:", operacion(suma,x,y))
# print("Resultado 2:", operacion(resta,x,y))
# print("Resultado 3:", operacion(multiplicacion,x,y))
# def validacion(func):
#     def envoltura(cedula):
#         if cedula[0]=="0":
#             return func(cedula)
#         else:
#             print("cedula no valida")
#             return None
#     return envoltura
#
# @validacion
# def ingresar_cedula(cedula):
#     print("Cedula ingresada: ", cedula)
#
# ingresar_cedula("0922934468")
# ingresar_cedula("1922934468")
# def miFuncion(*args, **kwargs):
#     print (args)
#     print (kwargs)
#
# miFuncion(1,2,3,a=1,b=2)
def suma(*args):
    total=0
    for i in args:
        total+=i
    return total

def operacion(f, *args):
    return f(*args)

print ("Resultado 1:", operacion(suma, 1,6,5,8,9,3,2,4,8))