# Restaurant API

This is a simple api, that features:
* storing, creating  and updating a menu, consisting of  meals from several categories;
* saving orders from users;
* authorization and authentication;
* image uploads;
* swagger api documentation, using drf_yasg;


## Installation

Clone this repository with git:

```bash
git clone https://github.com/Insomenya/restaurant-backend.git
```
Create python virtual environment, select it. Then use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies for the API in the environment.

```bash
python -m venv ./env

./env/Scripts/activate

pip install setuptools -r requirements.txt
```

## Usage

To run the server type:

```bash
python manage.py runserver
```

[Live version](https://insomenya.pythonanywhere.com/) is available at pythonanywhere.com.

## License

[MIT](https://choosealicense.com/licenses/mit/)