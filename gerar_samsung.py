import requests

def gerar():
    print("Baixando lista Samsung Brasil via APSATTV...")
    url = "https://www.apsattv.com/ssungbra.m3u"
    
    # Headers completos para o site pensar que é o VLC ou um Navegador
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # Pegamos o conteúdo bruto
        conteudo = response.text.strip()

        # Salvamos direto, sem frescura. Se o VLC lê, o seu site vai ler.
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write(conteudo)
            
        print("✅ Sucesso! O arquivo lista.m3u foi sobrescrito com os dados do APSATTV.")

    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    gerar()