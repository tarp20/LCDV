<h2 align="center">Chief blog.</h2>



### Description of the project:
Chef's blog with recipes


### Development tools

**Stack:**
- Python >= 3.9
- Django >= 3
- sqlite3

### Template used :

https://freehtmlthemes.ru/categories/food/template-587

## Development 

##### 1) Fork the repository and put an asterisk)

##### 2) Clone the repository

    git clone link_you_just_cloned

##### 3) Create virtual environment

    python -m venv venv
    python3 -m venv venv  (Mac)

    
##### 4) Activate virtual enviroment

##### 5) Install dependencies:

    pip install -r requirements.txt
    pip3 install -r requirements.txt  (Mac)

##### 6) Run command to perform migrations

    python manage.py migrate
    python3 manage.py migrate  (Mac)
    
##### 8) Create superuser 

    python manage.py createsuperuser
    python3 manage.py createsuperuser   (Mac)
    
##### 9) Run server

    python manage.py runserver
    python3 manage.py runserver (Mac)