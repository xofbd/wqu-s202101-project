import os

from flask import Flask, request

from location_info import generate_sunset_message, retrieve_local_ip_address

app = Flask(__name__)
DEPLOY = os.getenv('DEPLOY')


@app.route('/')
def main():
    if DEPLOY == 'heroku':
        ip_address = request.headers['X-Forwarded-For']
    else:
        ip_address = retrieve_local_ip_address()

    return generate_sunset_message(ip_address)


if __name__ == '__main__':
    app.run()
