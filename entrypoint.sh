#!/bin/bash

echo "➡️ Aplicando migrações..."
python manage.py migrate --noinput

echo "➡️ Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "➡️ Criando superusuário, se necessário..."
python create_superuser.py

echo "✅ Iniciando Gunicorn..."
exec gunicorn igreja_manager.wsgi:application --bind 0.0.0.0:$PORT
