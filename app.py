from flask import Flask, render_template, send_from_directory, session, redirect, url_for

app = Flask(__name__, template_folder='telas', static_folder='organ')

app.secret_key = '123456'  # necessária para sessões

# Rota para página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para servir PDFs da pasta livros
@app.route('/livros/<path:filename>')
def livros(filename):
    return send_from_directory('livros', filename)

# Rota para abrir livro e guardar nos últimos abertos
@app.route('/abrir/<filename>')
def abrir_livro(filename):
    ultimos = session.get('ultimos_livros', [])

    if filename in ultimos:
        ultimos.remove(filename)
    ultimos.insert(0, filename)
    ultimos = ultimos[:5]  # mantém só os 5 últimos
    session['ultimos_livros'] = ultimos

    return redirect(url_for('livros', filename=filename))

# Rota para mostrar últimos livros abertos
@app.route('/ultimos')
def mostrar_ultimos():
    ultimos = session.get('ultimos_livros', [])
    return render_template('ultimos.html', ultimos=ultimos)

if __name__ == '__main__':
    app.run(debug=True)
