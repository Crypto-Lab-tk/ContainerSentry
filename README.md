# Container Sentry

[![Docker Image Deploy](https://github.com/Crypto-Lab-tk/ContainerSentry/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Crypto-Lab-tk/ContainerSentry/actions/workflows/docker-image.yml)

## Introduction

This is a Docker monitoring application that searches for patterns in the logs of running Docker containers and sends a message to a Telegram chat if a pattern is found. The application requires a Docker daemon to be running on the host machine and a Telegram bot to be set up with a valid token and chat ID.

## Configuration
### `docker-config.json`

This file contains the configuration for connecting to the Docker daemon and the Telegram bot. The contents of the file are as follows:

```json
{
  "docker_socket": "/var/run/docker.sock",
  "telegram": {
    "token": "your_token_here",
    "chat_id": "your_chat_id_here"
  }
}
```

`docker_socket`: the path to the Docker daemon socket file.
`telegram.token`: the Telegram bot token.
`telegram.chat_id`: the ID of the Telegram chat to send messages to.

### `containers-config.json`
This file contains the configuration for the containers to monitor and the patterns to search for in their logs. The contents of the file are as follows:

```json
{
  "containers": {
    "container_name_1": {
      "patterns": [
        {
          "pattern": "error",
          "message": "Error occurred in container_name_1"
        }
      ]
    },
    "container_name_2": {
      "patterns": [
        {
          "pattern": "warning",
          "message": "Warning occurred in container_name_2"
        },
        {
          "pattern": "critical",
          "message": "Critical occurred in container_name_2"
        }
      ]
    }
  }
}
```
`containers.container_name_x`: the name of the container to monitor, where x is a number.
`containers.container_name_x`.patterns: a list of patterns to search for in the container's logs.
`containers.container_name_x`.patterns.pattern: the string pattern to search for in the logs.
`containers.container_name_x`.patterns.message: the message to send to the Telegram chat if the pattern is found.

### `requirements.txt`
This file lists the Python dependencies required by the application. The contents of the file are as follows:

```requirements
docker
requests
```
`docker`: the Python Docker API library

`requests`: the Python HTTP library used to send messages to Telegram.

## Running the Application

Create a Telegram bot and obtain a token and chat ID.

1. Create the `docker-config.json` and `containers-config.json` files and populate them with the required configurations.
2. Create a Docker image of the application using the provided Dockerfile.
3. Start the application container with the following command:
```javascript
docker run -v /var/run/docker.sock:/var/run/docker.sock your_image_name
```

## Limitations

* The application only searches for patterns in the logs of running Docker containers.

* The application only sends messages to a single Telegram chat.

* The application only supports the string pattern matching.





