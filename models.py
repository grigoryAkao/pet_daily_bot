from datetime import datetime

class Train:
    def __init__(self, departure, arrival, train_type, from_station, to_station):

        self.train_type: str = train_type
        self.from_station: str = from_station
        self.to_station: str = to_station
        self.departure = datetime.fromisoformat(departure)
        self.arrival = datetime.fromisoformat(arrival)


    def __str__(self):
        return f"""Электичка типа "{self.train_type}" со станции {self.from_station} отправляется:
{self.departure.date()} в {self.departure.time()}
и прибывает на станцию {self.to_station}:
в {self.arrival.time()}"""