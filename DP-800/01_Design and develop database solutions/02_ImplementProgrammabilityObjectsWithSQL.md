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

# Create scalar functions

## **Scalar Functions in SQL Server**

A **scalar function** is a user-defined function that accepts zero or more parameters and returns exactly **one value** of a specified data type.

Unlike stored procedures, scalar functions can be embedded directly into SQL expressions, such as `SELECT`, `WHERE`, and other T-SQL statements.

### **1. Purpose and characteristics**

- **Code reusability:** Encapsulate calculations and transformations in one place.
- **Consistency:** Apply the same business rules across multiple queries.
- **Modularity:** Separate reusable logic from application code and SQL queries.
- **Single-value return:** Always returns one value with an explicitly defined data type.
- **Parameters:** Can accept zero or more input parameters.

### **2. Create a scalar function**

Use `CREATE FUNCTION` with parameters, a `RETURNS` clause, and a function body.

**Basic syntax:**

```
CREATE FUNCTION schema_name.function_name
(
    @parameter1 datatype,
    @parameter2 datatype
)
RETURNS return_datatype
AS
BEGIN
    -- Function logic
    RETURN @result;
END;
```

**Example: Calculate sales tax**

```
CREATE FUNCTION dbo.CalculateSalesTax
(
    @Amount DECIMAL(10,2),
    @TaxRate DECIMAL(5,4)
)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @TaxAmount DECIMAL(10,2);

    SET @TaxAmount = @Amount * @TaxRate;

    RETURN @TaxAmount;
END;
```

- `RETURNS` specifies the data type of the returned value.
- `RETURN` sends the calculated result back to the caller.
- `DECLARE` creates a local variable inside the function.

### **3. Use scalar functions in queries**

Scalar functions can be called directly inside SQL statements.

**Example: Calculate employee tenure**

```
CREATE FUNCTION dbo.GetEmployeeTenure
(
    @HireDate DATE
)
RETURNS INT
AS
BEGIN
    DECLARE @Tenure INT;

    SET @Tenure = DATEDIFF(YEAR, @HireDate, GETDATE());

    RETURN @Tenure;
END;
```

Use the function in a query:

```
SELECT
    EmployeeName,
    HireDate,
    dbo.GetEmployeeTenure(HireDate) AS YearsOfService
FROM Employees
WHERE dbo.GetEmployeeTenure(HireDate) >= 5;
```

**Important: Deterministic vs. non-deterministic functions**

| Type              | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| Deterministic     | Returns the same result when given the same input parameters. |
| Non-deterministic | May return different results even with the same inputs.       |

- `GETDATE()` makes `GetEmployeeTenure` non-deterministic because its result depends on the current date.
- Non-deterministic functions cannot be used in indexed views or indexes on computed columns.
- To support determinism, pass the current date as a parameter instead of calling `GETDATE()` inside the function.

### **4. Scalar function best practices**

| Practice                       | Explanation                                                                          |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| Prefer deterministic functions | Helps support query optimizations and indexing scenarios.                            |
| Avoid side effects             | Functions shouldn't modify database state or depend on external resources.           |
| Watch performance              | Scalar functions may execute once per row when used in queries against large tables. |
| Keep logic simple              | Straightforward calculations and transformations are easier to maintain.             |

**Performance consideration:**

Using scalar functions in `SELECT` or `WHERE` clauses on large tables can significantly affect performance because SQL Server may execute the function for every row.

For these scenarios, consider **inline table-valued functions** as an alternative.

**Example: Format a phone number**

```
CREATE FUNCTION dbo.FormatPhoneNumber
(
    @PhoneNumber VARCHAR(10)
)
RETURNS VARCHAR(14)
AS
BEGIN
    DECLARE @FormattedNumber VARCHAR(14);

    IF LEN(@PhoneNumber) = 10
        SET @FormattedNumber =
            '(' + SUBSTRING(@PhoneNumber, 1, 3) + ') ' +
            SUBSTRING(@PhoneNumber, 4, 3) + '-' +
            SUBSTRING(@PhoneNumber, 7, 4);
    ELSE
        SET @FormattedNumber = @PhoneNumber;

    RETURN @FormattedNumber;
END;
```

