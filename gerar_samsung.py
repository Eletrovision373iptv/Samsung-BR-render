import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil...")
    try:
        # Fonte estável de JSON para Samsung BR
        data = requests.get("https://i.mjh.nz/SamsungTVPlus/br.json").json()
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write("#EXTM3U\n")
            for id, c in data['channels'].items():
                f.write(f'#EXTINF:-1 tvg-id="{id}" tvg-logo="{c["logo"]}" group-title="SAMSUNG TV PLUS",{c["name"]}\n')
                f.write(f'{c["url"]}\n')
        print("✅ Arquivo lista.m3u da Samsung gerado!")
    except Exception as e:
        print(f"❌ Erro ao gerar Samsung: {e}")

if __name__ == "__main__":
    gerar()