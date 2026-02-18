import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil...")
    
    # Lista de fontes possíveis (se uma cair, ele tenta a outra)
    fontes = [
        "https://raw.githubusercontent.com/fgl666/Grades/main/SamsungTVPlusBR.json",
        "https://i.mjh.nz/SamsungTVPlus/br.json"
    ]
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    sucesso = False

    for url in fontes:
        try:
            print(f"Tentando fonte: {url}")
            response = requests.get(url, headers=headers, timeout=15)
            if response.status_code == 200:
                data = response.json()
                
                # O JSON pode vir direto ou dentro de uma chave 'channels'
                canais = data.get('channels', data) if isinstance(data, dict) else {}
                
                if canais:
                    with open("lista.m3u", "w", encoding="utf-8") as f:
                        f.write("#EXTM3U\n")
                        for id, c in canais.items():
                            nome = c.get('name', 'Canal Samsung')
                            logo = c.get('logo', '')
                            link = c.get('url', '')
                            if link:
                                f.write(f'#EXTINF:-1 tvg-id="{id}" tvg-logo="{logo}" group-title="SAMSUNG TV PLUS",{nome}\n')
                                f.write(f'{link}\n')
                    print(f"✅ Sucesso! Lista gerada com {len(canais)} canais.")
                    sucesso = True
                    break
        except Exception as e:
            print(f"⚠️ Fonte falhou: {e}")

    if not sucesso:
        print("❌ Todas as fontes falharam. Verifique sua internet.")

if __name__ == "__main__":
    gerar()