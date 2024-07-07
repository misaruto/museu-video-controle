FROM mcr.microsoft.com/mssql/server:2019-latest

ENV SA_PASSWORD=@sa12345
ENV ACCEPT_EULA=Y


COPY ./sql/CREATE/*.sql /tmp/scripts/
COPY ./startup.sh /tmp/scripts/startup.sh

USER root
RUN chmod +x /tmp/scripts/startup.sh

USER mssql
