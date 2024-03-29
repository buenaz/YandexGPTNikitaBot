import requests
import config


def ask_gpt(collection):
    url = f"https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        'Authorization': f'Api-Key {config.TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        "modelUri": f"gpt://{config.FOLDER_ID}/yandexgpt",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": 500
        },
        "messages": [
            {
                "role": "system",
                "text": config.SYSTEM_PROMPT
            },
            {
                "role": "user",
                "text": collection
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        return response.json()['result']['alternatives'][0]['message']['text']
    except Exception as e:
        result = "Произошла непредвиденная ошибка. Подробности см. в журнале."