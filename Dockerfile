FROM python:3
WORKDIR /usr/src/app
COPY . .
CMD ["main.py"]
RUN pip install requests
ENTRYPOINT ["python3"]