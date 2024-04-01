import requests

def fetch_data(url, request_number):
    response = requests.get(url)
    print(f"Request {request_number}")

def main():
    url = "http://127.0.0.1:8000/api/employers/"
    num_requests = 1000000
    for i in range(num_requests):
        fetch_data(url, i)

if __name__ == "__main__":
    main()
