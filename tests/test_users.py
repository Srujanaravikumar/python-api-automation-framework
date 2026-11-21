import requests

def test_get_user():
    url="https://jsonplaceholder.typicode.com/users/1"
    response=requests.get(url)
    assert response.status_code==200
    response_data=response.json()
    assert "id" in response_data
    assert response_data["id"]==1
    assert "name" in response_data
    assert response_data["name"].strip()!= ""