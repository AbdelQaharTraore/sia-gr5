from controller import Robot

TIMESTEP = 64
MAX_SPEED = 10


def run_robot(robot):
    """
    Function to run the robot and implement the Braitenberg controller
    """
    # Initialize wheels
    wheels = []
    wheel_names = ['left wheel motor', 'right wheel motor']
    for i in range(2):
        wheel = robot.getDevice(wheel_names[i])
        wheel.setPosition(float('inf'))
        wheel.setVelocity(0.0)
        wheels.append(wheel)
    
    # Initialize light sensors
    light_sensors = []
    for i in range(8):
        light_sensor = robot.getDevice('ls' + str(i))
        light_sensor.enable(TIMESTEP)
        light_sensors.append(light_sensor)
    
    # Initialize distance sensors
    distance_sensors = []
    for i in range(8):
        distance_sensor = robot.getDevice('ds' + str(i))
        distance_sensor.enable(TIMESTEP)
        distance_sensors.append(distance_sensor)
        
    # Main control loop
    while robot.step(TIMESTEP) != -1:
        # Read light sensor values
        light_values = [sensor.getValue() for sensor in light_sensors]
        distance_values = [distance.getValue() for distance in distance_sensors]
        print("light_values" + str(light_values))
        # print("dis_values" + str(distance_values))
        left_speed = 0
        right_speed = 0
        
        # Implement Braitenberg logic here
        for i in range(8):
            if i < 4:
                left_speed += light_values[i] * (i + 1)
            else:
                right_speed += light_values[i] * (i + 1)
        
        # Avoid obstacles
        for i in range(8):
            if distance_sensors[i].getValue() > 500:
                if i < 4:
                    left_speed += 0.5 * distance_sensors[i].getValue()
                    right_speed -= 0.5 * distance_sensors[i].getValue()
                else:
                    right_speed += 0.5 * distance_sensors[i].getValue()
                    left_speed -= 0.5 * distance_sensors[i].getValue()
                break
        
        # Limit speeds to max speed
        left_speed = min(MAX_SPEED, max(-MAX_SPEED, left_speed))
        right_speed = min(MAX_SPEED, max(-MAX_SPEED, right_speed))
        
        # Set wheel speeds
        wheels[0].setVelocity(left_speed)
        wheels[1].setVelocity(right_speed)
            

if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)

