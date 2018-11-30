#Install
```
sudo apt-get install python-virtualenv # or install virtualenv using your prefered method 

virtualenv -p $(which python3) venv

source venv/bin/activate

pip install -r requirements.txt

./manage.py migrate

./manage.py runserver
```

#USE CASE

Open the development server at http://127.0.0.1:8000/.

That will bring you to the REST API enpoint:
```
{
    "documents": "http://127.0.0.1:8000/documents/",
    "customers": "http://127.0.0.1:8000/customers/",
    "addresses": "http://127.0.0.1:8000/addresses/",
    "products": "http://127.0.0.1:8000/products/",
    "records": "http://127.0.0.1:8000/records/"
}
```

Use the `documents` endpoint to upload `.tsv` files.

Once uploaded the `customers`, `addresses`, `products`, and `records` endpoints will be populated.

To view the database use the command `sqlite3 db.sqlite3`.
