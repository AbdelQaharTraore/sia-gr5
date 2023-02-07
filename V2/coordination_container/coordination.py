import requests

def coordination(light_value, obstacle_value):
:
    if obstacle_value > 500:
        # Avoid obstacle
        requests.post("http://obstacle-service:5000/avoid")
    else:
        # Seek light
        requests.post("http://light-service:5000/seek", json={"light_values": light_values})
