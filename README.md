# 📩 ClassifyEat API

API desenvolvida em **FastAPI** para classificação de mensagens
utilizando modelos da **OpenAI**. A aplicação recebe uma mensagem, envia
para um modelo LLM com um prompt específico e retorna a classificação
estruturada em JSON.

------------------------------------------------------------------------

## 🚀 Tecnologias Utilizadas

-   Python 3.10+
-   FastAPI
-   Pydantic v2
-   OpenAI API
-   Uvicorn
-   python-dotenv

------------------------------------------------------------------------

## 📂 Estrutura do Projeto

``` text
.venv
data
src/
├── api/
│   └── Routes.py
├── models/
│   └── Schemas.py
├── prompts/
│   └── prompt.txt
├── services/
│   └── ClassificationService.py
├── main.py
.env
README.md
requirements.txt
```

------------------------------------------------------------------------

## ⚙️ Instalação

### 1️⃣ Clone o repositório

``` bash
git clone https://github.com/eloisapsl/DesafioTakeat.git
cd DesafioTakeat
```

### 2️⃣ Crie e ative o ambiente virtual

``` bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 🔑 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

``` env
API_KEY=sua_chave_da_openai
```

------------------------------------------------------------------------

## ▶️ Executando a aplicação

``` bash
uvicorn src.main:app --reload
```

A API ficará disponível em:

    http://127.0.0.1:8000

------------------------------------------------------------------------

## 📚 Documentação Automática

O FastAPI gera documentação interativa automaticamente:

-   Swagger UI:\
    👉 `http://127.0.0.1:8000/docs`

-   ReDoc:\
    👉 `http://127.0.0.1:8000/redoc`

------------------------------------------------------------------------

## 📡 Endpoint de Classificação

### POST `/classify`

Classifica uma mensagem enviada pelo usuário.

#### 📥 Request Body

``` json
{
  "message": "Olá, gostaria de saber o status do meu pedido"
}
```

#### 📤 Response (200)

``` json
{
  "category": "PEDIDO_CARDAPIO",
  "confidence": 0.92
}
```

------------------------------------------------------------------------

## ❗ Possíveis Erros

  Código   Descrição
  -------- -------------------------------------
  422      Unprocessable Entity

------------------------------------------------------------------------

## 🧪 Exemplo com curl

``` bash
curl -X POST http://127.0.0.1:8000/classify \
     -H "Content-Type: application/json" \
     -d '{"message": "Meu pedido atrasou"}'
```

