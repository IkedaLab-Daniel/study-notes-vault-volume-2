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