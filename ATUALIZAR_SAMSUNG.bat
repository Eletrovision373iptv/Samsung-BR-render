@echo off
title Robo Samsung TV - Eletrovision
cls

echo ======================================================
echo    INICIANDO ATUALIZACAO SAMSUNG TV PLUS (BR)
echo ======================================================
echo.

:: ENTRA NA PASTA DA SAMSUNG
cd /d "C:\Users\Uso\Desktop\samsung BR"

:: 1. GERA A LISTA
echo [PASSO 1/3] Gerando lista Samsung M3U...
python gerar_samsung.py

:: 2. SALVA NO GIT
echo.
echo [PASSO 2/3] Gravando mudancas...
git add .
git commit -m "Atualizacao Samsung TV"

:: 3. ENVIA PARA O GITHUB
echo.
echo [PASSO 3/3] Enviando para o GitHub...
git push origin main --force

echo.
echo ======================================================
echo    SUCESSO! Painel Samsung Atualizado.
echo ======================================================
pause