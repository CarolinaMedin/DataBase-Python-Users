"""
+ Abrir asistente 
+ Login
+ Si elige registro: creacion de usuario en la database
+ Si elige login: identificacion de usuario + pregunta
+ Creacion de notas: crear, mostrar, borrar.add
"""
from users import actions

print("""
Acciones disponibles:
    -registro
    -login 
""")

hazEl = actions.Acciones() # Instancio la clase 
action = input("Tienes dos opciones de inicio de sesion, elige una : ")

if action == "registro":
    hazEl.registro() 
    
elif action == "login":
    hazEl.login()
    

