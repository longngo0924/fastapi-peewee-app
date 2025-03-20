FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Install additional dependencies required for psycopg2
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . /code/

# Expose port for the application
EXPOSE 8000

# Command to run the application using FastAPI CLI
CMD ["fastapi", "run", "app/main.py", "--port", "8000", "--host", "0.0.0.0"] 