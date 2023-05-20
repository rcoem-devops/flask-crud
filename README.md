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


docker pull python:3.8-alpine
docker images

docker build -t rahulmr/rknecdemo:v1 .

docker run -it --name flaskdemo -p 8090:5000 -d rahulmr/rknecdemo:v2 


