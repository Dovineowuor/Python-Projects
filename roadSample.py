def load_road_network(filename):
    # Open the file containing the intersection and roads info
    f = open(filename)
    # Read all the lines from the file
    lines = f.readlines()

    # Create empty dictionaries for intersection and road_cost
    intersections = {}
    roads_cost = {}

    # Markers to know what information are we reading from file
    # intersection = True => lines being read contain intersection information
    # roads = True => lines being read contain road information
    intersection = False
    roads = False

    # intersection_num only valid when intersection = True
    # Tells us that the line being read contain intersection information for which intersection #
    intersection_num = None

    # Go through each line in lines
    for line in lines:
        # Remove newlines at the end (otherwise we will see '\n' characters)
        line = line.strip()

        # Make sure we skip blank lines
        if(not len(line)==0):
            # If Intersection word is present in line we set intersection marker to True and road marker to False
            # and intersection_num to the last digit of the line
            if('Intersection' in line):
                # intersection_num is the last digit of the line i.e. #Intersection:0, 0 is the intersection_num

                intersection_num = int(line[-1])
                intersections[intersection_num] = []
                intersection = True
                roads = False
                # go to next iteration of loop
                continue
            # If Roads word is present in line we set roads marker to True and intersection marker to False
            if('Roads' in line):
                intersection = False
                roads = True
                # go to next iteration of loop
                continue
            # If intersection marker is set
            if(intersection):
                # Create an empty list to store intersection information
                lst = []
                # Each intersection list is separated by ';'
                for x in line.split(';'):
                    # After separating the intersection we convert it to tuple i.e. '(4,3)' will be converted to (4,3)
                    lst.append(eval(x))
                # Put the intersection list to the intersection dictionary
                intersections[intersection_num].append(lst)
            # If road marker is set
            if(roads):
                # Put the road cost information in the dictionary
                # eval again is used to conver string to tuple
                roads_cost[eval(line.split(':')[0])] = int(line.split(':')[1])
    # close the file
    f.close()

    # return the dictionaries
    return intersections, roads_cost
