from flask import Flask ,render_template , request #Importando a biblioteca do flask


class Jogo:
    def __init__(self,nome,categoria,console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

#Lista como fator global
jogo1 = Jogo('Call of duty','Batalha naval', 'Todas as plataformas')
jogo2 = Jogo('Rainbow Six ', 'Estrategia','Todas as plataformas')
jogo3 = Jogo('Fortnite', 'Battle Royale','Todas as plataformas')
titulo = "Lista de Jogos"
lista = [jogo1 , jogo2 , jogo3]

app = Flask(__name__)



@app.route('/') #Definindo a rota da nossa aplicação
def rota_raiz():
    return render_template('Home.html', titulo_home = titulo, jogos=lista)


@app.route('/cadastroJogo')
def cadastroJogo():

    return render_template('cadastro.html', titulo_cadastro="Cadastre um novo Jogo")






@app.route('/criar')

def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome,categoria,console)
    lista.append(jogo)
    return render_template("Home.html", titulo = "Lista de Jogos" , jogos =lista)



app.run(debug=True)
