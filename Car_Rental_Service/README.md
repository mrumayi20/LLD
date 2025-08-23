# Car Rental Service - Low Level Design (LLD)

This project is a Low-Level Design (LLD) of a car rental system implemented in Python using object-oriented principles and standard design patterns. It simulates a simplified rental platform that allows customers to reserve cars, process payments, and manage availability.

## Project Goal

To create a backend system that enables customers to:

- Search available cars based on criteria
- Book cars for specific dates
- Prevent double bookings
- Pay using different strategies (Cash or Card)
- Cancel or modify bookings if needed

## Features

- Search cars by price or capacity
- Book cars for a range of dates
- Prevent overlapping (double) bookings
- Cancel or modify bookings
- Choose between cash or card payments
- Maintain customer data (name, email, license)

## Key Components & Design Patterns

| Component        | Description                                                |
| ---------------- | ---------------------------------------------------------- |
| Car              | Car details, availability, and pricing                     |
| Customer         | Customer information                                       |
| Booking          | Booking details (dates, amount, status)                    |
| PaymentStrategy  | Strategy for choosing between Cash or Card payments        |
| SearchStrategy   | Strategy for searching cars by price or capacity           |
| RentalService    | Core service that handles bookings and availability checks |
| CarRentalService | Singleton controller that brings all components together   |

### Design Patterns Used

- **Singleton**: `CarRentalService` — ensures a single shared service instance
- **Strategy**: `PaymentStrategy`, `SearchStrategy` — enables flexible behavior for payment and searching

## Folder Structure

```
Car_Rental_Service/
├── booking.py
├── bookingStatus.py
├── car.py
├── carRentalService.py
├── customer.py
├── main.py
├── payment.py
├── rentalService.py
└── searchStrategy.py
```

## How to Run

### Requirements

- Python 3.8 or higher

### Run the demo

```bash
python main.py
```

This will:

- Add sample cars and customers
- Search cars by price or capacity
- Book a car
- Block overlapping bookings
- Cancel a booking and retry

## Future Enhancements

These are not implemented but can be added easily:

- Admin module (add/remove cars)
- GUI / REST API (Flask, FastAPI)
- Pickup & drop locations
- Email or SMS notifications
- Booking history and reporting
- Discount code or coupon support

## Purpose

This project is designed for:

- Practicing Object-Oriented Design
- Demonstrating use of design patterns
- Building a real-world LLD system
- Interview preparation (LLD rounds)

## Author

GitHub: https://github.com/mrumayi20  
Project: Car Rental Service — Python LLD
