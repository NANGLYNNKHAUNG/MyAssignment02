""" ARAP Webots main file """  
import robot  
def main():  

    red = 0  
    green = 0  
    blue = 0  
    range = 0.0  
    robot1 = robot.ARAP()  
    robot1.init_devices()  

    v1 = True  
    v2 = True   
    v3 = True
    v4 = True   
    v5 = True   
    summary = []  

    while True:  
        robot1.reset_actuator_values()  
        range = robot1.get_sensor_input()  
        robot1.blink_leds()  
        red, green, blue = robot1.get_camera_image(5)  

    # Printing only once and pushing string in list data structure                
        if v1 == True:  
            if 150 < red < 160:
               print("I see Red!")  
               v1 = False                        
               summary.append('Red')  
               print("Summary :", summary)    

        if v2 == True:   
            if 180 < green <= 200: 
               print("I see Green!")  
               v2 = False  
               summary.append('Green')   
               print("Summary :",summary)    

        if v3 == True:         
            if 180 < blue <= 200:
               print("I see Blue!")  
               v3 = False   
               summary.append('Blue')   
               print("Summary :",summary)   

        if v4 == True:         
            if 150 < blue <= 170: 
               print("I found water!")  
               v4 = False  
               summary.append('water')   
               print("Summary :",summary)    

        if v5 == True :         
            if 150 < green <= 170: 
               print("I found food!")  
               v5 = False   
               summary.append('food')   
               print("Summary :",summary)       

        if robot1.front_obstacles_detected():  
            robot1.move_backward()  
            robot1.turn_left()  

        else:  

            robot1.run_braitenberg()  
            robot1.set_actuators()  
            robot1.step()  

if __name__ == "__main__":  

    main() 