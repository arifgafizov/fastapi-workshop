FROM python:3.9.9
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update

WORKDIR /app

COPY src/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY ./src /app

EXPOSE 8000

CMD ["uvicorn", "workshop.app:app", "--host=0.0.0.0" , "--reload" , "--port", "8000"]
