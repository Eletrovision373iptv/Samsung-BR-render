import requests

def gerar():
    print("Buscando canais Samsung TV Plus Brasil (Fonte Kodi Brasil)...")
    # Link direto e funcional
    url = "https://kodibrasil.net/lista/samsung.m3u"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    try:
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()
        
        # Salva o arquivo baixado
        with open("lista.m3u", "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print(f"✅ Sucesso! Lista Samsung gerada (Fonte: Kodi Brasil).")
    except Exception as e:
        print(f"⚠️ Fonte 1 falhou, tentando fonte reserva...")
        try:
            # Fonte Reserva
            url2 = "https://raw.githubusercontent.com/Lazzarotto-oficial/Lazzarotto-oficial/main/SAMSUNG_TV_PLUS.m3u"
            res2 = requests.get(url2, headers=headers, timeout=20)
            res2.raise_for_status()
            with open("lista.m3u", "w", encoding="utf-8") as f:
                f.write(res2.text)
            print("✅ Sucesso com a fonte reserva!")
        except:
            print(f"❌ Erro crítico: {e}")

if __name__ == "__main__":
    gerar()