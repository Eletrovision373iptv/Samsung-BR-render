import requests

def gerar():
    print("Baixando lista Samsung Brasil via APSATTV...")
    # Link exato que você encontrou
    url = "https://www.apsattv.com/ssungbra.m3u"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()
        
        # O site entrega o conteúdo bruto da lista
        conteudo = response.text

        if "#EXTM3U" in conteudo:
            with open("lista.m3u", "w", encoding="utf-8") as f:
                f.write(conteudo)
            print("✅ Sucesso! Arquivo lista.m3u atualizado com dados do APSATTV.")
        else:
            print("❌ O link não retornou uma lista válida (M3U).")

    except Exception as e:
        print(f"❌ Erro ao baixar: {e}")

if __name__ == "__main__":
    gerar()