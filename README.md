    $env:FLASK_APP = "finance"
    $env:FLASK_ENV = "development"
    python -m flask run

    python -m flask init-db


    python -m pytest
    python -m coverage run -m pytest
    python -m coverage html