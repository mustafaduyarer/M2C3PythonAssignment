"""
Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario y una contraseña.
Crea un objeto usando la clase.

Create a python class called user to use the INIT method and create a username and a password.
Create an object using class.
"""


class Usuario:
    def __init__(self, nombre, contraseña):
        self.nombre = nombre
        self.contraseña = contraseña

    def conditional(self):
        if self.nombre == 'Mustafa' and self.contraseña == 1979:
            return f'¡Bienvenido {self.nombre} a su cuenta de mail!'
        else:
            return f'Nombre de usuario y/o contraseña incorrecta'


user1 = Usuario('Mustafa', 1979)
usuario_1 = user1.conditional()

user2 = Usuario('Mustafa', 197)
usuario_2 = user2.conditional()

print(usuario_1)
print(usuario_2)

print(usuario_1)
print(usuario_2)

print(usuario_1)
print(usuario_2)