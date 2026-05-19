FROM python:3.13-slim

# .pyc file ignored + unbuffered logging.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN useradd -m -u 1000 mainuser

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/
RUN SECRET_KEY=build_dummy_key ALLOWED_HOSTS=localhost python manage.py collectstatic --noinput

RUN chown -R mainuser:mainuser /app
USER mainuser

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "portfolio.wsgi:application"]

