FROM python:3.8

ENV PIP_DISABLE_PIP_VERSION_CHECK=on

RUN pip install poetry

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction

COPY . /app

EXPOSE 5000
STOPSIGNAL SIGINT
ENTRYPOINT ["python3", "app.py"]
CMD ["python3", "app.py"]
