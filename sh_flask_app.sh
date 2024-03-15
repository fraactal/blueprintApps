sudo docker stop flask_docker_app
sudo docker rm flask_docker_app
sudo docker rmi flask_docker_app
sudo docker image build -t flask_docker_app .
sudo docker run  --name flask_docker_app -p 5000:5000 -d flask_docker_app