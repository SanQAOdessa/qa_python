import json
import requests

url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'
params = {'sol': 1000, 'camera': 'fhaz', 'api_key': 'DEMO_KEY'}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()
    photos = data['photos']
    number = 1
    for photo in photos:
        response = requests.get(photo['img_src'])
        with open(f'mars_photo{number}.jpg', 'wb') as file:
            file.write(response.content)
        number += 1

except json.JSONDecodeError as e:
    print('Помилка при серіалізації JSON:', e)

except requests.exceptions.RequestException as e:
    print('Помилка при виконанні запиту:', e)