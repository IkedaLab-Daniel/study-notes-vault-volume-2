# Implement programmability objects with SQL

# Introduction

## **SQL Server Programmability Objects**

SQL Server provides several **programmability objects** that encapsulate logic, improve code reuse, centralize business rules, and simplify database development.

The five core objects covered in this module are:

| Object                            | Main Purpose                                                               |
| --------------------------------- | -------------------------------------------------------------------------- |
| **Views**                         | Virtual tables that simplify data access and provide security boundaries   |
| **Stored Procedures**             | Reusable T-SQL code blocks for complex operations and data modifications   |
| **Scalar Functions**              | Reusable calculations that return a single value                           |
| **Table-Valued Functions (TVFs)** | Functions that return result sets usable in queries                        |
| **Triggers**                      | Automatically execute in response to data modifications or database events |

## **Scenario: E-commerce Database**

As an e-commerce company grows, database developers encounter several challenges:

| Problem                                                       | Desired Solution  |
| ------------------------------------------------------------- | ----------------- |
| Repeated `JOIN` queries across applications                   | Views             |
| Business logic scattered throughout application code          | Stored procedures |
| Data modifications requiring automatic validation and logging | Triggers          |
| Repeated complex calculations across queries                  | Functions         |

## **What You'll Learn**

- **Views:** Simplify data access and establish security boundaries.
- **Stored procedures:** Encapsulate complex operations and data modifications.
- **Scalar functions:** Perform reusable calculations that return one value.
- **Table-valued functions:** Return result sets that can be used within queries.
- **Triggers:** Automatically respond to data modifications or database events.

## **Key Takeaway**

Each programmability object serves a different purpose:

- **Views** simplify how data is accessed.
- **Stored procedures** centralize operations and business logic.
- **Functions** provide reusable calculations and query results.
- **Triggers** automate actions in response to database events.

The goal is to choose the appropriate object based on the requirements, improving maintainability, consistency, and security across database applications.

# Create View

## **Views in SQL Server**

A **view** is a virtual table defined by a `SELECT` statement. It doesn't store data itself; it retrieves data from underlying tables whenever queried.

### **1. Purpose and benefits**

- **Simplify complex queries:** Encapsulate complex `JOIN` clauses, calculations, and filters so applications can query a single view.
- **Security boundary:** Expose only specific columns or rows while restricting direct access to underlying tables.
- **Consistent data presentation:** Transform data into formats suited to different applications, users, or reporting needs.
- **Reusable logic:** Define query logic once instead of duplicating it across applications.

### **2. Create and query a view**

Use `CREATE VIEW` followed by a `SELECT` statement.

```
CREATE VIEW Sales.CustomerOrders
AS
SELECT
    c.CustomerID,
    c.CustomerName,
    c.Email,
    o.OrderID,
    o.OrderDate,
    o.TotalAmount
FROM Sales.Customers c
INNER JOIN Sales.Orders o
    ON c.CustomerID = o.CustomerID;
```

Query it like a regular table:

```
SELECT *
FROM Sales.CustomerOrders
WHERE CustomerName = 'Contoso Ltd';
```

The view executes its underlying `SELECT` and returns the results as if they came from one table.

### **3. Views with calculated columns**

Views can centralize calculations using expressions such as `CASE`.

```
CREATE VIEW Sales.OrderSummary
AS
SELECT
    OrderID,
    CustomerID,
    OrderDate,
    TotalAmount,
    CASE
        WHEN TotalAmount < 100 THEN 'Small'
        WHEN TotalAmount < 1000 THEN 'Medium'
        ELSE 'Large'
    END AS OrderSize
FROM Sales.Orders;
```

Every query against this view uses the same order categorization logic.

### **4. Design considerations**

