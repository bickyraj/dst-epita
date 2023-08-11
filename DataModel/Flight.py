class Flight:
    icao24: str
    firstSeen: int
    estDepartureAirport: str
    lastSeen: int
    estArrivalAirport: str
    callsign: str
    estDepartureAirportHorizDistance: int
    estDepartureAirportVertDistance: int
    estArrivalAirportHorizDistance: int
    estArrivalAirportVertDistance: int
    departureAirportCandidatesCount: int
    arrivalAirportCandidatesCount: int

    def __init__(self, icao24, firstSeen, estDepartureAirport, lastSeen,
                 estArrivalAirport, callsign, estDepartureAirportHorizDistance,
                 estDepartureAirportVertDistance, estArrivalAirportHorizDistance,
                 estArrivalAirportVertDistance, departureAirportCandidatesCount,
                 arrivalAirportCandidatesCount):
        self.icao24 = icao24
        self.firstSeen = firstSeen
        self.estDepartureAirport = estDepartureAirport
        self.lastSeen = lastSeen
        self.estArrivalAirport = estArrivalAirport
        self.callsign = callsign
        self.estDepartureAirportHorizDistance = estDepartureAirportHorizDistance
        self.estDepartureAirportVertDistance = estDepartureAirportVertDistance
        self.estArrivalAirportHorizDistance = estArrivalAirportHorizDistance
        self.estArrivalAirportVertDistance = estArrivalAirportVertDistance
        self.departureAirportCandidatesCount = departureAirportCandidatesCount
        self.arrivalAirportCandidatesCount = arrivalAirportCandidatesCount

    def __repr__(self):
        return f"Flight(icao24='{self.icao24}', firstSeen={self.firstSeen}, estDepartureAirport='{self.estDepartureAirport}', " \
               f"lastSeen={self.lastSeen}, estArrivalAirport='{self.estArrivalAirport}', callsign='{self.callsign}', " \
               f"estDepartureAirportHorizDistance={self.estDepartureAirportHorizDistance}, " \
               f"estDepartureAirportVertDistance={self.estDepartureAirportVertDistance}, " \
               f"estArrivalAirportHorizDistance={self.estArrivalAirportHorizDistance}, " \
               f"estArrivalAirportVertDistance={self.estArrivalAirportVertDistance}, " \
               f"departureAirportCandidatesCount={self.departureAirportCandidatesCount}, " \
               f"arrivalAirportCandidatesCount={self.arrivalAirportCandidatesCount})"