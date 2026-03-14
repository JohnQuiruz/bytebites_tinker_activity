classDiagram
    class Customer {
        -String name
        -Transaction[] purchaseHistory
        +Customer(name String)
        +getName() String
        +setName(name String) void
        +getPurchaseHistory() Transaction[]
        +addTransaction(transaction Transaction) void
    }

    class FoodItem {
        -String name
        -Float price
        -String category
        -Float popularityRating
        +FoodItem(name String, price Float, category String)
        +getName() String
        +getPrice() Float
        +getCategory() String
        +getPopularityRating() Float
        +setPopularityRating(rating Float) void
    }

    class FoodItemCollection {
        -FoodItem[] items
        +FoodItemCollection()
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +filterByCategory(category String) FoodItem[]
    }

    class Transaction {
        -FoodItem[] items
        +Transaction()
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +computeTotal() Float
    }

    Customer "1" --> "0..*" Transaction : places
    Transaction "1" --> "1..*" FoodItem : contains
    FoodItemCollection "1" o-- "0..*" FoodItem : stores