




username_recibido = username_recibido.strip()

#PEP 8
if username_recibido == "": 
  print ("Usuario inexistente")
  print ("Manda un usuario valido")
elif len(username_recibido) <=14:
  print("la longitud del nombre de usuario es la adecuada")
else: 
  print("paso algo raro con el nombre de usuario")
  
print("\n validando email")    

if email_recibido.count("@") != 1:
  print("el formato del correo no es valido (debe contener un @)")
elif not (email_recibido.endswith(".com")) or email_recibido.endswith(".org"):
  print ("correo no valido")
else:
  print("El correo es valido :D")

print("Validando contraseña")

if len(password_recibida) >= 8:
  if password_recibida == username_recibido:
    print("la contraseña no puede ser igual al nombre de usuario")
  else:
    print("la contraseña cumple con los requisitos")
else:
  print("La contraseña es meisado corta:")

print("Validando roles")

roles_permitidos = "ADMIN SUPERADMIN MODERADOR USER"

if role_recibido in roles_permitidos: 
  print("pasale")
else:
  print("sin permisos")
  

  
  