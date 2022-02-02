# docker-from-my-image
FROM agaarbi/alpine-modified (which is alpine base with requirements)

# to run container with command prompt
docker exec -it naughty_volhard sh
docker run --rm -it --entrypoint=bin/sh alpine-modified
https://stackoverflow.com/questions/20813486/exploring-docker-containers-file-system
