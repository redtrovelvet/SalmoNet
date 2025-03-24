1. Create cybera instance
2. SSH to cybera instance
3. [Install docker on instance](https://docs.docker.com/engine/install/ubuntu/)
4. Clone repository on instance
5. Switch to deployment branch
6. Change IPV6 addresses in [environment variables file](.devcontainer/.env)
7. cd into .deployment
8. run ```sudo docker compose up --build```
9. Open new terminal
10. cd into .deployment
11. run ```docker compose exec salmon_project sh```
12. run ```python3 manage.py createsuperuser``` to create admin