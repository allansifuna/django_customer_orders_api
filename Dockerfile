# start by pulling the python image
FROM python:3.11-alpine

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

RUN apk add libpq-dev
# copy the requirements file into the image
COPY ./requirements.txt /requirements.txt


# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

# copy every content from the local file to the image
COPY . .

# configure the container to run in an executed manner
ENTRYPOINT ["python", "manage.py","runserver", "0.0.0.0:8000"]
EXPOSE 8000
