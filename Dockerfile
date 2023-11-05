# 3.12-slim だと以下のエラーになるため、3.10-slim に変更
# https://community.openai.com/t/error-installing-openai-aiohttps-error-on-python-3-12/456052/2
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# openai を使用するためのKeyを設定
ENV OPENAI_API_KEY="your_api_key_here"

WORKDIR /code

COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /code/
