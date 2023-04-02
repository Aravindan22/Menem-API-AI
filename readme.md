
# Menem API

This repository includes API part of Menem

## Run Locally

Clone the project

```bash
  git clone <project repo>
```

Install the requirements using the file

```bash
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app
```
  - If you want to host public you need to add below argument in command
    ```bash
    --host 0.0.0.0 --port <port number>
    ```


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`OPENAI_API_KEY`

Get this token from openai 

## Documentation

To see the API docs, you can run the application and visiti /docs path
