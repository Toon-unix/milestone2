FROM postgres:15

COPY ./app/init.sql /docker-entrypoint-initdb.d/init.sql

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=Root123!
ENV POSTGRES_DB=milestone2

EXPOSE 5432
