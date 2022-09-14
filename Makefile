api/build:
	docker-compose build --no-cache test-fastapi

api/up:
	docker-compose up test-fastapi

api/down:
	docker-compose rm -fsv test-fastapi

db/build:
	docker-compose build --no-cache test-fastapi-postgresql

db/up:
	docker-compose up test-fastapi-postgresql

db/down:
	docker-compose rm -fsv test-fastapi-postgresql
