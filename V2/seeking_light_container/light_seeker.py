from flask import Flask, request

app = Flask(__name__)

@app.route('/light', methods=['GET'])
def light_seeker(robot, light_sensors):
    light_value = request.args.get('light_value')
    if light_value:

        light_values = [sensor.getValue() for sensor in light_sensors]
        # Determine the direction of the light source
        max_light_index = light_values.index(max(light_values))
        
        # Turn the robot towards the light source
        if max_light_index < 4:
            # Turn left
            left_wheel_velocity = -1
            right_wheel_velocity = 1
        else:
            # Turn right
            left_wheel_velocity = 1
            right_wheel_velocity = -1
            
        # Set wheel velocities
        wheels = [robot.getDevice('left wheel motor'), robot.getDevice('right wheel motor')]
        for wheel in wheels:
            wheel.setVelocity(float('inf'))
        wheels[0].setVelocity(left_wheel_velocity)
        wheels[1].setVelocity(right_wheel_velocity

        result = "Light_values: {}".format(light_values)
        return result
    else:
        return "Error: light value not provided in query parameters"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
