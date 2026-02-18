import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil...")
    # URL ATUALIZADA (EPG.PW é uma fonte muito estável)
    url = "https://itv.as/samsung_br.json" 
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 404:
            # Tenta uma segunda fonte caso a primeira falhe
            url = "https://raw.githubusercontent.com/fgl666/Grades/main/SamsungTVPlusBR.json"
            response = requests.get(url, headers=headers)
            
        response.raise_for_status()
        data = response.json()
        
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            # Ajuste dependendo da estrutura do JSON da nova fonte
            channels = data.get('channels', data) 
            for id, c in channels.items():
                f.write(f'#EXTINF:-1 tvg-id="{id}" tvg-logo="{c.get("logo")}" group-title="SAMSUNG TV PLUS",{c.get("name")}\n')
                f.write(f'{c.get("url")}\n')
        print("✅ Arquivo lista.m3u da Samsung gerado!")
    except Exception as e:
        print(f"❌ Erro ao gerar Samsung: {e}")

if __name__ == "__main__":
    gerar()