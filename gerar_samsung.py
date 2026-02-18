import requests

def gerar():
    print("Buscando lista no site APSATTV...")
    # URL da lista específica (geralmente eles usam arquivos .m3u ou .txt)
    # Se você viu a lista em uma página específica, coloque a URL dela abaixo:
    url = "https://apsattv.com/samsungbr.m3u" 
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        
        # Se o link acima der 404, tentaremos o link principal de listas deles
        if response.status_code == 404:
            print("Link direto não encontrado, tentando buscar na raiz do site...")
            url = "https://apsattv.com/streams.txt" # Outro formato comum deles
            response = requests.get(url, headers=headers, timeout=30)

        response.raise_for_status()
        
        # Salva o resultado
        with open("lista.m3u", "w", encoding="utf-8") as f:
            # Se o site devolver HTML em vez de M3U, precisaremos filtrar, 
            # mas se for o arquivo de stream, salvamos direto:
            f.write(response.text)
            
        print("✅ Sucesso! Lista extraída do APSATTV e salva.")
        
    except Exception as e:
        print(f"❌ Erro ao acessar APSATTV: {e}")

if __name__ == "__main__":
    gerar()