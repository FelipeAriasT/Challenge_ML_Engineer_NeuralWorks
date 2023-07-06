install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

check:
	python -m pytest -vv test/

format:
	autopep8 --in-place --aggressive --aggressive *.py

lint:
	pylint --disable=R,C,W1203,E1101 #poner aca nombre de las carpeta

deploy:
	#push to GCP container registry
	docker build -t api .
	gcloud builds submit --tag gcr.io/neuralworks-391916/api      

	
all: install lint test format deploy