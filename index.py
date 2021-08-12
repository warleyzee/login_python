#========= Importar bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import dataBase

#========= criar janela de Login
jan = Tk()
jan.title("PY - Python - Acess Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False, height=False)
jan.iconbitmap(default="icon/icone.ico")

#========= Carregando Imagens
logo = PhotoImage(file="icon/logo.png")


#========= separadores da janela - Esquerda e direita
LeftFrame = Frame(jan, width=200, height=300, bg="MIDNIGHTBLUE", relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=395, height=300, bg="MIDNIGHTBLUE", relief="raise")
RightFrame.pack(side=RIGHT)

#========= Inserindo Logo na esquerda
LogoLabel = Label(LeftFrame, image=logo, bg="MIDNIGHTBLUE")
LogoLabel.place(x=50, y=100)

#========= Campos para fazer o login

UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="White")
UserLabel.place(x=10, y=100)
UserEntry = ttk.Entry(RightFrame, width=30)
UserEntry.place(x=95, y=106)

PassLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
PassLabel.place(x=10, y=150)
PassEntry = ttk.Entry(RightFrame, width=30, show="•")
PassEntry.place(x=95, y=155)

# Função para validar o login no banco 
def Login():
    user  = UserEntry.get()
    senha = PassEntry.get()

    dataBase.cursor.execute("""
    SELECT * FROM Usuarios
    WHERE (Usuario = ? AND senha = ?)
    """, (user, senha))
    autentic = dataBase.cursor.fetchone()
    try:
        if(user in autentic and senha in autentic):
            messagebox.showinfo(title="Entrou", message="Seja Bem Vindo" + user)

            LoginButton.place(x=500000)
            CadastroButton.place(x=500000)
            UserLabel.place(x=500000)
            UserEntry.place(x=500000)
            PassLabel.place(x=500000)
            PassEntry.place(x=500000)

            voltar = ttk.Button(RightFrame, text="Logoff", width=10)
            voltar.place(x=310, y=10)
        else:
            pass
    except:
        messagebox.showinfo(title="Cadastro", message="Usuário ou Senha Invalido.")

LoginButton = ttk.Button(RightFrame, text="Entrar", width=10, command=Login)
LoginButton.place(x=210, y=190)

#Função para ciar um novo usuario 
def Cadastrar():
    #Removendo botões da tela:
    LoginButton.place(x=500000)
    CadastroButton.place(x=500000)
    UserLabel.place(x=500000)
    UserEntry.place(x=500000)
    PassLabel.place(x=500000)
    PassEntry.place(x=500000)

    #inserir campos de Cadastro
    nomeLabel = Label(RightFrame, text="Nome:* ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    nomeLabel.place(x=5, y=5)
    nomeEntry = ttk.Entry(RightFrame, width=39)
    nomeEntry.place(x=100, y=10)

    emailLabel = Label(RightFrame, text="E-mail:* ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    emailLabel.place(x=5, y=41)
    emailEntry = ttk.Entry(RightFrame, width=39)
    emailEntry.place(x=100, y=46)

    telefoneLabel = Label(RightFrame, text="Telefone: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    telefoneLabel.place(x=5, y=80)
    telefoneEntry = ttk.Entry(RightFrame, width=39)
    telefoneEntry.place(x=100, y=85)

    paisLabel = Label(RightFrame, text="País: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    paisLabel.place(x=5, y=120)
    paisEntry = ttk.Entry(RightFrame, width=39)
    paisEntry.place(x=100, y=125)

    usuarioLabel = Label(RightFrame, text="Usuario:* ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    usuarioLabel.place(x=5, y=157)
    usuarioEntry = ttk.Entry(RightFrame, width=39)
    usuarioEntry.place(x=100, y=165)
    
    senhaLabel = Label(RightFrame, text="Senha:* ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg='White')
    senhaLabel.place(x=5, y=199)
    senhaEntry = ttk.Entry(RightFrame, width=39)
    senhaEntry.place(x=100, y=202)

   
    #função para voltar a pagina princial de login    
    def backToLogin():
        nomeLabel.place(x=500000)
        nomeEntry.place(x=500000)
        emailLabel.place(x=500000)
        emailEntry.place(x=500000)
        telefoneLabel.place(x=500000)
        telefoneEntry.place(x=500000)
        paisLabel.place(x=500000)
        paisEntry.place(x=500000)
        voltar.place(x=50000)
        cadastrarUser.place(x=5000)
        CadastroButton.place(x=50000)
        usuarioLabel.place(x=50000)
        usuarioEntry.place(x=50000)
        senhaLabel.place(x=50000)
        senhaEntry.place(x=50000)


        UserLabel = Label(RightFrame, text="Usuário: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="White")
        UserLabel.place(x=10, y=100)
        UserEntry = ttk.Entry(RightFrame, width=30)
        UserEntry.place(x=95, y=106)

        PassLabel = Label(RightFrame, text="Senha: ", font=("Century Gothic", 15), bg="MIDNIGHTBLUE", fg="white")
        PassLabel.place(x=10, y=150)
        PassEntry = ttk.Entry(RightFrame, width=30, show="•")
        PassEntry.place(x=95, y=155)

        LoginButton = ttk.Button(RightFrame, text="Entrar", width=10, command=Login)
        LoginButton.place(x=210, y=190)

        # CadastroButton = ttk.Button(RightFrame, text="Cadastrar", width=10, command=Cadastrar)
        # CadastroButton.place(x=125, y=190)

    #função para criar usuario no banco 
    def Cadastrar():
        CadastroButton.place(x=50000)
        nome = nomeEntry.get()
        email = emailEntry.get()
        telefone = telefoneEntry.get()
        pais = paisEntry.get()
        usuario = usuarioEntry.get()
        senha = senhaEntry.get()

        if(nome== "" and email== "" and usuario== "" and senha== ""):
            messagebox.showerror(title="Cadastro", message="Campos obrigatorios não preenchidos!")
        else:
            dataBase.cursor.execute("""
            INSERT INTO Usuarios (Nome, Email, telefone, Pais, Usuario, Senha) 
            VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, email, telefone, pais, usuario, senha))
            dataBase.conn.commit()
            messagebox.showinfo(title="CADASTRO", message="Cadastrado com Sucesso!")

    cadastrarUser = ttk.Button(RightFrame, text="Cadastrar", width=10, command=Cadastrar)
    cadastrarUser.place(x=290, y=250)

    voltar = ttk.Button(RightFrame, text="Voltar", width=10, command=backToLogin)
    voltar.place(x=200, y=250)
    
  
CadastroButton = ttk.Button(RightFrame, text="Cadastrar", width=10, command=Cadastrar)
CadastroButton.place(x=125, y=190)



#manter a janela aberta.
jan.mainloop()

