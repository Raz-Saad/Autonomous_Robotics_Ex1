class DistanceSensor:
    def __init__(self, sensor_direction, distance=0):
        self.distance = distance  # the distance from an obstacle
        self.direction = sensor_direction  # forward, backward, left, right

    # update the current distance from an obstacle using the map and drone's position
    def update_values(self, map_matrix, location_on_map, drone_orientation):
        max_range = 120  # 3 meters in pixels (3 meters / 0.025 meters per pixel)
        directions = {
            "forward": (0, -1),
            "backward": (0, 1),
            "leftward": (-1, 0),
            "rightward": (1, 0)
        }
        dx, dy = directions[self.direction]
        drone_x, drone_y = location_on_map
        drone_radius = 10  # Assuming drone radius is 10 cm

        sensor_x = drone_x - drone_radius if dx < 0 else drone_x + drone_radius
        sensor_y = drone_y - drone_radius if dy < 0 else drone_y + drone_radius

        for dist in range(1, max_range + 1):
            nx, ny = int(sensor_x + dx * dist), int(sensor_y + dy * dist)
            if nx < 0 or nx >= len(map_matrix[0]) or ny < 0 or ny >= len(map_matrix):
                self.distance = dist * 2.5  # Distance in cm
                return
            if map_matrix[ny][nx] == 1:
                self.distance = dist * 2.5  # Distance in cm
                return
        self.distance = max_range * 2.5  # If no obstacle is found within range