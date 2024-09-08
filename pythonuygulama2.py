import math

# 2D koordinatları demet (tuple) olarak içeren noktalar listesini tanımlayın
points = [(1, 2), (4, 6), (5, 9), (3, 4), (8, 1)]

# İki nokta arasındaki Öklid mesafesini hesaplayan fonksiyon
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Her nokta çifti arasındaki mesafeleri hesaplayın
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulun
min_distance = min(distances)

# Minimum mesafeyi yazdırın
print("Minimum Öklid mesafesi:", min_distance)
