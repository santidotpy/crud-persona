FROM python:3

RUN git clone https://github.com/santidotpy/crud-persona.git

WORKDIR /crud-persona

RUN pip install -r requirements.txt

CMD ["python3", "test_persona.py"]