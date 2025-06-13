# Biblioteca do T.I

Este projeto é um sistema de biblioteca online desenvolvido como parte do curso da Faculdade Martha Falcão Wyden.  
Autores: **Kristhiam Soares Santana** e **João Carllos Abreu Fariá**.

## 📚 Sobre o Projeto

O sistema permite a visualização e leitura de livros técnicos em formato digital, focados na área de Tecnologia da Informação (TI). Os livros são organizados com capas, títulos e links diretos para visualização em PDF. Há também um botão flutuante que permite alternar entre os livros disponíveis e os últimos livros abertos.

## 🖥️ Requisitos para execução no Linux

Para executar este projeto localmente no Linux, será necessário:

- Python 3.8 ou superior
- Pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- Flask

### ⚙️ Instruções de instalação e execução

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio

# (Opcional) Crie e ative um ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instale as dependências
pip install flask

# Execute a aplicação
python app.py
```

## 📁 Estrutura do Projeto

```
📂 projeto/
├── app.py
├── livros/
│   ├── index.html
│   └── ultimos.html
├── organ/
│   ├── imagens/
│   ├── csss/
│   └── bootstrap/
├── telas/
│   ├── imagens/
│   ├── csss/
└── README.md
```

## 🚀 Funcionalidades

- Visualização de livros com capas e títulos
- Leitura em PDF em nova aba
- Botão flutuante para alternar entre páginas
- Design responsivo com Bootstrap

---

Projeto acadêmico - Faculdade Martha Falcão Wyden  
Desenvolvido por Kristhiam Soares Santana e João Carllos Abreu Fariá