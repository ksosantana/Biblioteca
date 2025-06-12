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

# ajuda do chat para naão ocasionar duplicagem de livros, com um erro que eu mesmo tive
    if filename in ultimos:
        ultimos.remove(filename)  

    ultimos.insert(0, filename)  # adiciona ao topo da lista
    session['ultimos_livros'] = ultimos[:5]  # mantém apenas os 5 últimos

    return redirect(url_for('livros', filename=filename))
@app.route('/ultimos')
def mostrar_ultimos():
    ultimos = session.get('ultimos_livros', [])
    return render_template('ultimos.html', ultimos=ultimos)

if __name__ == '__main__':
    app.run(debug=True)
