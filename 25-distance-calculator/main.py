from dataclasses import dataclass
from geopy.geocoders import Nominatim
from geopy.distance import geodesic


@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude


def get_coordinates(adress: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent="distance_calculator")
    location = geolocator.geocode(adress)

    if location:
        return Coordinates(latitude=location.latitude, longitude=location.longitude)


def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    if home and target:
        distance: float = geodesic(home.coordinates(), target.coordinates()).kilometers
        return distance


def get_distance_km(home: str, target: str) -> float | None:
    home_coordinates: Coordinates = get_coordinates(home)
    target_coordinates: Coordinates = get_coordinates(target)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f"{home} -> {target}")
        print(f"{distance:.2f} quilômetros")
        return distance
    else:
        print("Falha ao calcular a distância...")


def main():
    home_address: str = "Rua Jalde Antonio Fragoso 510, Iguape/SP, Brazil"
    target_address: str = "Rua Projetada 50, Jacupiranga/SP, Brazil"
    get_distance_km(home=home_address, target=target_address)


if __name__ == "__main__":
    main()
