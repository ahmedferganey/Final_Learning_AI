# Mini-Rag

## Scope
This is a minimal implementation of the RAG Model for question answering    .

---

## Requirements

- Python 3.10

#### Install Dependencies

```bash
sudo apt update
sudo apt install libpq-dev gcc python3-dev
```

#### Create a new environment 

**Create a new environment using the following command:**
```bash
$ python3 -m venv .venv
```
**Activate the environment:**
```bash
$ source .venv/bin/activate
$ sudo apt update
$ sudo apt install libpq-dev gcc python3-dev
```

#### Create .env and requirements.txt 

```bash
$ touch requirements.txt .env

```

---

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```


## Run the FastAPI server (Development Mode)


```bash
(.venv) fragello@fragello:~/ME/Github/Learning/Final_Learning_AI/09_Gen_AI/02_rag/project/mini_rag_app$ uvicorn  main:app --reload --host 0.0.0.0 --port 5000
```

## POSTMAN Collection

Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)








## Suggested Contents
- `assets/`
- `examples/`
- `datasets/`
- `prompts/`
- `demo/`
