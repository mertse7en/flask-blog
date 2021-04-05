## Installation
pip install virtualenv
virtualenv venv
cd .\venv
.\Scripts\activate
pip install Flask

cd ..


## For windows
$env:FLASK_APP = "app"  
$env:FLASK_ENV = "development"

flask run