from flask import Flask, jsonify
import random

app = Flask(__name__)

nomes = [
    "Tyler", "Brandon", "Ethan", "Logan", "Cameron", "Jordan", "Hunter", "Dylan",
    "Connor", "Kyle", "Jaden", "Aiden", "Zachary", "Caleb", "Austin", "Ryan",
    "Chase", "Nathan", "Jason", "Cole",
    "José", "Luis", "Carlos", "Jesús", "Miguel", "Eduardo", "Andrés", "Diego",
    "Javier", "Héctor", "Fernando", "Ramón", "Raúl", "Emilio", "Manuel", "César",
    "Marco", "Iván", "Cristian", "Ricardo"
]

sobrenomes = [
    "Johnson", "Smith", "Brown", "Williams", "Taylor", "Anderson", "Miller", "Moore",
    "Clark", "Hall", "Young", "Hill", "Scott", "Green", "Evans", "Walker",
    "Allen", "Wright", "Mitchell", "Campbell",
    "Hernández", "García", "Martínez", "Rodríguez", "López", "Pérez", "Sánchez", "Ramírez",
    "Torres", "Flores", "Vargas", "Cruz", "Gutiérrez", "Reyes", "Castillo", "Morales",
    "Navarro", "Jiménez", "Ramos", "Mendoza"
]

nacionalidades = [
    "🇺🇸 Estados Unidos", "🇨🇦 Canadá", "🇲🇽 México"
]

posicoes = [
    "Goleiro", "Zagueiro Central", "Lateral Direito", "Lateral Esquerdo",
    "Volante", "Meia Central", "Meia Ofensivo", "Ponta Direita",
    "Ponta Esquerda", "Centroavante"
]

comparacoes = [
    "Christian Pulisic", "Alphonso Davies", "Weston McKennie", "Jonathan David",
    "Tyler Adams", "Ricardo Pepi", "Gio Reyna", "Brenden Aaronson",
    "Jesús Ferreira", "Kellyn Acosta", "Tim Weah", "Miles Robinson",
    "Héctor Herrera", "Carlos Vela", "Chicharito Hernández", "Memo Ochoa"
]

cap_atual = [
    "Reserva na NLEDF", "Titular em clube pequeno da NLEDF", "Titular em clube médio da NLEDF",
    "Reserva em grande clube da NLEDF"
]

cap_potencial = [
    "Titular em clube médio da NLEDF", "Titular em grande clube da NLEDF",
    "Estrela na NLEDF", "Transferência para elite europeia"
]

@app.route("/api/jogador", methods=["GET"])
def gerar_jogador():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    nacionalidade = random.choices(
        nacionalidades,
        weights=[60, 20, 20],  # EUA tem mais chance
        k=1
    )[0]
    posicao = random.choice(posicoes)
    comparacao = random.choice(comparacoes)
    atual = random.choice(cap_atual)
    potencial = random.choice(cap_potencial)

    # Distribuição das estrelas
    chance = random.randint(1, 100)
    if chance <= 10:
        estrelas = 5
    elif chance <= 35:
        estrelas = 4
    elif chance <= 70:
        estrelas = 3
    else:
        estrelas = 2

    estrelas_str = "<:sstar:1214063700886036532>" * estrelas

    return jsonify({
        "nome": f"{nome} {sobrenome}",
        "nacionalidade": nacionalidade,
        "posição": posicao,
        "comparação": comparacao,
        "capacidade_atual": atual,
        "capacidade_potencial": potencial,
        "estrelas": estrelas_str
    })

if __name__ == "__main__":
    app.run(debug=True)

