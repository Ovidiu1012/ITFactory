import json
class Variables:
    search_item = 'Lupi'
class Credentials:
    email = 'pytest.vinulbun@gmail.com'
    pwd = 'ITFactory2023.'
class Details:
    obs = 'Comanda test Python Ovidiu'
class Api:
    url = "http://nexus.atacpc.ro:55005/api/v3/read/comenzi_clienti"
    header = {

        "Authorization" : "Basic MUM1NDBDNjNGNjYxNDlBRDgxRTdEN0FCMTQxQTk5NjQ6",
        "Content-Type" : "application/json"

    }
    body = json.dumps({
        "den_client": "Python test"
    })