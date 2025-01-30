from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/bot", methods=["POST"])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    msg = response.message()

    # Dicionário de perguntas e respostas
    respostas = {
        "quantos litros de óleo de motor a freemont usa": "A Freemont usa 4,75 litros de óleo de motor.",
        "qual óleo de motor especificado": "O óleo recomendado é 5W30 API/SN.",
        "quantos litros de óleo de câmbio a freemont usa": "Troca completa: 9 Litros (Flush), troca parcial por gravidade: 6,5 Litros.",
        "qual óleo de câmbio especificado": "Use sempre ATF+4, NÃO utilizar outra especificação.",
        "quantos litros de aditivo de arrefecimento a freemont usa": "A Freemont usa 11 litros de aditivo de arrefecimento.",
        "qual fluido de freio recomendado": "O fluido de freio recomendado é DOT 4, mas troque no circuito completo.",
        "quais são os limites máximos de temperatura": (
            "Limites máximos de temperatura:\n"
            "Radiador: 110°C\n"
            "Óleo Motor: 120°C\n"
            "Óleo Câmbio: 120°C"
        ),
        "qual bateria utilizar": "Bateria 60 Ah, polo positivo invertido ou esquerdo.",
        "manutenção preventiva": (
            "🔧 **Manutenção preventiva:**\n"
            "- Troque os 2 Ts do ar quente e o T do radiador se necessário (após 50.000 km).\n"
            "- Se o reservatório de expansão borbulhar, troque a tampa metálica do radiador.\n"
            "- Se a temperatura da água ultrapassar 110°C, verifique as válvulas termostáticas (são 2).\n"
            "- Verifique o óleo de câmbio regularmente (deve estar vermelho e na quantidade correta).\n"
            "- Não siga o manual para troca do óleo de câmbio, reduza o intervalo pela metade! 🚗💨"
        ),
    }

    # Verifica se a pergunta corresponde a alguma resposta no dicionário
    resposta_encontrada = None
    for pergunta, resposta in respostas.items():
        if pergunta in incoming_msg:
            resposta_encontrada = resposta
            break

    # Enviar resposta correspondente ou mensagem padrão se não encontrar
    if resposta_encontrada:
        msg.body(resposta_encontrada)
    else:
        msg.body("Desculpe, não entendi. Pergunte algo como: 'óleo de motor', 'óleo de câmbio', 'manutenção preventiva'.")

    return str(response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
