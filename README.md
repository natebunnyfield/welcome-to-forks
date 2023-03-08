# Welcome to Forks: A Take Home Assessment for [redacted]

## Installation

* Open a terminal and run

```sh
git clone https://github.com/natebunnyfield/welcome-to-forks.git
cd welcome-to-forks
pipenv install
```

* Create your own Github OAuth Application at [github.com/settings/applications/new](https://github.com/settings/applications/new)

* Fill out the form with following values. Leave `Application description` blank and `Enable Device Flow` unchecked.

```
Application name: welcome-to-forks
Homepage URL: https://www.youtube.com/watch?v=6XaiH56V9tI
Authorization callback URL: http://localhost:8080/oauth/callback
```

On the next page, you will need to find the `Client ID` and a generate a new client secret. Copy both into a new `.env` file using `.env.example` as a template.

## Usage

* After installation, run this terminal command in the same directory

```sh
pipenv run flask run
```

* Navigate to [localhost:8080](http://localhost:8080).

## Future improvements

* Tests
* Error handling
* Incorporate feedback from interview
