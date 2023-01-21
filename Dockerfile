FROM python:3.10

ARG APP_PATH="/app"

WORKDIR $APP_PATH

# Enable virtualenv
ENV VIRTUAL_ENV="$APP_PATH/venv"
RUN python3.10 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install poetry

COPY . $APP_PATH
RUN poetry install

EXPOSE 8000
ENTRYPOINT ["poetry", "run", "python", "-m", "uvicorn", "my_project.main:app"]
