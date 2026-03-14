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

    class Transaction {
        -FoodItem[] items
        +Transaction()
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +computeTotal() Float
    }

    class FoodItem {
        -String name
        -Float price
        -String category
        -Float popularityRating
        +FoodItem(name String, price Float, category String, popularityRating Float)
        +getName() String
        +getPrice() Float
        +getCategory() String
        +getPopularityRating() Float
    }

    class FoodItemCollection {
        -FoodItem[] items
        +FoodItemCollection()
        +addItem(item FoodItem) void
        +getItems() FoodItem[]
        +filterByCategory(category String) FoodItem[]
    }

    Customer "1" --> "0..*" Transaction : places
    Transaction "1" --> "1..*" FoodItem : contains
    FoodItemCollection "1" o-- "0..*" FoodItem : stores

---

## Architect's Note

### Construction and mutation strategy

The previous revision exposed a real incoherence: getters were applied everywhere but there was no defined way to set initial state on any object. Every private field was a dead end. This revision fixes that with a uniform rule and also addresses the question of where setters belong.

**The governing rule: every private field has exactly one entry point -- a constructor parameter for fields that define what the object IS, a mutator method for fields that change or accumulate over the object's lifetime. The spec language determines which category a field falls into.**

#### Per-class breakdown

**FoodItem** -- All four fields are constructor parameters: `FoodItem(name, price, category, popularityRating)`. No setters. The spec says "for each food item, track: name, price, category, popularity rating." These properties define the item. A Spicy Burger at $8.99 in the Burgers category is a complete, self-describing entity from the moment it is created. The spec provides no scenario where these fields change after creation. If the business needs to update menu pricing, that is an admin/catalog concern that would warrant a separate class or service -- not mutation on the domain object that customers browse and transactions reference.

**Customer** -- `name` is a constructor parameter AND has a setter. The spec says "the system should manage customers by tracking customer name." The word "manage" implies lifecycle operations -- customers are created, maintained, potentially updated. Names can have typos. People change names. A constructor sets the initial value; `setName()` allows correction. `purchaseHistory` starts empty and grows via `addTransaction()` -- it is an accumulating collection, not an intrinsic property.

**Transaction** -- No-arg constructor. A transaction begins empty and is assembled incrementally via `addItem()`. The spec says "when a user picks items, group them into a single transaction" -- this describes a process of accumulation, not atomic creation. No setters needed because there are no intrinsic fields; the items list is the entire substance of a transaction and it is built through its mutator.

**FoodItemCollection** -- No-arg constructor. Same reasoning as Transaction: it is a container that starts empty and is populated via `addItem()`. No intrinsic identity, no fields to set at construction beyond an empty list.

#### Why Customer gets a setter but FoodItem does not

This is not arbitrary. The spec uses different verbs for different entities:

- "**Manage** customers by tracking name" -- manage implies create, read, update. Setters are appropriate.
- "For each food item, **track**: name, price, category, popularity rating" -- track implies record and read. Food items are catalog data browsed by customers and referenced by transactions. The spec never describes modifying a food item after creation.

If a FoodItem's price changes, the business creates a new FoodItem (or a separate admin service handles catalog updates). The domain model that customers interact with treats food items as fixed reference points. This is not an assumption -- it follows from the spec giving no mutation scenario for food items while explicitly using "manage" for customers.

### What changed from the previous revision

1. **Added constructors to all four classes.** Core fix carried forward. Every class now has an explicit constructor.

2. **Added `setName()` to Customer.** The previous revision treated `name` as set-once constructor data, same as FoodItem fields. But Customer and FoodItem have different lifecycles in the spec. "Manage customers" implies mutability. This is now reflected.

3. **Added `addTransaction()` to Customer.** Carried forward from the previous revision. Without this, purchase history could never grow.

### What was kept and why

- The four candidate classes, relationships, cardinalities, and composition/aggregation choices are unchanged. These have been correct since the first revision.
- No setters on FoodItem. Justified by spec language, not by special-case reasoning.
- No `removeItem()` methods. Spec does not require removal.

### What was considered and rejected

- **No-arg constructor for Customer with setName() as the only entry point for name.** This would allow a Customer to exist without a name -- a nameless customer is not a valid entity per the spec. The constructor enforces that every Customer has a name from birth. The setter allows it to change after.

- **Setters on FoodItem.** Addressed above. The spec draws a clear line between "manage" (Customer) and "track" (FoodItem). Setters on FoodItem would misrepresent the domain.

- **Constructor with items for Transaction, e.g., `Transaction(items FoodItem[])`.** The spec describes incremental item selection ("picks items, group them"), not batch creation. `addItem()` models the real workflow.

### Risks and flags

- **Customer identity is underspecified.** `Customer(name)` creates a customer, but names are not unique identifiers. The spec mentions "verify that users are legitimate customers" with no mechanism for doing so. The team needs to decide if an ID or other unique field is required before implementation.

- **FoodItem popularity rating source is still undefined.** It is a required constructor parameter now, so the caller must provide it. Computed from transaction history? Manually curated? Business-defined? The spec is silent and implementation cannot proceed without an answer.

- **Transaction finalization is not modeled.** The diagram shows `addItem()` but no concept of a transaction being "complete" or "submitted." Right now, a Transaction can have items added to it indefinitely. If the system needs to distinguish between in-progress and finalized transactions, that will require either a state field or a separate type. The spec does not require this distinction, so it is not modeled -- but flagging it as a likely future need.
