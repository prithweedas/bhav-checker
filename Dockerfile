FROM node:14.15.2 as build
WORKDIR /usr/src/app
COPY . .
WORKDIR /usr/src/app/client
RUN npm install
RUN npm run build

FROM python:3.9.0 as main
WORKDIR /usr/src/app
COPY --from=build /usr/src/app/server/ ./
COPY ./requirements.txt ./requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python manage.py collectstatic
EXPOSE 8000
CMD [ "gunicorn", "server.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3" ]

