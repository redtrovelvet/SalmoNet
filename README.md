# CMPUT404-Project-SocialDistribution

Originally developed as a group project for CMPUT404 at the University of Alberta.

Team: Salmon

See this [web page](https://uofa-cmput404.github.io/general/project.html) for a description of the project

Docs: https://uofa-cmput404.github.io/w25-project-mod-salmon/

## Images
<img width="1440" alt="Screenshot 2025-04-07 at 3 53 28 AM" src="https://github.com/user-attachments/assets/dd351f37-1f70-4b1d-955f-ac9750ae9ebf" /> 
<img width="1440" alt="Screenshot 2025-04-07 at 3 53 39 AM" src="https://github.com/user-attachments/assets/3ce39b41-842b-4354-ad1d-301ddbabf934" />
<img width="1437" alt="Screenshot 2025-04-07 at 3 52 04 AM" src="https://github.com/user-attachments/assets/8791f0cd-dfb5-4c1b-bc26-c4443b60dfc7" />
<img width="1440" alt="Screenshot 2025-04-07 at 3 52 22 AM" src="https://github.com/user-attachments/assets/e32235ec-8f26-47ae-8e2c-9fd8185d7554" />
<img width="1440" alt="Screenshot 2025-04-07 at 3 56 32 AM" src="https://github.com/user-attachments/assets/2a6c22ce-1e86-4705-86f6-a859b6db3f35" />
<img width="1440" alt="Screenshot 2025-04-07 at 4 03 19 AM" src="https://github.com/user-attachments/assets/93cca44d-61d6-4a4d-9f94-049c05f9cf6f" />
<img width="1440" alt="Screenshot 2025-04-07 at 4 01 07 AM" src="https://github.com/user-attachments/assets/ffe4e8a0-7843-4f6d-9ef4-5c86404ef2c7" />

## Video
https://youtu.be/RLeqbPTvaUE

## Fully Connected Groups
- ForestGreen
- DodgerBlue
- Lavender
- MintCream

## License
MIT License

## Team Members:
- Carlin Boyles
- Ethan Chung
- Ryan Edwards
- Gitanjali Ghugare
- Harshita Handa
- Jesugbenga Omoniwa

## Structure
- .deployment: production deployment setup
  -  Caddyfile: configures the reverse proxy
  -  docker-compose.yml: containers for django app, caddy, and postgress reverse proxy
  -  Dockerfile
  -  .env: environemnt variables used in production
- .devcontainer/: devcontainer configuration for local development
  - devcontainer.json
  - .env: specifications for local ev variables
  - Dockerfile: for the dev environemnt
- .github/
  - workflows/
    - ci.yml: github actions
- docs/: documentation files
  - author_api.md
  - commented_api.md
  - comments_api.md
  - following_friends_api.md
  - inbox.md
  - index.md
  - liked_api.md
  - likes_api.md
  - malicious_user.md
  - node_management_api.md
  - post_api.md
  - project-requirements.md
- src/: main project code
  - salmon_project/
    - salmon_project/
      - __init__.py
      - settings.py
      - urls.py
      - wsgi.py
      - asgi.py
    - social_distribution/
      - migrations/
      - static/
        - css/
        - img/
        - js/
      - templates/: django templates for html rendering
      - tests/: testing codes
        - __init__.py
        - tests_comments_likes.py
        - tests_following_friends.py
        - tests_identity.py
        - tests_inbox.py
        - tests_malicious_user.py
        - tests_node_management.py
        - tests_posting.py
        - tests_reading.py
        - tests_sharing.py
        - tests_visibility.py
      - __init__.py
      - admin.py
      - apps.py
      - models.py: database schema
      - serializers.py: REST framework serializerrs
      - urls.py: routes within the app
      - views.py: api endpoints and html views
  - manage.py: django's management script
  - requirements.txt: dependencies for django app
- gitignore
- deployment.md: instructions to host your node using cybera instance
- mkdocs.yml

## Setup

### Devcontianer
1. open repository in editor
2. install contianers extension if necessary
3. reopen in the devcontainer
4. run:
   - ```cd src/salmon_project```
   - ```python manage.py makemigrations```
   - ```python manage.py migrate```
   - ```python manage.py runserver```
5. Go to http://127.0.0.1:8000 in your browser.

### Deployment
1. edit .deployment/.env to allow your IP address
2. ensure BASE_URL in settings is your IP address
3. ssh into your instance and clone the repository
4. cd into .deployment
4. run:
   - ```sudo docker compose up --build```
5. once containers are up, go to new terminal to run migrations and create superuser:
   - ```docker compose exec salmon_project sh```
   - ```cd salmon_project```
   - ```python manage.py makemigrations```
   - ```python manage.py migrate```
   - ```python manage.py createsuperuser```
6. Access the app through your IP address

### Enjoy our application!

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/Ttpk-cQs)
