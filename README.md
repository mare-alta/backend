# atualizar o dev
python manage.py makemigrations
python manage.py migrate

#Entrar e criar o projeto no heroku

#acessar o projeto criado
heroku git:remote -a PROJETO

#commitar e fazer o deploy
git add .
git commit -m "Deploy da aplicação"
git push -u heroku master

# atualizar o prod
heroku run python manage.py migrate