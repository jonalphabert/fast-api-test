# Fast API Project - Cashier Application API

### How to Start This Project

First of all, you can clone this project. Then, run this command on your terminal

```bash
    pip install -r requirements.txt
    python populate_database.txt
    uvicorn app.main:app --reload
```

If you want to use virtual environment python, you can run this command

```
    python3 -m venv venv
    ./venv/Script/activate                      # If you are on windows
    source venv/bin/activate                    # If you are on Mac or linux
    pip install -r requirements.txt
    python populate_database.txt
    uvicorn app.main:app --reload
```

The documentation of this project will serve on http://localhost:8000/docs