| Practice                   | Purpose                                                                 |
| -------------------------- | ----------------------------------------------------------------------- |
| Specify columns explicitly | Avoid `SELECT *`; prevents unexpected results when base tables change.  |
| Use `WITH CHECK OPTION`    | Ensures modifications through a view satisfy its filtering conditions.  |
| Keep views focused         | Separate views by use case instead of creating one overly complex view. |

**Example:&#x20;**`WITH CHECK OPTION`

```
CREATE VIEW Sales.HighValueOrders
AS
SELECT
    OrderID,
    CustomerID,
    OrderDate,
    TotalAmount
FROM Sales.Orders
WHERE TotalAmount > 1000
WITH CHECK OPTION;
```

- An `INSERT` or `UPDATE` through this view must produce a row that satisfies `TotalAmount > 1000`.
- An order with `TotalAmount = 500` cannot be inserted through this view because it wouldn't be visible in the view.

### **5. When to use views**

Use views when you need to:

- Simplify complex queries shared by multiple applications or users.
- Restrict access to specific rows or columns.
- Present data in different formats for reporting or application requirements.
- Encapsulate reusable query logic **without parameters**.

### **6. Views vs. other database objects**

| Requirement                                                     | Recommended object                 |
| --------------------------------------------------------------- | ---------------------------------- |
| Simplify and reuse query logic without parameters               | Views                              |
| Physically store query results for performance-critical queries | Indexed views (materialized views) |
| Perform complex calculations that accept parameters             | User-defined functions             |
| Control data modification logic                                 | Stored procedures                  |

**Key takeaway:** Views bridge the gap between the physical database structure and the logical representation applications need. They simplify data access, centralize query logic, and provide a way to control which data users can see.

# Create stored procedures

## **Stored Procedures in SQL Server**

A **stored procedure** is a compiled collection of T-SQL statements stored and executed by SQL Server as a single unit.

It encapsulates business logic, validation rules, and database operations, allowing applications to interact with the database through reusable server-side code.

### **1. Purpose and benefits**

- **Performance:** Execution plans can be cached after the first execution, reducing repeated parsing and optimization overhead.
- **Code reusability:** Define database operations once and call them from multiple applications.
- **Reduced network traffic:** Execute multiple SQL statements on the server instead of sending individual queries.
- **Centralized business logic:** Keep validation and business rules inside the database.
- **Controlled data access:** Applications can execute procedures without needing direct access to underlying tables.

### **2. Create a basic stored procedure**

Use `CREATE PROCEDURE` followed by the procedure name and T-SQL statements.

```
CREATE PROCEDURE dbo.GetCustomerOrders
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        OrderID,
        CustomerID,
        OrderDate,
        TotalAmount
    FROM dbo.Orders
    ORDER BY OrderDate DESC;
END;
```

**Important:**

- `BEGIN` and `END` define the procedure body.
- `SET NOCOUNT ON` prevents row-count messages from being sent to the client, reducing network traffic.
- Use schema-qualified names such as `dbo.GetCustomerOrders`.

### **3. Work with parameters**

Parameters make procedures flexible and reusable.

**Input parameters (**`@`**)**

Accept values from the calling application. They can have default values, making them optional.

```
CREATE PROCEDURE dbo.GetCustomerOrdersByDate
    @CustomerID int,
    @StartDate datetime = NULL,
    @EndDate datetime = NULL
AS
BEGIN
    SET NOCOUNT ON;

    SELECT
        OrderID,
        OrderDate,
        TotalAmount
    FROM dbo.Orders
    WHERE CustomerID = @CustomerID
        AND (@StartDate IS NULL OR OrderDate >= @StartDate)
        AND (@EndDate IS NULL OR OrderDate <= @EndDate)
    ORDER BY OrderDate DESC;
END;
```

**Output parameters (**`OUTPUT`**)**

Return values from a procedure to the calling application.

