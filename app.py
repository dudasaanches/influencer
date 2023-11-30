from flask import Flask, render_template, request, redirect


app = Flask(__name__)
class cadInfluencers:
    def __init__(self,nome,plataforma,seguidores,areas):
        self.nome = nome
        self.plataforma = plataforma
        self.seguidores = seguidores
        self.areas = areas

lista=[]

@app.route('/')
def pokemon():
    return render_template('Influenciadores.html',Titulo = "Influenciadores Digitais",ListaInfluenciadores = lista)

@app.route('/Cadastro')
def cadastro():
    return render_template('cadastro.html', Titulo = "Cadastro de  Influenciadores")

@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    plataforma = request.form['plataforma']
    seguidores = request.form['seguidores']
    areas = request.form['areas']
    obj =cadInfluencers(nome,plataforma,seguidores,areas)
    lista.append(obj)
    return redirect('/')

@app.route('/excluir/<nomeinflu>', methods=['GET', 'DELETE'])
def excluir(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            lista.pop(i)
            break
    return redirect('/')

@app.route('/editar/<nomeinflu>', methods=['GET'])
def editar(nomeinflu):
    for i, influ in enumerate(lista):
        if influ.nome == nomeinflu:
            return render_template("Editar.html", Influencer=influ, Titulo="Alterar o influenciadores")

@app.route('/alterar', methods=['POST', 'PUT'])
def alterar():
    nome = request.form['nome']
    for i, influ in enumerate(lista):
        if influ.nome == nome:
            influ.nome = request.form['nome']
            influ.plataforma = request.form['plataforma']
            influ.seguidores = request.form['seguidores']
            influ.areas = request.form['areas']
    return redirect('/')


if __name__ == '__main__':
    app.run()