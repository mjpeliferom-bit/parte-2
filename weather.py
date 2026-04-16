import requests

api_key = "93e11876396d366ac2b56ed0b0b2cad7"
cidade = "Barueri"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt_br"

resposta = requests.get(url)
dados = resposta.json()

if "weather" in dados:
    print("Clima:", dados["weather"][0]["description"])
    print("Temperatura:", dados["main"]["temp"])

    chuva = dados.get("rain", {}).get("1h", 0)

    if chuva > 0:
        print("Vai chover -> NÃO irrigar")
    else:
        print("Sem chuva -> irrigar")
else:
    print("Erro na API:", dados)