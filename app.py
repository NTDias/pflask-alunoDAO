from flask import Flask, render_template , request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)
app.secret_key = "Uma_chave_não_muito_confiável"


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/aluno')
def listar_aluno():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/listar.html', lista=lista)

@app.route('/aluno/form') 
def form_aluno():
    return render_template('/aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])  
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade) 

    if result["status"] == "ok":
        flash("Regitro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/aluno')


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/listar.html', lista=lista)

@app.route('/professor/form') 
def form_professor():
    # CORREÇÃO: Passar um professor vazio [id, nome, disciplina]
    professor_vazio = [0, "", ""]
    # CORREÇÃO: Usar a variável 'professor'
    return render_template('professor/form.html', professor=professor_vazio)

@app.route('/professor/salvar/', methods=['POST']) 
def salvar_professor():
    id = request.form.get('id')
    if id == '0' or id == '':
        id = None
        
    nome = request.form['nome']
    disciplina = request.form['disciplina'] 
    
    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina) 

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')


@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/listar.html', lista=lista)

@app.route('/curso/form') 
def form_curso():
    curso_vazio = [0, ""]
    return render_template('curso/form.html', curso=curso_vazio)

@app.route('/curso/salvar/', methods=['POST']) 
def salvar_curso(id=None):
    nome_curso = request.form['nome_curso']
    
    dao = CursoDAO()
    result = dao.salvar(id, nome_curso) 

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')


@app.route('/saudacao/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)

@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    email = request.form['email']
    senha = request.form['senha']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    dados = "" 
    
    if(request.method == 'POST'):
        nome = request.form['nome'] 
        data_nascimento = request.form['data_nascimento']
        cpf = request.form['cpf']
        nome_mae = request.form['nome_mae']
        
        dados = f"Cadastro Recebido: \n\n Nome: {nome}, \n Nasc: {data_nascimento}, \n CPF: {cpf}, \n Mãe: {nome_mae}"
        
        return render_template('cadastro/cadastro.html', valor_recebido=dados)

    return render_template('cadastro/cadastro.html', valor_recebido=dados) # Passa 'dados' vazios


if __name__ == '__main__':
    app.run(debug=True)