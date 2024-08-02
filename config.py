import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "26172374"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "49e1836f52025eca17961a8b1c837418")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sifan9sifan9:4qdAGPpbYuNXW4cv@cluster0.gowtahu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
