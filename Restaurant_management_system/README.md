"
# 🍽️ Restaurant Management System (LLD)

A complete low-level design of a restaurant management system in Python.

This project showcases clean OOP design, modular components, and the use of design patterns to handle real-world restaurant operations such as reservations, orders, payments, and role-based responsibilities.

---

## 🔧 Features

- ✅ Table reservation (with date & time conflict check)
- ✅ Order placement and modification (add, remove, update items)
- ✅ Role-based staff control (waiter vs manager)
- ✅ Payment processing via Strategy Pattern (Cash, Card)
- ✅ Singleton system controller
- ✅ Clean class responsibilities and file separation

---

## ▶️ Run Instructions

1. Navigate to this project:
   \`\`\`bash
   cd Restaurant_management_system
   \`\`\`

2. Run the main program:
   \`\`\`bash
   python main.py
   \`\`\`

---

## 📁 Folder Contents

- \`main.py\` - Entry point for testing
- \`menu.py\`, \`item.py\` - Menu and item models
- \`order.py\`, \`orderServices.py\` - Order logic
- \`reservation.py\`, \`reservationServices.py\`, \`reservationStatus.py\` - Reservation system
- \`staff.py\`, \`staffRole.py\`, \`staffServices.py\` - Staff handling
- \`payment.py\` - Payment strategy implementation
- \`table.py\` - Table entity with availability logic

---

## 🧠 Design Patterns Used

- **Singleton** — For core restaurant system instance
- **Strategy Pattern** — For payment methods (cash, card)
- **Enum** — For roles and reservation status
- **Role-based Access Control** — Enforced in service layer

---

## 🧑‍💻 Author

**@mrumayi20**

---
"
