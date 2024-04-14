from enum import Enum


class BreweryType(str, Enum):
    micro = "micro"
    nano = "nano"
    regional = "regional"
    brewpub = "brewpub"
    large = "large"
    planning = "planning"
    bar = "bar"
    contract = "contract"
    proprietor = "proprietor"
    closed = "closed"