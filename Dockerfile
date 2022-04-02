# base image
FROM python:3.9

# working directory inside container
WORKDIR /app

# copy requirements file to working directory in container
COPY requirements.txt ./requirements.txt

# install dependencies from requirements file
RUN pip3 install -r requirements.txt 

# expose port to container
EXPOSE 8501

# copy app to workind directory in container
COPY . /app

# specify command that executes the app
ENTRYPOINT ["streamlit","run"]

# specify the name of the app to be executed by the entry point
CMD ["main.py"]

