import requests
import re

def gerar():
    print("Buscando canais Samsung TV Plus Brasil (Modo Direto)...")
    url = "https://i.mjh.nz/SamsungTVPlus/br.m3u8"
    
    try:
        response = requests.get(url, timeout=20)
        response.raise_for_status()
        conteudo = response.text

        # Salva o arquivo diretamente fazendo pequenos ajustes de nome
        with open("lista.m3u", "w", encoding="utf-8") as f:
            # Ajusta o group-title para ficar bonito no seu painel
            f.write(conteudo.replace('group-title="', 'group-title="SAMSUNG - '))
            
        print(f"✅ Sucesso! Lista gerada a partir da fonte M3U8 oficial.")
    except Exception as e:
        print(f"❌ Erro crítico: {e}")
        print("DICA: Tente abrir este link no seu navegador: https://i.mjh.nz/SamsungTVPlus/br.m3u8")

if __name__ == "__main__":
    gerar()