```
CREATE PROCEDURE dbo.CalculateOrderTotal
    @OrderID int,
    @TotalAmount decimal(10,2) OUTPUT
AS
BEGIN
    SET NOCOUNT ON;

    SELECT @TotalAmount = SUM(Quantity * UnitPrice)
    FROM dbo.OrderDetails
    WHERE OrderID = @OrderID;

    RETURN 0;
END;
```

To receive an output parameter, declare a variable and specify `OUTPUT` when executing the procedure:

```
DECLARE @Total decimal(10,2);

EXEC dbo.CalculateOrderTotal
    @OrderID = 101,
    @TotalAmount = @Total OUTPUT;

SELECT @Total AS OrderTotal;
```

### **4. Implement error handling**

Use `TRY...CATCH` blocks to handle errors and maintain data integrity.

```
BEGIN TRY
    BEGIN TRANSACTION;

    -- Main operations

    COMMIT TRANSACTION;
END TRY
BEGIN CATCH
    IF @@TRANCOUNT > 0
        ROLLBACK TRANSACTION;

    DECLARE @ErrorMessage nvarchar(4000) = ERROR_MESSAGE();
    DECLARE @ErrorSeverity int = ERROR_SEVERITY();
    DECLARE @ErrorState int = ERROR_STATE();

    RAISERROR(@ErrorMessage, @ErrorSeverity, @ErrorState);
END CATCH;
```

**Important components:**

| Component              | Purpose                                   |
| ---------------------- | ----------------------------------------- |
| `TRY`                  | Contains the main operations.             |
| `CATCH`                | Handles errors raised in the `TRY` block. |
| `BEGIN TRANSACTION`    | Starts a transaction.                     |
| `COMMIT TRANSACTION`   | Saves transaction changes.                |
| `ROLLBACK TRANSACTION` | Reverses uncommitted changes.             |
| `@@TRANCOUNT`          | Checks the number of active transactions. |
| `ERROR_MESSAGE()`      | Returns the error message.                |
| `ERROR_SEVERITY()`     | Returns the error severity.               |
| `ERROR_STATE()`        | Returns the error state.                  |

Always check `@@TRANCOUNT` before rolling back to avoid errors when no active transaction exists.

### **5. Stored procedure best practices**

| Practice                   | Explanation                                                                                                              |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Use schema-qualified names | Use `dbo.Orders` instead of `Orders` to avoid ambiguity and schema resolution overhead.                                  |
| Validate parameters        | Reject invalid inputs early before executing database operations.                                                        |
| Avoid `SELECT *`           | Explicitly specify columns to prevent unexpected results when table structures change.                                   |
| Use meaningful names       | Include action verbs such as `Get`, `Insert`, `Update`, `Delete`, and `Calculate`.                                       |
| Avoid the `sp_` prefix     | SQL Server reserves this prefix for system procedures; using it can cause unnecessary searches in the `master` database. |

**Parameter validation example:**

```
IF @CustomerID IS NULL OR @CustomerID <= 0
BEGIN
    RAISERROR('CustomerID must be a positive integer.', 16, 1);
    RETURN -1;
END;
```

**Naming examples:**

```
-- Good
CREATE PROCEDURE dbo.GetCustomerOrders;
CREATE PROCEDURE dbo.UpdateCustomerAddress;
CREATE PROCEDURE dbo.DeleteExpiredOrders;

-- Avoid
CREATE PROCEDURE dbo.sp_GetCustomerOrders;
```

### **6. Key concepts to remember**

- `CREATE PROCEDURE` creates a stored procedure.
- `EXEC` or `EXECUTE` runs a stored procedure.
- `@Parameter` defines a procedure parameter.
- `OUTPUT` returns a parameter value to the caller.
- `RETURN` provides an integer return status.
- `SET NOCOUNT ON` suppresses row-count messages.
- `TRY...CATCH` handles runtime errors.
- `@@TRANCOUNT` checks active transactions.

**Key takeaway:** Stored procedures centralize database operations and business logic, support input/output parameters, provide error handling, and can improve repeated query execution through execution plan caching.