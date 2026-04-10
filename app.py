from flask import Flask, render_template, request

app = Flask(__name__)

mensagens = []

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        mensagem = request.form.get("mensagem")
        if mensagem:
            mensagens.append(mensagem)
    return """
    <h1>Chat Simples</h1>
    <form method="POST">
        <input name="mensagem" placeholder="Digite sua mensagem">
        <button type="submit">Enviar</button>
    </form>
    <ul>
        """ + "".join(f"<li>{m}</li>" for m in mensagens) + """
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)
