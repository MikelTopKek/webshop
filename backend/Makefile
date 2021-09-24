current_dir = $(shell pwd)

start_backend_local:
	docker-compose -f docker-compose-local.yml up -d;

stop_backend_local:
	docker-compose -f docker-compose-local.yml stop;

build_local:
	docker-compose -f docker-compose-local.yml build;

down_local:
	docker-compose -f docker-compose-local.yml down;
