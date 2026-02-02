# Entrar na pasta do repositório
cd /caminho/para/seu/repositorio   # <–– troque para o caminho real

# Se quiser usar o branch main em vez de master:
git branch -M main

# Inicializar Git LFS
git lfs install

# Registrar padrões de arquivos grandes
git lfs track "ANALISE_DADOS/*.csv"
git lfs track "ANALISE_DADOS/*.ipynb"

# Adicionar .gitattributes
git add .gitattributes
git commit -m "setup: configure git-lfs para dados e notebooks grandes"

# Remover do índice arquivos grandes já commitados, se aplicável
git rm --cached ANALISE_DADOS/cancelamentos.csv
git rm --cached ANALISE_DADOS/Analise_dados.ipynb
git rm --cached ANALISE_DADOS/gabarito.ipynb
git commit -m "chore: remover arquivos grandes do índice para migrar via LFS"

# Adicionar todo o restante dos arquivos
git add .
git commit -m "feat: adicionar código, notebooks leves e estrutura do projeto"

# Adicionar remote, caso ainda não tenha
git remote add origin https://github.com/EssenceGiT/PYTHON_HASHTAG.git

# Dar push para o GitHub
git push -u origin main
