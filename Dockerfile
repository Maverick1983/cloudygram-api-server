FROM python:3.9.12-slim
ENV PYTHONUNBUFFERED=0
WORKDIR /app
RUN python -m venv /opt/Telegram
# Enable venv
ENV PATH="/opt/Telegram/bin:$PATH"
RUN sh /opt/Telegram/bin/activate
COPY main.py main.py
COPY keys.json keys.json
COPY requirements.txt requirements.txt
COPY cloudygram_api_server cloudygram_api_server
RUN pip3 install -r requirements.txt
COPY _telethon /opt/Telegram/lib/python3.9/site-packages/telethon/utils.py
COPY _telethon /opt/Telegram/lib/python3.9/site-packages/telethon/version.py
CMD [ "python3", "-u" ,"main.py" ]