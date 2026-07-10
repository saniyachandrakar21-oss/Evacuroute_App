from loader.building_loader import BuildingLoader
from hazards.hazard_manager import HazardManager
from routing.pathfinder import PathFinder

# Load building
graph = BuildingLoader.load("data/building_data.json")

print("===== BUILDING LOADED =====")
graph.display_summary()

# Get current location
current = input("\nEnter Your Current Location: ").strip()

# Validate current location
if current not in graph.nodes:
    print("\nInvalid Current Location!")
    exit()

# Get fire locations
fires = input("Enter Fire Location(s) (comma separated): ").split(",")

# Apply hazards
for fire in fires:
    fire = fire.strip()

    if fire not in graph.nodes:
        print(f"\nInvalid Fire Location: {fire}")
        exit()

    HazardManager.apply_fire(graph, fire)

print("\n===== UPDATED BUILDING =====")
graph.display_summary()

# Run Dijkstra Algorithm
distances, previous = PathFinder.shortest_path(graph, current)

# Find nearest exit
exit_node = PathFinder.nearest_exit(graph, distances)

print("\nNearest Exit:", exit_node)

if exit_node is not None:

    path = PathFinder.get_path(previous, exit_node)

    print("\n===== SAFE EVACUATION ROUTE =====\n")
    print("  →  ".join(path))

    print(f"\nTotal Distance : {distances[exit_node]:.2f} meters")

else:

    shelter = PathFinder.find_shelter(graph, distances)

    if shelter is not None:

        shelter_path = PathFinder.get_path(previous, shelter)

        print("\n===== SHELTER IN PLACE =====\n")

        print("Suggested Shelter :", shelter)

        print("\nRoute")

        print("  →  ".join(shelter_path))

        print(f"\nDistance : {distances[shelter]:.2f} meters")

    else:

        print("\nNo Safe Exit or Shelter Available!")