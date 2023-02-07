import os
from flask import Flask, request

app = Flask(__name__)

@app.route('/avoid_obstacles', methods=['POST'])
def avoid_obstacles():
    data = request.get_json()
    distance_values = data['distance_values']
    left_speed = 0
    right_speed = 0
    for i in range(8):
        if distance_values[i] > 500:
            if i < 4:
                left_speed += 0.5 * distance_values[i]
                right_speed -= 0.5 * distance_values[i]
            else:
                right_speed += 0.5 * distance_values[i]
                left_speed -= 0.5 * distance_values[i]
            break
    return {'left_speed': left_speed, 'right_speed': right_speed}

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