This function:

- Formats valid 10-digit phone numbers.
- Returns the original input if it doesn't match the expected length.
- Is deterministic and has no side effects.

### **5. Modify and remove scalar functions**

**Modify using&#x20;**`ALTER FUNCTION`

Changes the function definition without dropping and recreating it, preserving permissions and dependencies.

```
ALTER FUNCTION dbo.CalculateSalesTax
(
    @Amount DECIMAL(10,2),
    @TaxRate DECIMAL(5,4)
)
RETURNS DECIMAL(10,2)
AS
BEGIN
    DECLARE @TaxAmount DECIMAL(10,2);

    SET @TaxAmount = ROUND(@Amount * @TaxRate, 2);

    RETURN @TaxAmount;
END;
```

**Remove using&#x20;**`DROP FUNCTION`

```
DROP FUNCTION IF EXISTS dbo.CalculateSalesTax;
```

- `IF EXISTS` prevents errors if the function doesn't exist.
- Before dropping a function, check whether other database objects depend on it.
- Use `sys.sql_expression_dependencies` to inspect dependencies.

### **6. Key concepts to remember**

| Statement / Function              | Purpose                                            |
| --------------------------------- | -------------------------------------------------- |
| `CREATE FUNCTION`                 | Creates a user-defined function.                   |
| `RETURNS`                         | Defines the return data type.                      |
| `RETURN`                          | Returns the function's single value.               |
| `ALTER FUNCTION`                  | Modifies an existing function.                     |
| `DROP FUNCTION`                   | Removes a function.                                |
| `DATEDIFF()`                      | Calculates the difference between dates.           |
| `GETDATE()`                       | Returns the current database system date and time. |
| `ROUND()`                         | Rounds a numeric value.                            |
| `sys.sql_expression_dependencies` | Helps identify database object dependencies.       |

**Key takeaway:** Scalar functions encapsulate reusable calculations and transformations that return one value. They're useful for consistent business logic, but be mindful of non-deterministic behavior and per-row performance overhead on large datasets.

# Create table-valued functions

## **Table-Valued Functions in SQL Server**

A **table-valued function (TVF)** is a user-defined function that accepts parameters and returns a **table (result set)** instead of a single value.

Unlike stored procedures, TVFs can be used directly in `SELECT` statements, `JOIN` clauses, and other queries, making their results usable as data sources.

### **1. Types of table-valued functions**

SQL Server provides two types:

| Feature          | Inline TVF                   | Multi-statement TVF              |
| ---------------- | ---------------------------- | -------------------------------- |
| Query structure  | Single `SELECT` statement    | Multiple statements              |
| Table definition | Inferred from `SELECT`       | Explicitly declared              |
| Return syntax    | `RETURNS TABLE`              | `RETURNS @TableName TABLE (...)` |
| Logic            | Simple parameterized queries | Complex or multi-step processing |
| Performance      | Generally better             | Potential performance trade-off  |

**Inline TVF**

- Contains one `SELECT` statement.
- SQL Server automatically determines the returned table structure.
- Optimizer treats it similarly to a parameterized view.
- Generally preferred for simple queries with parameters.

**Multi-statement TVF**

- Uses a `BEGIN...END` block.
- Explicitly declares the returned table's columns and data types.
- Allows multiple operations, calculations, and conditional logic.
- Offers more flexibility but can have performance disadvantages.

### **2. Create an inline TVF**

Use `RETURNS TABLE` followed by a single `RETURN (SELECT ...)`.

```
CREATE FUNCTION dbo.GetCustomerOrders
(
    @CustomerID INT
)
RETURNS TABLE
AS
RETURN
(
    SELECT
        OrderID,
        OrderDate,
        TotalAmount,
        Status
    FROM Sales.Orders
    WHERE CustomerID = @CustomerID
);
```

Call it like a table:

