#!/bin/bash
SA_PASSWORD="@sa12345"
##Script to run inside docker container
arquivos=$(ls /tmp/scripts/*.sql -1)
for arquivo in $arquivos
do
  echo "Executing file: $arquivo"
  /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -i $arquivo
  echo "$arquivo executed successfully"
done


