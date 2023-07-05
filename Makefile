install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=mlib --cov=app test_mlib.py

format:
	autopep8 --in-place --aggressive --aggressive *.py

lint:
	pylint --disable=R,C,W1203,E1101 #poner aca nombre de las carpeta

deploy:
	#push to ECR for deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 561744971673.dkr.ecr.us-east-1.amazonaws.com
	docker build -t mlops .
	docker tag mlops:latest 561744971673.dkr.ecr.us-east-1.amazonaws.com/mlops:latest
	docker push 561744971673.dkr.ecr.us-east-1.amazonaws.com/mlops:latest
	
all: install lint test format deploy