```
SELECT OrderID, OrderDate, TotalAmount
FROM dbo.GetCustomerOrders(1001)
WHERE OrderDate >= '2024-01-01';
```

You can further filter, join, or aggregate the returned results.

### **3. Create a multi-statement TVF**

Use `RETURNS @TableName TABLE (...)` to explicitly define the returned table structure.

```
CREATE FUNCTION dbo.GetProductSalesSummary
(
    @StartDate DATE,
    @EndDate DATE
)
RETURNS @SalesSummary TABLE
(
    ProductID INT,
    ProductName NVARCHAR(100),
    TotalQuantity INT,
    TotalRevenue DECIMAL(18,2),
    AveragePrice DECIMAL(18,2)
)
AS
BEGIN
    INSERT INTO @SalesSummary
    SELECT
        p.ProductID,
        p.ProductName,
        SUM(od.Quantity),
        SUM(od.Quantity * od.UnitPrice),
        AVG(od.UnitPrice)
    FROM Production.Products p
    INNER JOIN Sales.OrderDetails od
        ON p.ProductID = od.ProductID
    INNER JOIN Sales.Orders o
        ON od.OrderID = o.OrderID
    WHERE o.OrderDate BETWEEN @StartDate AND @EndDate
    GROUP BY p.ProductID, p.ProductName;

    RETURN;
END;
```

**How it works:**

1. `RETURNS @SalesSummary TABLE` declares the table variable and its structure.
2. `INSERT INTO @SalesSummary` populates the returned table.
3. `RETURN` sends the completed result set back to the caller.

### **4. Use TVFs in queries**

TVFs can be combined with other tables using `APPLY` or `JOIN`.

**A. CROSS APPLY**

Executes the function using values from each row of the left-side table.

```
SELECT
    c.CustomerName,
    o.OrderID,
    o.TotalAmount
FROM Customers c
CROSS APPLY dbo.GetCustomerOrders(c.CustomerID) o
WHERE o.Status = 'Completed';
```

- Calls the function for each customer using their `CustomerID`.
- Returns matching rows from the function.
- Customers without matching orders are excluded.

**B. INNER JOIN**

Can also be used with inline TVFs:

```
SELECT
    c.CustomerName,
    o.OrderDate,
    o.TotalAmount
FROM Customers c
INNER JOIN dbo.GetCustomerOrders(c.CustomerID) o
    ON 1 = 1
WHERE YEAR(o.OrderDate) = 2024;
```

**C. CROSS APPLY with constant parameters**

```
SELECT
    c.CustomerName,
    s.ProductName,
    s.TotalRevenue
FROM Customers c
CROSS APPLY dbo.GetProductSalesSummary(
    '2024-01-01',
    '2024-12-31'
) s
WHERE s.TotalRevenue > 10000
ORDER BY s.TotalRevenue DESC;
```

Here, the function receives constant date parameters rather than values from each customer row.

### **5. Key concepts to remember**

| Keyword / Operator         | Purpose                                                        |
| -------------------------- | -------------------------------------------------------------- |
| `RETURNS TABLE`            | Defines an inline TVF.                                         |
| `RETURNS @TableName TABLE` | Declares the return table for a multi-statement TVF.           |
| `RETURN`                   | Returns the result set.                                        |
| `INSERT INTO @TableName`   | Populates the return table variable.                           |
| `CROSS APPLY`              | Evaluates the right-side expression using each left-side row.  |
| `INNER JOIN`               | Combines rows from tables or inline TVFs based on a condition. |

### **6. When to use each type**

- **Inline TVF:** Simple parameterized queries, filtering, and reusable data retrieval. Generally offers better optimization.
- **Multi-statement TVF:** Complex processing that requires multiple statements or intermediate result construction.
- **Stored procedure:** Operations that modify data or require more procedural control.

**Key takeaway:** Table-valued functions encapsulate reusable queries that return entire result sets. Inline TVFs are generally preferable for performance and simpler queries, while multi-statement TVFs provide flexibility for more complex processing.