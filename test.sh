python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd tienda
./manage.py makemigrations api
./manage.py migrate
./manage.py test --parallel
cd ..
deactivate