# ChatBot do Ayrton

ChatBot inteligente criado com Streamlit e OpenAI GPT-3.5.

## Como usar localmente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Configure sua chave da OpenAI em `.streamlit/secrets.toml`:
```toml
OPENAI_API_KEY = "sua-chave-aqui"
```

3. Execute o app:
```bash
streamlit run othercode.py
```

## Deploy no Streamlit Cloud

1. Faça fork/clone deste repositório
2. Vá em [share.streamlit.io](https://share.streamlit.io)
3. Conecte seu repositório GitHub
4. Em Settings → Secrets, adicione:
```
OPENAI_API_KEY = "sua-chave-aqui"
```
5. Deploy!
