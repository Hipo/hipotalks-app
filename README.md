# Hipotalks App

You can find the figma file [here](https://www.figma.com/file/zRCcVpnh5lVn3BDpbDtBqN/Hipotalks).

## Deployment ‍💻

All commands should be run considering the repository's root (i.e. where this file is located) as the working directory unless they are executed within a container (which has its own working directory).

### Running the project 🚀

- Install [Docker](https://docker.com).

- Secret credentials like aws keys are not included in the settings. Provide secrets.py from the main developer.
And put it under the settings directory.

- `docker-compose -f docker-compose-development.yml up --build -d`
 The first time the process might take a few minutes, after that Docker will use its cache to speed up things.
 
- `docker-compose -f docker-compose-development.yml exec hipotalks_app bash`

- `python manage.py migrate` (This might raise an error. Wait a few seconds for database to be ready. Then run it again.)
- `python manage.py createsuperuser`
- You can run `python manage.py runserver 0:8000` to run server.

Now you can reach the app from your host machine at **http://localhost:8000**


When you are done:

- `docker-compose -f docker-compose-development.yml down` (Optional)
- `docker system prune` (Optional, frees storage by removing **all** unused images, containers etc. **on the host**, use with care!)
