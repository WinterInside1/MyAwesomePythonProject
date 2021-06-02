#!/usr/bin/env sh
  if [ "$Database" = "postgres" ]
  then
      echo "Waiting for postgres"
      while ! nc -z $SQL_HOSt $SQL_PORT; do
        sleep 0.1
      done
      echo "PgSQL started"
  fi


  exec "$@"
