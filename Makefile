build:
	docker-compose build api

start:
	docker-compose up api

daemon:
	docker-compose up -d api

lint:
	docker-compose run --rm api bash -c "python -m flake8 ./api"

db/connect:
	docker exec -it testdb psql -Upostgres

db/downgrade:
	docker-compose run --rm api python manage.py db downgrade

db/upgrade:
	docker-compose run --rm api python manage.py db upgrade

db/migrate:
	docker-compose run --rm api python manage.py db migrate

db/recreate:
	docker-compose run --rm api python manage.py recreate_db

db/recreate_admin:
	docker-compose run --rm api python manage.py recreate_admin_db

db/add_admin:
	docker-compose run --rm api python manage.py create_admin_record
