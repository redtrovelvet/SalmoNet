1. Create cybera instance
2. SSH to cybera instance
3. [Install docker on instance](https://docs.docker.com/engine/install/ubuntu/)
4. Clone repository on instance
5. Switch to deployment branch
6. Change IPV6 addresses in [environment variables file](.devcontainer/.env)
7. Change BASE_URL in [settings.py](salmon_project/salmon_project/settings.py) to "http://[ipv6 address]"
8. cd into .deployment
9. run ```sudo docker compose up --build```
10. Open new terminal
11. cd into .deployment
12. run ```docker compose exec salmon_project sh```
13. run ```python3 manage.py createsuperuser``` to create admin