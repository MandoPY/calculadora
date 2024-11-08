# função com parametro perfil
def loginUsuario(perfil):
    # converte as letras pra minusculas
    perfil = perfil.lower()
    # se o parametro for igual a "admin"
    if perfil == "admin":
        # imprime boas vindas para o administrador
        print("Bem-vindo, Administrador.")
    # caso contrario
    else:
        # imprime boas vindas para o usuario
        print("Bem-vindo, Usuário")

# chamada da função com diferentes parametros
loginUsuario("Admin")
loginUsuario("admin")
loginUsuario("User")
loginUsuario("usuário")
loginUsuario("etc.")