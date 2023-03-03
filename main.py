import docker
import json
import requests
import time


def send_telegram_message(message, telegram_config):
    """
    Отправка сообщения в телеграм
    """
    url = f"https://api.telegram.org/bot{telegram_config['token']}/sendMessage"
    payload = {
        "chat_id": telegram_config['chat_id'],
        "text": message
    }
    response = requests.post(url, json=payload)
    if response.status_code != 200:
        print(f"Failed to send message to Telegram. Status code: {response.status_code}")
    else:
        print("Telegram message sent successfully!")


def main():
    # Чтение конфигурации Docker и Telegram из файлов
    with open('docker-config.json') as f:
        docker_config = json.load(f)
    with open('containers-config.json') as f:
        containers_config = json.load(f)
    telegram_config = docker_config['telegram']

    # Подключение к докеру
    client = docker.DockerClient(base_url='unix://' + docker_config['docker_socket'])

    # Получение списка запущенных контейнеров
    running_containers = client.containers.list()

    # Поиск паттернов в каждом контейнере и отправка сообщений в телеграм
    for container in running_containers:
        container_name = container.name
        for config_name, config in containers_config['containers'].items():
            if config_name in container_name:
                patterns = config['patterns']
                container_logs = container.logs().decode('utf-8')
                for pattern in patterns:
                    if pattern['pattern'] in container_logs:
                        message = pattern['message']
                        status = pattern['status']
                        last_notification = pattern['last_notification']
                        # Определяем, нужно ли отправлять уведомление
                        if status == "active" and (not last_notification or time.time() - last_notification > 3600):
                            send_telegram_message(message, telegram_config)
                            pattern['last_notification'] = time.time()
                            with open('containers-config.json', 'w') as f:
                                json.dump(containers_config, f, indent=4)


if __name__ == '__main__':
    main()
