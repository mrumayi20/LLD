from datetime import date

from item import Item
from menu import Menu
from orderServies import OrderServices
from reservationServices import ReservationServices
from restaurantManagementService import RestaurantManagementSystem
from staffRole import StaffRole
from staffServices import StaffServices
from payment import Payment, CashStrategy, CardStrategy

# --- SETUP ---
system = RestaurantManagementSystem.get_instance()

# Add tables
system.add_tables(table_no=1, capacity=4)
system.add_tables(table_no=2, capacity=2)

# Add staff
system.add_staff(name="Alice", role=StaffRole.WAITER)
system.add_staff(name="Bob", role=StaffRole.MANAGER)

waiter = system.staff[0]
manager = system.staff[1]

# Create menu and add items
menu = Menu()
burger = Item("Burger", 10)
pizza = Item("Pizza", 15)
coke = Item("Coke", 5)
menu.add_item_in_menu(burger)
menu.add_item_in_menu(pizza)
menu.add_item_in_menu(coke)

# Services
order_service = OrderServices()
reservation_service = ReservationServices()
staff_services = StaffServices(order_service, reservation_service)

# --- FLOW 1: Reservation Flow ---
print("\n--- FLOW 1: Reservation Flow ---")
date_today = date.today()
start_time = "18:00"
end_time = "20:00"
no_of_people = 2

table = system.find_available_table(capacity=no_of_people, date=date_today, start_time=start_time, end_time=end_time)

if table:
    reservation = staff_services.handle_reservation(
        staff=manager,
        table=table,
        name="John Doe",
        date=date_today,
        start_time=start_time,
        end_tme=end_time,
        no_of_people=no_of_people
    )
    print(f"Reservation confirmed for {reservation.cust_name} at table {reservation.table_no}")

    # Test cancellation
    reservation_service.cancel_reservation(reservation)
    print(f"Reservation for {reservation.cust_name} cancelled.")

    # Test reservation search
    try:
        found_reservations = reservation_service.search_reservation_by_name("John Doe")
        print(f"Found reservation: {found_reservations}")
    except Exception as e:
        print(e)

else:
    print("Reservation failed, no tables available.")

# --- FLOW 2: Walk-in Customer Ordering Food ---
print("\n--- FLOW 2: Walk-in Customer Ordering Food ---")

walkin_people_count = 2
walkin_start_time = "13:00"
walkin_end_time = "14:00"

available_table = system.find_available_table(
    capacity=walkin_people_count,
    date=date_today,
    start_time=walkin_start_time,
    end_time=walkin_end_time
)

if available_table:
    print(f"Table {available_table.get_table_no()} is available for walk-in customer.")

    # Take the order
    order = staff_services.take_order(
        staff=waiter,
        table_number=available_table.get_table_no(),
        ordered_items=[(burger, 1), (coke, 2)]
    )

    # Modify the order
    print("\n--- Order Modification ---")
    order.add_item(pizza, 1)
    print("Added 1 Pizza.")
    order.update_item_quantity(coke, 1)
    print("Updated Coke quantity to 1.")
    order.remove_item(burger)
    print("Removed Burger from order.")

    # Serve food
    staff_services.serve_food(staff=waiter)

    # Calculate and pay
    order.calculate_amount()
    print(f"Final order total: ${order.amount}")
    payment = Payment(CashStrategy())
    payment.make_payment(order.amount)

else:
    print("No available table for walk-in customer.")

# --- Additional Tests ---
print("\n--- Additional Tests ---")

# Menu item update
print("Updating Burger price to $12")
menu.update_meu_item_price(burger, 12)

print("Removing Coke from menu")
menu.remove_item_from_menu(coke)

# Role permission test
print("\n--- Permission Test ---")
try:
    # Waiter trying to make reservation (should fail)
    staff_services.handle_reservation(
        staff=waiter,
        table=system.tables[0],
        name="Unauthorized",
        date=date_today,
        start_time="21:00",
        end_tme="22:00",
        no_of_people=2
    )
except PermissionError as e:
    print(f"Expected error: {e}")
