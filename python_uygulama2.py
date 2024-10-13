import math
import ast

def main():
    #default testcase
    points = [(1, 2), (4, 6), (3, 1), (7, 3)]
    
    user_in = input("Enter points as tuples (e.g., (1, 2), (4, 6), (3, 1), (7, 3)), or press Enter to use default points: ")
    
    if user_in.strip():  
        try:        
            points = ast.literal_eval(user_in)
            if not all(isinstance(point, tuple) and len(point) == 2 for point in points):
                raise ValueError("All points must be tuples of two coordinates.")
        except Exception as e:
            print("Invalid input. Using default test case points.")

    distances = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            distance = euclideanDistance(points[i], points[j])
            distances.append(distance)

    #checking if distances exists 
    if distances:
        minimum = min(distances)
        print(f"The minimum distance is: {minimum}")
    else:
        print("No distances to calculate.")

    return minimum

def euclideanDistance(pt1, pt2):
    
    result = math.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)
    return result

main()
