import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil (Fonte Taws)...")
    # Link direto da Taws para Samsung Brasil
    url = "https://www.taws.com.br/iptv/samsung.m3u"
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        
        # Vamos limpar a lista para garantir que o formato fique perfeito para o seu site
        conteudo = response.text
        
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write(conteudo)
            
        print(f"✅ Sucesso! Lista Samsung gerada com a fonte Taws.")
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    gerar()