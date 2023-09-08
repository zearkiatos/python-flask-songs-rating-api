#!/bin/bash
activate () {
    if [ -d "venv" ] 
    then
        echo "Python 🐍 environment was activated"
        source venv/bin/activate
    else
        echo "The folder environment doesn't exist"
        python3 -m venv venv
        source venv/bin/activate
        echo "The environment folder was created and the python 🐍 environment was activated"
    fi
}

install () {
    pip install -r requirements.txt
}

run () {
    cd flaskr
    if [ -z "$1" ]
    then
        flask run
    else
        flask run -p $1
    fi
}

docker_up() {
    docker compose up --build
}

docker_down() {
    docker compose down
}

run_docker () {
    if [ -z "$1" ]
    then
        flask run -h localhost
    else
        flask run -p $1 -h localhost
    fi
}
