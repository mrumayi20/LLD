from enum import Enum


class BookingStatus(Enum):
    HELD = 'HELD'
    CANCELLED = 'CANCELLED'
    CONFIRMED = 'CONFIRMED'
