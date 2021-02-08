FROM python as notifier

COPY main.py /tmp/main.py
COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

CMD python /tmp/main.py

FROM notifier as specific

COPY specific.py /tmp/specific.py
COPY specific.requirements.txt /tmp/specific.requirements.txt

RUN pip install -r /tmp/specific.requirements.txt

CMD python /tmp/specific.py