# ByteBites Backend Feature Request

We need to build the backend logic for the ByteBites app.

## Client Feature Request
> We need to build the backend logic for the ByteBites app. The system needs to manage our customers, tracking their names and their past purchase history so the system can verify they are real users.
>
> These customers need to browse specific food items (like a "Spicy Burger" or "Large Soda"), so we must track the name, price, category, and popularity rating for every item we sell.
>
> We also need a way to manage the full collection of items — a digital list that holds all items and lets us filter by category such as "Drinks" or "Desserts".
>
> Finally, when a user picks items, we need to group them into a single transaction. This transaction object should store the selected items and compute the total cost. 

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