# pycharm
Docker with pycharm, spark 1.6.1, and pybuilder


#Run socat to open a bidirectional byte stream to interact with pycharm IDE
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"

#Get your ip address.  May not be inet
ifconfig en0 | grep 'inet ' | awk -F ' ' '{print $2}'

#To run
docker run -it -v /tmp/.X11-unix/:/tmp/.X11-unix/ -e DISPLAY=YOUR.IP.ADDRESS:0 --rm sunileman/pycharm

#To run and mount directories 
docker run -it -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v ~/PycharmProjects:/root/PycharmProjects -v ~/.PyCharm40:/root/.PyCharm40 -e DISPLAY=YOUR.IP.ADDRESS:0 --rm sunileman/pycharm

#Bash into container
docker exec -it <container id> bash
