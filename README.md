# LoginTestLab:
## O projeto começou como um experimento em Python utilizando Selenium, com o objetivo de estudar automação de páginas web e interação com formulários de login em um ambiente autorizado.

### Na primeira versão (v0.1.0), foi desenvolvido um script simples capaz de:

.Inicializar o navegador Chrome automaticamente;                                                                                 
.Acessar uma página de login;                                                                                                                        
.Localizar os campos de usuário e senha;                                                                                                                                                                  
.Preencher os campos automaticamente;                                                                                                                                                                  
.Gerar combinações numéricas para testes;                                                                                                                                                                  
.Enviar o formulário;                                                                                                                                                                  
.Verificar o resultado da autenticação através da URL;                                                                                                                                                                  
.Encerrar o navegador ao finalizar a execução.                                                                                                                                                                  
### 1. Configura o navegador de teste
```bash
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
URL_LOGIN = ""  
COMBINACOES_SENHA = []
USER = "2026130028"
```
