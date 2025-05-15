import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import json
import time

def carregar_dados():
    try:
        with open('MeusDados.json', encoding='utf-8') as f:
            MeusDados = json.load(f)
        
        if 'curriculo' in MeusDados:
            caminho = MeusDados['curriculo']['caminho']
            if not os.path.exists(caminho):
                raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
            if not caminho.lower().endswith('.pdf'):
                print("⚠️ Aviso: O arquivo do currículo não é PDF")
        
        return MeusDados
    except json.JSONDecodeError:
        raise ValueError("Erro no formato do arquivo JSON")
    except Exception as e:
        raise Exception(f"Erro ao carregar dados: {str(e)}")

def inject_autofill(driver, MeusDados):
    try:
        script = f"""
        const dados = {json.dumps(MeusDados)};
        
        function detectarCampoCurriculo(element) {{
            const atributos = [
                element.labels?.[0]?.innerText?.toLowerCase() || '',
                element.getAttribute('aria-label')?.toLowerCase() || '',
                element.getAttribute('placeholder')?.toLowerCase() || '',
                element.id?.toLowerCase() || '',
                element.name?.toLowerCase() || ''
            ];
            
            return atributos.some(attr => 
                /curr|curriculo|cv|resume|arquivo|documento/.test(attr)
            );
        }}
        
        function setupAutofill() {{
            document.querySelectorAll('input, textarea, select').forEach(element => {{
                if (element.type === 'file') {{
                    if (detectarCampoCurriculo(element)) {{
                        element.style.border = '2px solid green';
                        console.log('Campo de currículo detectado!');
                    }}
                }}
                
                element.addEventListener('click', function() {{
                    const atributos = [
                        this.labels?.[0]?.innerText?.toLowerCase() || '',
                        this.id?.toLowerCase() || '',
                        this.name?.toLowerCase() || '',
                        this.placeholder?.toLowerCase() || ''
                    ];
                    
                    for (const [key, value] of Object.entries(dados)) {{
                        if (key !== 'curriculo' && 
                            atributos.some(attr => attr.includes(key.toLowerCase()))) {{
                            this.value = value;
                            break;
                        }}
                    }}
                }});
            }});
        }}
        
        setupAutofill();
        new MutationObserver(setupAutofill).observe(
            document.body, {{ childList: true, subtree: true }}
        );
        """
        driver.execute_script(script)
    except Exception as e:
        print(f"Erro ao injetar autopreenchimento: {str(e)}")

def preencher_curriculo(driver, caminho_arquivo):
    try:
        campo_upload = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='file']"))
        )
        
        # Verificação mais robusta
        is_curriculo = driver.execute_script("""
            const element = arguments[0];
            const atributos = [
                element.labels?.[0]?.innerText?.toLowerCase() || '',
                element.getAttribute('aria-label')?.toLowerCase() || '',
                element.getAttribute('placeholder')?.toLowerCase() || '',
                element.id?.toLowerCase() || '',
                element.name?.toLowerCase() || ''
            ];
            return atributos.some(attr => 
                /curr|curriculo|cv|resume|arquivo|documento/.test(attr)
            ;
        """, campo_upload)
        
        if is_curriculo:
            campo_upload.send_keys(os.path.abspath(caminho_arquivo))
            print("✅ Currículo enviado com sucesso!")
            return True
        else:
            print("⚠️ Campo de arquivo encontrado, mas não parece ser para currículo")
            return False
            
    except TimeoutException:
        print("⚠️ Tempo esgotado: Campo de upload não encontrado")
        return False
    except Exception as e:
        print(f"⚠️ Erro inesperado ao enviar currículo: {str(e)}")
        return False

def main():
    try:
        MeusDados = carregar_dados()
        driver = webdriver.Chrome()
        
        try:
            driver.get("https://www.vagas.com.br/cadastrar-curriculo/dados-pessoais")
            
            # Adicione aqui o código de login manual se necessário
            input("⚠️ Faça o login manualmente e pressione Enter para continuar...")
            
            inject_autofill(driver, MeusDados)

            if 'curriculo' in MeusDados:
                print("🔍 Procurando campo de currículo...")
                time.sleep(3)  # Espera para página carregar
                if not preencher_curriculo(driver, MeusDados['curriculo']['caminho']):
                    print("❌ Não foi possível enviar o currículo automaticamente")
                    print("Tente enviar manualmente o arquivo:", MeusDados['curriculo']['caminho'])
            
            input("Pressione Enter para fechar...")
            
        finally:
            driver.quit()
    except Exception as e:
        print(f"❌ Erro fatal: {str(e)}")

if __name__ == "__main__":
    main()