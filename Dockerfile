FROM python:3.10-bullseye

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY . app.py /app/


RUN pip install --no-cache-dir --upgrade pip &&\
    pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]