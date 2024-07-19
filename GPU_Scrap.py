import requests
from bs4 import BeautifulSoup
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def scrap_gpu_database():
    url = 'https://www.tomshardware.com/reviews/gpu-hierarchy,4388.html'
    data_item = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/91.0.4472.124 Safari/537.36'}


    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontra todas as linhas da tabela
    rows = soup.find_all('tr')

    # Itera sobre as linhas encontradas
    for row in rows:
        # Encontra todas as células da linha
        cells = row.find_all('td')

        # Verifica se a célula contém as informações desejadas
        if len(cells) > 1:
            fps_values = [cell.text.strip() for cell in cells[0:]]
            row = {'Nome': fps_values[0], '1080p Ultra': fps_values[2], '1080p Medio': fps_values[3],
                   '1440p Ultra': fps_values[4], '4k Ultra': fps_values[5], 'Especificação': fps_values[6]
                   }
            data_item.append(row)

    return data_item

data_item = scrap_gpu_database()
df = pd.DataFrame(data_item)
print(df)

df.to_csv('dadosGPU.csv', index=False)