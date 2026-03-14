classDiagram
    class Customer {
        -String name
        -Transaction[] purchaseHistory
        +getPurchaseHistory() Transaction[]
    }

    class Transaction {
        -FoodItem[] items
        +computeTotal() Float
    }

    class FoodItem {
        -String name
        -Float price
        -String category
        -Float popularityRating
    }

    class FoodItemCollection {
        -FoodItem[] items
        +filterByCategory(category String) FoodItem[]
    }

    Customer "1" --> "0..*" Transaction : places
    Transaction "1" --> "1..*" FoodItem : contains
    FoodItemCollection "1" o-- "0..*" FoodItem : stores