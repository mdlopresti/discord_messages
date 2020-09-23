FROM python

COPY main.py /tmp/main.py
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD python /tmp/main.py