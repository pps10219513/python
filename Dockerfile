FROM python:3

WORKDIR /usr/src/app

COPY calculadora.py ./
COPY test_calculator.py ./

CMD [ "python", "-m", "unittest", "discover", "-v"]
