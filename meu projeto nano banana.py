import os
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configuração da API do Nano Banana
# DICA: Guarde sua chave em variáveis de ambiente, nunca direto no código!
NANO_BANANA_API_KEY = os.environ.get("NANO_BANANA_API_KEY", "sua_chave_aqui")
NANO_BANANA_URL = "https://nanobanana.ai"  # Exemplo de endpoint padrão


@app.route('/api/gerar-imagem', methods=['POST'])
def gerar_imagem():
    data = request.get_json()
    prompt_usuario = data.get('prompt')

    if not prompt_usuario:
        return jsonify({"error": "O prompt é obrigatório"}), 400

    # Estrutura de payload para o Nano Banana Pro (2K)
    headers = {
        "Authorization": f"Bearer {NANO_BANANA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "nano-banana-pro",
        "prompt": prompt_usuario,
        "width": 2048,  # Resolução 2K
        "height": 2048,  # Resolução 2K
        "n": 1  # 1 imagem por vez (custa ~US$ 0,139)
    }

    try:
        # Faz a chamada para a API externa
        response = requests.post(NANO_BANANA_URL, json=payload, headers=headers)
        response_data = response.json()

        # Retorna o link da imagem gerada para o seu site frontend
        return jsonify(response_data), response.status_code

    except Exception as e:
        return jsonify({"error": f"Erro na conexão: {str(e)}"}), 500


if __name__ == '__main__':
    # Roda o servidor local na porta 5000
    app.run(port=5000, debug=True)
