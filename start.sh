#!/bin/bash

LIST=()
i=0
docker_option="up -d"
second_docker_option=""

if [[ "$(sudo docker images -q py-rdb:latest 2> /dev/null)" == "" ]]; then
echo "Build main img"
 sudo docker-compose -f main-img/docker-compose.yml build --no-cache 
fi

while [[ $# -gt 0 ]]; do
  key="$1"

  case $key in
    -s|--single)
      LIST[$i]="$2"
      i=$(($i+1))
      shift # past argument
      shift # past value
      ;;
    -h|--help)
        cat << EOF
-o | --option:     Docker options: 
        up = up -d
        down
        logs = --tail=200 -f
        build--no-cache = build --no-cache
        build
        restart
EOF
      echo "-s | --single:     Only start this application. The argument should be the name of the application folder. The argument can be used multiple times"
      shift # past argument
      shift # past value
      ;;
        up)
            docker_option='up -d'
            shift # past argument
            ;;
        down)
            docker_option=down
            shift # past argument
            ;;
        logs)
            docker_option=logs
            second_docker_option= --tail=200 -f
            shift # past argument
            ;;
        build--no-cache)
            docker_option=build --no-cache
            shift # past argument
            ;;
        build)
            docker_option=build
            shift # past argument
            ;;
        restart)
            docker_option=restart
            shift # past argument
            ;;
      
    *)    # unknown option
      shift # past argument
      ;;
  esac
done

echo $docker_option
if [ ${#LIST[@]} -gt 0 ]; then
  for x in ${LIST[@]}; do
  sudo docker-compose -f $x/docker-compose.yml -p python-test $docker_option
    done
else
  sudo docker-compose -p python-test $docker_option
 
fi
 


    
