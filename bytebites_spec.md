# ByteBites Backend Feature Request

We need to build the backend logic for the ByteBites app.

## Customer Management
The system should manage customers by tracking:
- Customer name
- Past purchase history

This helps verify that users are legitimate customers.

## Food Item Data
Customers need to browse specific food items (for example, "Spicy Burger" and "Large Soda").

For each food item, track:
- Name
- Price
- Category
- Popularity rating

## Item Collection / Menu
We need a digital list of all food items that can:
- Store the full collection of items
- Filter items by category (for example, "Drinks" or "Desserts")

## Transactions
When a user picks items, group them into a single transaction.

Each transaction should:
- Store selected items
- Compute the total cost

## Candidate Classes
The system must model the following core data objects the system needs:
- Customer
- Food Item
- Food Item Collection
- Transaction