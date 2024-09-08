import math

# Define the list of points (2D coordinates as tuples)
points = [(1, 2), (4, 6), (5, 9), (3, 4), (8, 1)]

# Function to calculate Euclidean distance between two points
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Calculate distances between each pair of points
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Find the minimum distance
min_distance = min(distances)

# Output the minimum distance
print("The minimum Euclidean distance is:", min_distance)
