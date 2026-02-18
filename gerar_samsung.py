import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil...")
    # Link atualizado e headers para evitar bloqueio
    url = "https://i.mjh.nz/SamsungTVPlus/br.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status() # Verifica se o site respondeu 200 OK
        data = response.json()
        
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for id, c in data['channels'].items():
                f.write(f'#EXTINF:-1 tvg-id="{id}" tvg-logo="{c["logo"]}" group-title="SAMSUNG TV PLUS",{c["name"]}\n')
                f.write(f'{c["url"]}\n')
        print("✅ Arquivo lista.m3u da Samsung gerado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao gerar Samsung: {e}")

if __name__ == "__main__":
    gerar()