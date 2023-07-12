# validador_usuario.py

def validar_usuario(username):
    if len(username) < 7:
        return "El nombre de usuario debe contener al menos 7 caracteres"
    elif len(username) > 12:
        return "El nombre de usuario no puede contener más de 12 caracteres"
    elif not username.isalnum():
        return "El nombre de usuario puede contener solo letras y números"
    else:
        return True
