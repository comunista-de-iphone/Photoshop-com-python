# PRIMEIRO COMANDO NO TERMINAL. RESPONSÁVEL POR INSTALAR O PATH VALIDATE: pip install pathvalidate
# SEGUNO COMANDO NO TERMINAL. RESPONSÁVEL POR INSTALAR O PY WIN 32: pip install pywin32
# TERCEIRO COMANDO NO TERMINAL: RESPNSÁVEL POR ATIVAR O SCRIPT: python main.py


# REGRAS DE USO - REGRAS DE USO - REGRAS DE USO - REGRAS DE USO - REGRAS DE USO - REGRAS DE USO - REGRAS DE USO
# NÃO COLOCAR AS CAMADAS QUE SERÃO ALTERADAS PELO SCRIPT EM PASTAS NO PHOTOSHOP
# NÃO USAR PLANILHAS. O ARQUIVO .PS DEVE SER UNICO
# AS VARIAVEIS "textoArray", "camadaArray", "coresArray" E "fundoArray" PRECISAM TER EXATAMENTE O MESMO NOME DAS CAMADAS QUE SERÃO ALTERADAS NO PHOTOSHOP

import os 
from photoshopy import Photoshopy

contador = 1
fontSize = 62
textoArray = [
    ("TEXT HEADLINE", "WHERE THE JOURNEY BEGINS!", "IG"),
    ("TEXT HEADLINE", "WE MAKE DREAMS COME TRUE", "IG"),
    ("TEXT HEADLINE", 'NO MATTER WHERE,\rWE TAKE YOU THERE', "IG"),
    ("TEXT HEADLINE", "A LIFE WITHOUT JOURNEYS\rIS ONE NOT LIVED AT ALL", "IG"),
    ("TEXT HEADLINE", "MAKE YOUR NEXT TRIP AWESOME", "IG"),
    ("TEXT HEADLINE", "TRAVEL CAN OPEN YOUR MIND", "IG"),
    ("TEXT HEADLINE", "WE KNOW THE BEST ROUTES", "IG"),
    ("TEXT HEADLINE", "TRAVEL IS THE BEST TEACHER", "IG"),
    ("TEXT HEADLINE", "THE ART OF TRAVELING HERE", "IG"),
    ("TEXT HEADLINE", "A WORLD OF ADVENTURE\rIS JUST A FLIGHT AWAY", "IG"),
    ("TEXT HEADLINE", "TRAVEL LIKE A KING", "IG"),
]
camadaArray = ["CANADA 1", "CANADA 2", "RJ 1", "AFRICA 2"]
coresArray = ["BLUE", "WHITE", "RED"]
fundoArray = ["DESCONTO"]

app = Photoshopy()
app.openPSD(os.path.abspath("./Photoshop/Viagem_01.psd"))

# ATIVA O FUNDO DA IMAGEM 
for fundoAtivo in fundoArray:
    app.hideShowLayer(fundoAtivo, True)

    # ATIVA A CAMADA CENTRAL DO CRIATIVO
    for ativarCamada in camadaArray:
        app.hideShowLayer(ativarCamada, True)
        print(ativarCamada)

        # ATIVA TODAS AS CORES SEM FILTRO
        for corAtiva in coresArray:
            app.hideShowLayer(corAtiva, True)

            # MUDA O TEXTO E SALVA CRIATIVO
            for layer, msg, namefile in textoArray:
                app.updateLayerText(layer, msg, fontSize)
                app.exportJPEG(namefile + str(contador) + ".jpg", os.path.abspath("./Criativos"))
                contador += 1

            app.hideShowLayer(corAtiva, False)
        app.hideShowLayer(ativarCamada, False)
    app.hideShowLayer(fundoAtivo, False)


# app.closePSD()