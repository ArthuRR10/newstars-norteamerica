from flask import Flask, jsonify
from threading import Thread
import random

app = Flask(__name__)

# Nomes comuns nos EUA, Canadá e México
nomes = [
    # EUA / Canadá
    "Tyler", "Brandon", "Ethan", "Logan", "Cameron", "Jordan", "Hunter", "Dylan",
    "Connor", "Kyle", "Jaden", "Aiden", "Zachary", "Caleb", "Austin", "Ryan",
    "Chase", "Nathan", "Jason", "Cole",
    # México / Latinos norte-americanos
    "José", "Luis", "Carlos", "Jesús", "Miguel", "Eduardo", "Andrés", "Diego",
    "Javier", "Héctor", "Fernando", "Ramón", "Raúl", "Emilio", "Manuel", "César",
    "Marco", "Iván", "Cristian", "Ricardo"
]

sobrenomes = [
    # EUA / Canadá
    "Johnson", "Smith", "Brown", "Williams", "Taylor", "Anderson", "Miller", "Moore",
    "Clark", "Hall", "Young", "Hill", "Scott", "Green", "Evans", "Walker",
    "Allen", "Wright", "Mitchell", "Campbell",
    # México / Latinos norte-americanos
    "Hernández", "García", "Martínez", "Rodríguez", "López", "Pérez", "Sánchez", "Ramírez",
    "Torres", "Flores", "Vargas", "Cruz", "Gutiérrez", "Reyes", "Castillo", "Morales",
    "Navarro", "Jiménez", "Ramos", "Mendoza"
]

# Nacionalidades com peso maior para EUA
nacionalidades_pesos = [
    ("🇺🇸 Estados Unidos", 60),
    ("🇲🇽 México", 25),
    ("🇨🇦 Canadá", 15)
]

posicoes = [
    "Goleiro", "Zagueiro", "Lateral Direito", "Lateral Esquerdo", "Volante",
    "Meia Central", "Meia Ofensivo", "Ponta Direita", "Ponta Esquerda", "Centroavante"
]

comparacoes = [
    "Christian Pulisic", "Alphonso Davies", "Weston McKennie", "Gio Reyna", "Jonathan David",
    "Hirving Lozano", "Jesús Ferreira", "Timothy Weah", "Ricardo Pepi", "Santiago Giménez",
    "Tyler Adams", "Brenden Aaronson", "Edson Álvarez", "Diego Lainez", "Cyle Larin"
]

capacidade_atual = [
    "Reserva na Championship", "Titular na Championship",
    "Reserva na NLEDF", "Titular na NLEDF"
]

capacidade_potencial = [
    "Titular na Championship", "Reserva na NLEDF", "Titular na NLEDF",
    "Reserva em time de Champions League", "Titular em time de Champions League"
]

# Estrelas: chance maior para 4 ou 5
estrelas_pesos = [(2, 5), (3, 20), (4, 45), (5, 30)]

@app.route('/')
def gerar_jogador():
    nome = f"{random.choice(nomes)} {random.choice(sobrenomes)}"
    nacionalidade = random.choices(
        [n[0] for n in nacionalidades_pesos],
        weights=[n[1] for n in nacionalidades_pesos]
    )[0]
    posicao = random.choice(posicoes)
    comparacao = random.choice(comparacoes)
    atual = random.choice(capacidade_atual)
    potencial = random.choice(capacidade_potencial)
    estrelas = random.choices(
        [e[0] for e in estrelas_pesos],
        weights=[e[1] for e in estrelas_pesos]
    )[0]
    estrelas_txt = "<:sstar:1214063700886036532>" * estrelas

    return jsonify({
        "nome": nome,
        "nacionalidade": nacionalidade,
        "posicao": posicao,
        "comparacao": comparacao,
        "cap_atual": atual,
        "cap_potencial": potencial,
        "estrelas": estrelas_txt
    })

def run():
    app.run(host='0.0.0.0', port=8080)

Thread(target=run).start()

