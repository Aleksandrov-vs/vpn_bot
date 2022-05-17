ifneq (,$(wildcard ./.env))
    include .env
    export
endif

fresh_database:
	echo "This command cleans up the whole database. Press ENTER if you are sure you are not on production, else press Ctrl+C"; \
	read REPLY; \
	docker-compose stop postgres; \
	rm -rf data/postgres || true; \
	docker-compose up -d postgres; \
    until docker-compose exec  postgres pg_isready -h localhost -p 5432; do sleep 1; done;\

restart_bot:
	echo "This command will rebuild the bot image and restart the container. Press ENTER if you are sure you are not on production, else press Ctrl+C"; \
	read REPLY; \
	docker-compose up -d --no-deps --build bot;\


