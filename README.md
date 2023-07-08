# flask-crud
 
 
## Pre-requisites

1. Install Python on your Laptop / Desktop
2. Make sure pip is properly configured. To verify open command prompt or powershell window or terminal and `python -V` and `pip -V`
3. Read about `virtualenv` you can create a local env in directory
4. Avoid Spaces in the directory aka folder names e.g. instead of my flask app create a folder my-flask-app or my_flask_app
5. Install flask and pytest
6. Check the `requirements.txt` file for the versions. In python, `requirements.txt` is very important file and the name should be eact same that is `requirements.txt` , no shortcuts like `reqs.txt` or `myrequirement.txt` or `somethingelse.txt` 

## Instructions for running the flask application


open terminal

clone the git repository using below command

`git clone https://github.com/rcoem-devops/flask-crud.git`

the cd to the `flask-crud` directory

Run below command to create a Table in Database

`python create_table.py`

run below command to start the Flask App

`python app.py`

It will run flask app on port `5000` on `localhost` or `127.0.0.1`

Open browser and hit `http://127.0.0.1:5000/`


python -V
pip -V
pip install virtualenv --user
python -m pip install --upgrade pip
docker version
python -m virtualenv venv
source ./venv/bin/activate
pip install -r requirements.txt
python ./create_table.py
python ./app.py
docker pull nginx
docker image ls
docker run -it --rm --name web -p 8080:80 -d nginx
docker ps
docker container ls
CONTAINER ID   IMAGE     COMMAND CREATED  STATUS                    PORTS                                                                  NAMES
9b445d8770c5   nginx     "/docker-entrypoint.…"   48 seconds ago   Up 46 seconds   0.0.0.0:8080->80/tcp, :::8080->80/tcp   web

docker container ls -a
docker container stop web
docker container stop 9b445d8770c5

docker run -it --name web -p 8080:80 -d nginx

