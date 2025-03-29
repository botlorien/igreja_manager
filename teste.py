import cloudinary
import cloudinary.uploader
import cloudinary.api

import os

# Carrega variáveis de ambiente (ou substitua pelos valores diretamente para teste)
cloudinary.config(
  cloud_name=os.getenv('CLOUDINARY_CLOUD_NAME'),
  api_key=os.getenv('CLOUDINARY_API_KEY'),
  api_secret=os.getenv('CLOUDINARY_API_SECRET')
)

# Caminho de um arquivo qualquer (imagem ou PDF)
file_path = 'media/imagens_igrejas/th.jpg'  # ou 'teste.pdf'

try:
    result = cloudinary.uploader.upload(file_path)
    print("✅ Upload feito com sucesso!")
    print("📎 URL do arquivo:", result['secure_url'])
except Exception as e:
    print("❌ Erro ao tentar enviar para o Cloudinary:")
    print(e)
