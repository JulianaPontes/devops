FROM python:3.10

# Diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos para o container
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt || true

# Porta que a aplicação vai usar (exemplo: 5000)
EXPOSE 5000

# Comando correto para rodar o app
CMD ["python", "app.py"]