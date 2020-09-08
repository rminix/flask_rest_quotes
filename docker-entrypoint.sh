while ! nc -z $POSTGRES_HOST:5432; do
    echo "Can't reach database server or port. retrying in 5 second..."
    sleep 5
done
#flask db upgrade
uwsgi --ini uwsgi.ini