import requests

def gerar():
    print("Buscando Samsung TV Plus (Link Direto GitHub)...")
    # Este link está dentro do GitHub, o seu PC não vai bloquear.
    url = "https://raw.githubusercontent.com/Lazzarotto-oficial/Lazzarotto-oficial/main/SAMSUNG_TV_PLUS.m3u"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print("✅ Sucesso! Lista Samsung gerada via GitHub.")
    except Exception as e:
        print(f"❌ Erro ao acessar GitHub: {e}")

if __name__ == "__main__":
    gerar()