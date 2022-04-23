
from matplotlib import pyplot as plt
from Obstacle import *
from Vehicle import *
import plot

def in_bound_region(Vehicle):
    '''
    Check if the Vehicle has reached within the Goal Bounds
    '''
    if Vehicle.distance(Vehicle.state,Vehicle.goal) < vehicle.goal_bound:
        if vehicle.goal_list:
            # print("Goal Update",Vehicle.distance(Vehicle.state,Vehicle.goal))
            vehicle.goal = vehicle.goal_list.pop(0)
            vehicle.goal[2] *= np.pi/180
            if not vehicle.goal_list:
                vehicle.goal_bound = vehicle.size
        else:
            return True
    return False


def end_loop(Vehicles):
    '''
    Takes in the list of Vehicle Objects. 
    Returns True if All vehicles are in bound region
    Returns False if vehicles >=1 hasn't reached goal

    Can be expanded to add collision detection
    '''
    flag = True
    for vehicle in Vehicles:
        if not in_bound_region(vehicle):
            flag = False
    return flag

if __name__== '__main__':
    
    # Experiment No
    Experiment_No = 3
    # Simulation Parameters:
    sampling_time = 0.2
    prediction_horizon = 15

    '''
    Define the Obstacles (Read Obstacle Class for Better understanding)
    Sample:
    Obstacle_"Name" = Obstacle  (id, 
                                "Obstacle Type",
                                ["X Position", "Y Position", "Radius", "Velocity(Km/h)", "Angle(Deg)"], 
                                "Sampling Time", 
                                "Image Path",
                                "Color of Obstacle",
                                "Zoom for the Photo")
    '''

    # Obstacle_1 = Obstacle(1, 
    #                      "Static", 
    #                      [1000, 50, 2, 0, 0], 
    #                      sampling_time) 
    #                     #  "../Object_Photos/police.png"
                        #  )
    Obstacle_1 = Obstacle(1, "Static", [90, 45.0, 1.0, 0, 0], sampling_time)
    # Obstacle_1 = Obstacle(1, "Dynamic", [0.0, 0.0, 2.0, 31, 45], sampling_time, "../Object_Photos/police.png")
    # Obstacle_2 = Obstacle(2, "Dynamic", [200.0, 0.0, 2.0, 30.0, 155], sampling_time, "../Object_Photos/taxi.png")                        
    # Obstacle_2 = Obstacle(2, "Static", [110, 25, 2, 0, 0], sampling_time)
    # Obstacle_3 = Obstacle(3, [50, 50, 2, 0, 0])
    # Obstacle_4 = Obstacle(4, [ 50, 50, 2, 10, 270], "Dynamic", "../Object_Photos/police.png")
    # Obstacle_5 = Obstacle(5, [ 25, 50, 2, 10, -90], "Dynamic", "../Object_Photos/police.png")
    # Obstacles = []
    # for i in range(10):
    #     for j in range(1):
    #         Obstacles.append(Obstacle(i+j, "Static", [i*5+50, j*5+50, 1, 0, 0], sampling_time))

    #Form a List (Do not forget to add Obstacles in this list)
    Obstacles = [Obstacle_1]

    '''
    Define the Vehicle (Read Vehicle Class for Better understanding)
    Sample:
    Vehicle_"Name" = Vehicle("id",
                            "Start States", 
                            "Goal States",
                            "Initial Control Input",
                            "Velocity Limit(Km/h)",
                            "Steering Rate Limit (Deg/s)",
                            "Start Time",
                            "Sampling Time",
                            "Prediction Horizon 
                            ["Obstacle 1","Obstacle 2", ... ] 
                            ["Static Offset Region", "Dynamic Offset Region"]
                            "Color of Path/Vehicle"
                            "Image Path"
                            "Zoom for the Photo")
    '''
    # Define Start, Goal States and Control Input 
    # (States include x,y position, orientation, steering angle)
    # (Inputs Include velocity and steering angle)
    
    # Start_1 = [0.0, 90.0, 0.0, 0.0]
    # Goal_1 = [[45.0, 90.0, 0.0, 0.0], [135.0, 0.0, 0.0, 0.0], [180.0, 0.0, 0.0, 0.0]] #[90.0 ,45.0, 0.0, 0.0]
    # inital_control_input_1 = [25.0,0.0]

    Start_1 = [51.0, 22.5, 30.0, 0.0]
    Goal_1 = [[129.0, 67.5, 30.0, 0.0]] #, [135.0, 0.0, 0.0, 0.0], [180.0, 0.0, 0.0, 0.0]] #[90.0 ,45.0, 0.0, 0.0]
    inital_control_input_1 = [20.0,0.0]

    start_time_1 = 0

    start_time_1 = 0
    Vehicle_1 = Vehicle(1, 
                        Start_1,Goal_1, 
                        inital_control_input_1, 
                        120.0, 10, 30,
                        start_time_1, 
                        sampling_time, 
                        prediction_horizon, 
                        [Obstacle_1], 
                        [40, 80], 
                        "#f1c40f", 
                        "../Object_Photos/aventador_y.png", 
                        ZOOM=0.018)
    
    Start_2 = [129.0, 22.5, 150.0, 0.0]
    Goal_2 = [[51.0, 67.5, 150.0, 0.0]] #,[45.0, 90.0, 180.0, 0.0], [0.0, 90, 180.0, 0.0]] #, [135.0, 0.0, 0.0, 0.0], [180.0, 0.0, 0.0, 0.0]] #[90.0 ,45.0, 0.0, 0.0]
    inital_control_input_2 = [20.0,0.0]

    start_time_2 = 0

    Vehicle_2 = Vehicle(2, 
                        Start_2,Goal_2, 
                        inital_control_input_2, 
                        120.0, 10, 30,
                        start_time_2, 
                        sampling_time, 
                        prediction_horizon, 
                        [Obstacle_1], 
                        [40, 80], 
                        "#f50116", 
                        "../Object_Photos/ferrari_2.png", 
                        ZOOM=0.045)

    Start_3 = [90.0, 90.0, 270.0, 0.0]
    Goal_3 = [[90.0, 0.0, 270.0, 0.0]]#,[45.0, 90.0, 180.0, 0.0], [0.0, 90, 180.0, 0.0]] #, [135.0, 0.0, 0.0, 0.0], [180.0, 0.0, 0.0, 0.0]] #[90.0 ,45.0, 0.0, 0.0]
    inital_control_input_3 = [20.0,0.0]

    start_time_3 = 0

    Vehicle_3 = Vehicle(3, 
                        Start_3,Goal_3, 
                        inital_control_input_3, 
                        120.0, 10, 30,
                        start_time_3, 
                        sampling_time, 
                        prediction_horizon, 
                        [Obstacle_1], 
                        [40, 80], 
                        "#003b77", 
                        "../Object_Photos/aventador_b.png", 
                        ZOOM=0.022)
    # Start_2 = [45.0, 0.0, 90.0, 0.0]
    # Goal_2 = [45.0, 90.0, 90.0, 0.0]
    # inital_control_input_2 = [15.0,0.0]
    # start_time_2 = 0
    # Vehicle_2 = Vehicle(2, 
    #                     Start_2,Goal_2, 
    #                     inital_control_input_2, 
    #                     120.0, 10,
    #                     start_time_2, 
    #                     sampling_time, 
    #                     prediction_horizon, 
    #                     [Obstacle_1, Obstacle_2], 
    #                     [40, 80], 
    #                     "#f50116", 
    #                     "../Object_Photos/ferrari_2.png", 
    #                     ZOOM=0.058)
    
    # Start_3 = [90.0, 45.0, 180.0, 0.0]
    # Goal_3 = [0.0, 45.0, 180.0, 0.0]
    # inital_control_input_3 = [15.0,0.0]
    # start_time_3 = 0
    # Vehicle_3 = Vehicle(3, 
    #                     Start_3,Goal_3, 
    #                     inital_control_input_3, 
    #                     120.0, 10,
    #                     start_time_3, 
    #                     sampling_time, 
    #                     prediction_horizon, 
    #                     [Obstacle_1, Obstacle_2], 
    #                     [40, 80], 
    #                     "#79a824", 
    #                     "../Object_Photos/aventador_g.png", 
    #                     ZOOM=0.03)

    # Start_4 = [45.0, 90.0, 270.0, 0.0]
    # Goal_4 = [45.0, 0.0, 270.0, 0.0]
    # inital_control_input_4 = [15.0,0.0]
    # start_time_4 = 0
    # Vehicle_4 = Vehicle(4, 
    #                     Start_4,Goal_4, 
    #                     inital_control_input_4, 
    #                     120.0, 10,
    #                     start_time_4, 
    #                     sampling_time, 
    #                     prediction_horizon, 
    #                     [Obstacle_1], 
    #                     [40, 80], 
    #                     "#003b77", 
    #                     "../Object_Photos/aventador_b.png", 
    #                     ZOOM=0.03)
    # Start_C = [0.0, 50.0, 0.0, 0.0]
    # Goal_C = [100.0, 50.0, 0.0, 0.0]
    # inital_control_input_C = [10.0*5/18,0.0]
    # start_time_C = 0

    # Vehicle_C = Vehicle(3, Start_C,Goal_C, inital_control_input_C, 120.0*5/18, 10,start_time_C, Obstacles, 50, 100, "#003b77", "../Object_Photos/aventador_b.png", ZOOM=0.038)

    #Form a List (Do not forget to add all Vehicles in this list)
    Vehicles = [Vehicle_1, Vehicle_2, Vehicle_3] #, Vehicle_3, Vehicle_4]#, Vehicle_C]

    # Define Plot Limits
    fig, ax = plt.subplots()
    # fig.canvas.manager.full_screen_toggle()
    ax.set_xlim([-15, 195])
    ax.set_ylim([-10, 100])

    for vehicle in Vehicles:
        vehicle.global_plot(ax)
        for other_vehicle in Vehicles:
            if vehicle.id != other_vehicle.id:
                vehicle.Obstacles.append(other_vehicle)
    
    # Plot an background image on the graph
    # img = cv2.imread('road.jpg')		# this is read in BGR format
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)		# this converts it into RGB
    # ax.imshow(img, extent=[-10, 110,-5, 55])

    # Plot the Static Obstacles
    for obstacle in Obstacles:
        if obstacle.type == 'Static':
            obstacle.plot(ax)

    # Simulation Runs Till All Robots Do Not Reach Goal Configuration 
    while(not end_loop(Vehicles)): #not end_loop(Vehicles)):

        for vehicle in Vehicles:
            if not in_bound_region(vehicle):
                vehicle.optimizer()
                vehicle.bicycle_model(vehicle.control_input[0], vehicle.control_input[1], True)
                
        for obstacle in Obstacles:
            if obstacle.type == 'Dynamic':
                obstacle.Model()

        plot.plot_simulation(Vehicles, Obstacles, ax)

    plot.plot_simulation(Vehicles, Obstacles, ax, True, False, Experiment_No)
    plot.save_graph(Vehicles, Experiment_No)











