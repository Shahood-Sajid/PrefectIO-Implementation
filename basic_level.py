from prefect import flow, task
import requests

@task(retries=2)
def extract_data():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    return data

@task
def transform_data(data):
    transformed_data = [item['title'] for item in data]
    return transformed_data

@task
def load_data(transformed_data):
    # Just print the first 5 for simplicity
    for title in transformed_data[:5]:
        print(f"Loading title: {title}")
    1/0

@flow
def etl_flow(name="ETL flow"):
    data = extract_data()
    print("sadfs")
    transformed_data = transform_data(data)
    load_data(transformed_data)

if __name__ == "__main__":
    etl_flow()
