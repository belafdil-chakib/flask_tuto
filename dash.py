import requests

# Define the base URL for the API
base_url = 'http://localhost:5000'


def get_predict(id_client):
    response = requests.get(base_url + f"/predict/{id_client}")
    score = response.json()
    # Check if the request was successful (200 status code)
    if response.status_code == 200:
        # Print the response content (JSON data)
        print(score)
    else:
        # Print an error message if the request failed
        print('Error: request failed with status code', response.status_code)

    return


if __name__ == '__main__':
    get_predict("100001")
