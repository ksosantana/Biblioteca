from flask import Flask, render_template, send_from_directory, session, redirect, url_for

app = Flask(__name__, template_folder='telas', static_folder='organ')
app.secret_key = '123456'  # Chave necessária para utilizar sessões

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/livros/<path:filename>')
def livros(filename):
    return send_from_directory('livros', filename)

@app.route('/abrir/<filename>')
def abrir_livro(filename):
    ultimos = session.get('ultimos_livros', [])

    # Remove o arquivo caso já exista para evitar duplicação
    if filename in ultimos:
        ultimos.remove(filename)

    ultimos.insert(0, filename)  # adiciona ao topo da lista
    session['ultimos_livros'] = ultimos[:5]  # mantém apenas os 5 últimos

    return redirect(url_for('livros', filename=filename))

@app.route('/ultimos')
def mostrar_ultimos():
    ultimos = session.get('ultimos_livros', [])
    
    nomes_livros = {
        'livro1.pdf': 'Algoritmos e Lógica de Programação',
        'livro2.pdf': 'Python Para Iniciantes',
        'livro3.pdf': 'Informática Básica',
        'livro4.pdf': 'Linux Completo',
        'livro5.pdf': 'Redes de Computadores',
        'livro6.pdf': 'Lógica de Programação em Java',
        'livro7.pdf': 'Montagem de Computadores',
        'livro8.pdf': 'Computação em Nuvem',
        'livro9.pdf': 'Estrutura de Dados',
        'livro10.pdf': 'Tecnologia da Informação e Comunicação',
        'livro11.pdf': 'Git e GitHub',
        'livro12.pdf': 'Kanban em 10 Passos',
        'livro13.pdf': 'Scrum e XP direto das Trincheiras',
        'livro14.pdf': 'Inteligência Artificial',
        'livro15.pdf': 'E-book DevOps',
        'livro16.pdf': 'Introdução a Computação Grafica',
        'livro17.pdf': 'Sistemas Embarcados',
        'livro18.pdf': 'Introdução a Testes de Softwares',
        'livro19.pdf': 'Arquitetura e Organização de Computadores',
        'livro20.pdf': 'Métodos Ágeis',
    }
    
    # Cria uma lista de dicionários com arquivo e nome do livro para o template
    livros_completos = []
    for arquivo in ultimos:
        nome = nomes_livros.get(arquivo, arquivo)  # Se não achar o nome, usa o nome do arquivo
        livros_completos.append({'arquivo': arquivo, 'nome': nome})

    return render_template('ultimos.html', ultimos=livros_completos)

if __name__ == '__main__':
    app.run(debug=True)

