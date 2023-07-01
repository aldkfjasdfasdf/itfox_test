FROM python:3.11

WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/

CMD python manage.py migrate && \
    echo "from apps.profile.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell && \
    python manage.py runserver 0.0.0.0:8000