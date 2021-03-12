FROM python:3.8.8-slim
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["bin/deploy-app", "dev", "0.0.0.0"]
