import requests

def get_data():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    try:
        print("Connecting to the API...")

        response = requests.get(url, timeout=5)

        response.raise_for_status()

        data = response.json()

        if not isinstance(data, dict) or "title" not in data:
            print("Error: The API returned invalid data.")
            return

        print("\nData received successfully!")
        print("Title:", data["title"])
        print("Body:", data["body"])

    except requests.exceptions.Timeout:
        print("Error: The request took too long. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect. Check your internet connection.")

    except requests.exceptions.HTTPError:
        print("Error: The server returned an unsuccessful response.")

    except requests.exceptions.RequestException:
        print("Error: Something went wrong with the API request.")

    except ValueError:
        print("Error: The API returned data in an invalid format.")

get_data()