FROM python:3.14.7-alpine
LABEL authors="Stanisław Marszałek"

RUN pip install django && pip install django-scheduler

EXPOSE 8000

WORKDIR /usr/checkAvailability

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]