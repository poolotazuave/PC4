# EJERCICIO 1
import requests

def get_bitcoin_price():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response_json = response.json()
        bitcoin_price = response_json["bpi"]["USD"]["rate_float"]
        return bitcoin_price
    except requests.RequestException as e:
        print("Error al obtener el precio de Bitcoin:", e)
        return None

def main():
    try:
        n = float(input("Ingrese la cantidad de bitcoins que posee: "))
        bitcoin_price = get_bitcoin_price()

        if bitcoin_price is not None:
            total_cost = n * bitcoin_price
            formatted_cost = "{:,.4f}".format(total_cost)
            print(f"El costo actual de {n:.8f} Bitcoins es: {formatted_cost} USD")
    except ValueError:
        print("Por favor, ingrese un valor válido para la cantidad de bitcoins.")

if __name__ == "__main__":
    main()


#EJERCICIO 2
import pyfiglet
import random

def select_random_font():
    available_fonts = pyfiglet.Figlet.getFonts()
    return random.choice(available_fonts)

def main():
    user_font = input("Ingrese el nombre de la fuente (deje en blanco para aleatoria): ")
    if not user_font:
        selected_font = select_random_font()
        print(f"Fuente aleatoria seleccionada: {selected_font}")
    else:
        selected_font = user_font

    user_text = input("Ingrese el texto: ")
    ascii_text = pyfiglet.Figlet(font=selected_font).renderText(user_text)
    print(ascii_text)

if __name__ == "__main__":
    main()





