# Prova de Programação Web em python 

# 📦 Projeto Python

Este projeto foi desenvolvido em Python e utiliza um ambiente virtual (`venv`). Siga os passos abaixo para clonar e executar localmente.

---

## 🚀 Como rodar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/MaurilioSemeao/pythom_get_post.git
cd pythom_get_post
```

### 2. Crie e ative o ambiente virtual

#### Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

#### Windows (CMD):

```cmd
python -m venv venv
venv\Scripts\activate
```

#### Windows (PowerShell):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

> 🔗 Dica: Use o **mesmo nome** (`venv`) para que o `.gitignore` funcione corretamente.

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Verifique se está tudo funcionando

Execute o script principal ou rode os testes:

```bash
python app.py
# ou
pytest
```

### 5. Verifique se o ambiente está ativo corretamente

```bash
which python  # Linux/macOS
# ou
where python  # Windows
```

Deve retornar algo como:

```
/caminho/para/seu/projeto/venv/bin/python
```

---

## 🧼 Como manter o projeto limpo

### Ignorar arquivos desnecessários

Certifique-se de que o arquivo `.gitignore` contém:

```gitignore
venv/
.venv/
__pycache__/
*.py[cod]
Scripts/
Lib/
```

### Atualizar `requirements.txt` ao adicionar novas dependências

```bash
pip freeze > requirements.txt
```

---

## 📁 Estrutura esperada

```bash
python_get_post/
├── venv/               # Ambiente virtual (ignorado)
├── app.py              # Arquivo principal
├── calc_2grau.py       # Arquivo da função calcula equação 2º grau
├── faherenheit.py      # Aquivo da função que converte celcius para fahernheit
├── requirements.txt    # Dependências
└── README.md           # Este guia
```

---

## 🧑‍💻 Autor

Maurilio


