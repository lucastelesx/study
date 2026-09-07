import requests

def buscar_preco_bitcoin():
    # Usando a AwesomeAPI (mais estável para conexões no Brasil)
    url = "https://economia.awesomeapi.com.br/last/BTC-USD"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        dados = response.json()
        
        # O formato dessa API é um pouco diferente
        preco = dados['BTCUSD']['bid']
        print(f"✅ Conexão OK! Preço do Bitcoin (AwesomeAPI): ${preco}")
        
    except Exception as e:
        print(f"❌ Erro ao acessar AwesomeAPI: {e}")

if __name__ == "__main__":
    buscar_preco_bitcoin()