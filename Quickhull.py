def quickhull(s):
    # If the length is 2 or less than a convex hull can't be reached so return value
    if len(s) <= 2:
        return s
    p1 = min(s) # Finding minimum point
    p2 = max(s) # Finding maximum point
    convex_hull = [] # Initialising convex hull
    
    # Recursively finds the hull above the line
    findHull(s, p1, p2, convex_hull, "above") 
    
    # Recursively finds the hull below the line
    findHull(s, p1, p2, convex_hull, "below")
    
    # Prints the convex hull
    print(convex_hull)

def findHull(s, p1, p2, hull, segment):
    # Converts above and below into numbers as it will be easier later to get sides
    if segment == "above":
        segment = 1
    if segment == "below":
        segment = -1
        
    segmentPoints = [] # Initialises sidePoints
    # For every point in s will be used to calculate side
    for i in s:
        v = i # Just a temp value to be used 
        calc_segment = onSegment(p1, p2, v) # Calculation done in side function
        # Gets the points on the side chosen so either above and below
        if calc_segment == segment:
            segmentPoints.append(v)
    
    # Points found on the side
    if len(segmentPoints) > 0:
        all_dist = [] # Initialises all distances
        for i in segmentPoints:
            v = i # Just a temp value to be used 
            dist = distance(p1, p2, v) # Distance calculation
            all_dist.append(dist) # Appending to a list
        points = dict(zip(segmentPoints, all_dist)) # Zips the points and distances together
        
        # Finds the max value of the point using the distances
        max_point = max(points, key = points.get)
        
        # Values to make the the code readible for the next section
        A = -onSegment(max_point, p1, p2)
        B = -onSegment(max_point, p2, p1)
        
        # This is to apply findHull on max point to p1
        findHull(s, max_point, p1, hull, A)
        
        # This is to apply findHull on max point to p2
        findHull(s, max_point, p2, hull, B)
    
    # No points found on side of line
    else:
        # p1 not in hull will append to hull
        if p1 not in hull:
            hull.append(p1)
        
        # p2 not in hull will append to hull
        elif p2 not in hull:
            hull.append(p2)

def onSegment(p1, p2, p3):
    # Calculating distance from p3 and the line p1 to p2
    A = (p3[1] - p1[1]) * (p2[0] - p1[0])
    B = (p2[1] - p1[1]) * (p3[0] - p1[0])
    segment =  A - B
    
    # Calculating if its on the side
    if segment != 0:
        return segment // abs(segment)
    else:
        return 0 

def distance(p1, p2, p3):
    # Calculating distance from p3 and the line p1 to p2
    A = (p3[1] - p1[1]) * (p2[0] - p1[0])
    B = (p2[1] - p1[1]) * (p3[0] - p1[0])
    return abs(A - B)

def distance(p1, p2, p3):
    # Calculating distance from p3 and the line p1 to p2
    A = (p3[1] - p1[1]) * (p2[0] - p1[0])
    B = (p2[1] - p1[1]) * (p3[0] - p1[0])
    return abs(A - B)