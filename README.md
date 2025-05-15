# Preenchimento Automático de Currículos (`ProjetoCurriculum`)
![GifTesteDeApi](https://github.com/user-attachments/assets/5dc68729-97ea-4147-9b0c-70187585f232)

# Preenchimento Automático de Currículos (`ProjetoCurriculum`)

<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="60" height="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/json/json-original.svg" alt="JSON" width="60" height="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" alt="Selenium" width="60" height="60"/>
</p>

---

## 🛠️ Linguagens e Ferramentas Utilizadas | Languages and Tools Used

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python" width="20" height="20"/> **Python**  
  - _Linguagem principal do projeto, utilizada para automação e manipulação de dados._  
  - _Main language of the project, used for automation and data handling._

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/json/json-original.svg" alt="JSON" width="20" height="20"/> **JSON**  
  - _Formato utilizado para armazenar e organizar os dados pessoais do usuário._  
  - _Format used to store and organize user personal data._

- <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" alt="Selenium" width="20" height="20"/> **Selenium WebDriver**  
  - _Ferramenta para automação de navegadores web, responsável por preencher os formulários automaticamente._  
  - _Tool for web browser automation, responsible for automatically filling out forms._

---

[English below 🇺🇸]




## 📄 Descrição

Este projeto automatiza o preenchimento de formulários de cadastro de currículos em sites de vagas de emprego, utilizando Python, Selenium WebDriver e um arquivo JSON com seus dados pessoais. O objetivo é economizar tempo e evitar erros ao preencher repetidamente os mesmos dados em diferentes plataformas.

---

## 🚀 Funcionalidades

- **Leitura automática de dados pessoais** a partir de um arquivo `MeusDados.json`.
- **Preenchimento automático** de campos de formulários em sites de emprego.
- **Upload automático do currículo** em PDF.
- **Detecção inteligente** dos campos corretos para cada informação.
- **Mensagens de status e erros** claras no terminal.

---

## 🛠️ Como usar

1. **Clone o repositório:**
   ```sh
   git clone https://github.com/seu-usuario/ProjetoCurriculum.git
   cd ProjetoCurriculum
   ```

2. **Instale as dependências:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Edite o arquivo `MeusDados.json`** com seus dados pessoais e o caminho do seu currículo em PDF.

4. **Execute o script:**
   ```sh
   python Autocomplete.py
   ```

5. **Faça login manualmente** quando solicitado e pressione Enter para continuar.

---

## 📁 Estrutura dos Arquivos

```
ProjetoCurriculum/
├── Autocomplete.py
├── MeusDados.json
├── requirements.txt
└── README.md
```

---

## ⚠️ Avisos de Segurança

- **Nunca compartilhe seu arquivo `MeusDados.json` publicamente**, pois ele pode conter informações sensíveis.
- **Não armazene senhas reais** ou dados confidenciais em repositórios públicos.

---

## 📋 Exemplo de `MeusDados.json`

```json
{
  "nome": "Seu Nome",
  "sobrenome": "Seu Sobrenome",
  "email": "seu@email.com",
  "telefone": "999999999",
  "curriculo": {
    "caminho": "C:/Users/usuario/Documents/Curriculo.pdf"
  }
}
```

---

# 🇺🇸 English Version

## 📄 Description

This project automates the process of filling out resume registration forms on job sites, using Python, Selenium WebDriver, and a JSON file with your personal data. The goal is to save time and avoid errors when repeatedly entering the same information on different platforms.

---

## 🚀 Features

- **Automatic reading of personal data** from `MeusDados.json`.
- **Autofill** of form fields on job websites.
- **Automatic upload of your PDF resume**.
- **Smart detection** of the correct fields for each piece of information.
- **Clear status and error messages** in the terminal.

---

## 🛠️ How to Use

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-user/ProjetoCurriculum.git
   cd ProjetoCurriculum
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Edit the `MeusDados.json` file** with your personal data and the path to your PDF resume.

4. **Run the script:**
   ```sh
   python Autocomplete.py
   ```

5. **Log in manually** when prompted and press Enter to continue.

---

## 📁 File Structure

```
ProjetoCurriculum/
├── Autocomplete.py
├── MeusDados.json
├── requirements.txt
└── README.md
```

---

## ⚠️ Security Warnings

- **Never share your `MeusDados.json` file publicly**, as it may contain sensitive information.
- **Do not store real passwords** or confidential data in public repositories.

---

## 📋 Example `MeusDados.json`

```json
{
  "nome": "Your Name",
  "sobrenome": "Your Last Name",
  "email": "your@email.com",
  "telefone": "999999999",
  "curriculo": {
    "caminho": "C:/Users/youruser/Documents/Curriculo.pdf"
  }
}
```

---

## 📝 Licença | License

Este projeto está sob a licença MIT.  
This project is licensed under the MIT License.
