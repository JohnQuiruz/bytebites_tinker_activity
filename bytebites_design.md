classDiagram
    class Category {
        <<enumeration>>
        BURGERS
        DRINKS
        DESSERTS
        SIDES
    }

    class Customer {
        -String id
        -String name
        -Transaction[] purchaseHistory
        +Customer(id String, name String)
        +getName() String
        +setName(name String) void
        +getPurchaseHistory() Transaction[]
        +addTransaction(transaction Transaction) void
    }

    class FoodItem {
        -String name
        -Float price
        -Category category
        -Float popularityRating
        +FoodItem(name String, price Float, category Category)
        +getName() String
        +getPrice() Float
        +getCategory() Category
        +getPopularityRating() Float
        +setPopularityRating(rating Float) void
    }

    class FoodItemCollection {
        -FoodItem[] items
        +FoodItemCollection()
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +filterByCategory(category Category) FoodItem[]
    }

    class Transaction {
        -String customerId
        -FoodItem[] items
        +Transaction(customerId String)
        +getCustomerId() String
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +computeTotal() Float
    }

    Customer "1" --> "0..*" Transaction : places
    Transaction "1" --> "1..*" FoodItem : contains
    FoodItemCollection "1" o-- "0..*" FoodItem : stores
    FoodItem ..> Category : uses
