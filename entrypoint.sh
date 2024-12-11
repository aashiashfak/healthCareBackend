# python manage.py makemigrations --noinput
# python manage.py migrate --noinput


# # if [ "$APPLICATION_MODE" = "production" ]; then
# #     python manage.py collectstatic --noinput
# #     gunicorn base.wsgi:application --bind 0.0.0.0:8000 --workers 3
# # else
# #     python manage.py runserver 0.0.0.0:8000
    
# # fi

# python manage.py runserver 0.0.0.0:8000