activate:
	source run.sh; activate

install:
	source run.sh; install

run:
	source run.sh; run $(port)

docker-up:
	source run.sh; docker_up

docker-down:
	source run.sh; docker_down

run-docker:
ifeq ($(strip $(port)),)
	flask run -h 0.0.0.0
else
	flask run -p $(port) -h 0.0.0.0
endif