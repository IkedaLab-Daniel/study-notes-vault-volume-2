# Design and Implement database objects with SQL

# Introduction

## Database Object Design

- Database object design decisions are often difficult and costly to change after implementation compared to application code.
- Choosing the right objects upfront prevents complex migrations, performance issues, and production disruptions.
- Specialized database objects fundamentally affect how data is stored, queried, and validated.

## Key Topics

- Table Design: Choose appropriate data types, sizes, and structures. Understand rowstore vs. columnstore indexes based on workload.
- Specialized Table Types:
  - In-Memory Tables: High-throughput scenarios.
  - Temporal Tables: Automatic historical data tracking and auditing.
  - External Tables: Integration with Fabric lakehouses.
  - LEDGER Tables: Blockchain-style verification and compliance.
  - GRAPH Tables: Managing complex relationships.
- Constraints & Validation: Maintain data integrity using PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK, and DEFAULT constraints.
- Advanced Features:
  - JSON Columns: Support flexible data structures.
  - Optimized Indexes: Improve query performance.
  - SEQUENCE Objects: Generate IDs, including distributed ID generation patterns.
- Partitioning: Divide large tables and indexes into manageable segments for scalability and maintenance.

## Why Database Object Design Matters

| Area            | Benefit                                                      |
| --------------- | ------------------------------------------------------------ |
| Performance     | Faster query execution through proper table and index design |
| Data Integrity  | Ensures consistency and accuracy through constraints         |
| Maintenance     | Simplifies database administration                           |
| AI Capabilities | Enables integration with AI features                         |
| Scalability     | Handles large datasets efficiently through partitioning      |

## Supported Microsoft SQL Platforms

- Azure SQL Database
- Azure SQL Managed Instance
- SQL Database in Microsoft Fabric
- SQL Server

Key takeaway: Choose database objects based on your workload and long-term architectural requirements. Features such as temporal tracking, ledger verification, columnstore storage, and sequences are better planned during initial database design than retrofitted later.

# Understand your SQL server-based platform choices

## Microsoft SQL Platform Selection

Choose a SQL platform based on workload requirements, compatibility, infrastructure control, and management responsibilities.

### IaaS vs. PaaS

- PaaS (Platform-as-a-Service): Microsoft manages infrastructure, networking, OS patches, and database engine updates. Developers manage tables, indexes, constraints, and data.
- IaaS (Infrastructure-as-a-Service): You control the SQL Server instance, database engine configuration, and operating system.

Key difference: PaaS reduces infrastructure maintenance; IaaS provides greater customization and control.

## Azure SQL Database (PaaS)

- Fully managed database service with enterprise-grade performance and availability.
- Hyperscale:
  - Flexible storage that automatically expands.
  - No predefined maximum database size.
  - Supports additional read replicas for read-intensive workloads.
  - Pay for storage capacity used.
- Serverless Compute:
  - Automatically scales compute based on demand.
  - Automatically pauses when idle; storage charges continue.
  - Resumes when a connection request arrives.
  - Applications should implement connection retry logic because resuming introduces delays.
  - Long-running transactions can prevent autopause.
- Intelligent Query Processing: Analyzes workloads to improve query performance.
- Automatic Tuning: Recommends or automatically creates indexes and corrects query plan regressions.
- High Availability: Built-in HA with a 99.99% uptime SLA.

## Azure SQL Managed Instance (PaaS)

- Provides near 100% compatibility with the latest SQL Server Enterprise Edition.
- Automatic database engine patching, backups, and high availability.
- Native Virtual Network integration for network isolation.

Instance-level features:

- SQL Server Agent
- Service Broker
- Linked servers
- Cross-database queries (three-part naming)
- Database Mail

Additional capabilities:

- Managed Instance Link: Synchronizes on-premises SQL Server data to Azure using distributed availability groups. Supports hybrid deployments, read offloading, disaster recovery, and minimal-downtime migrations.
- In-Memory OLTP: Business Critical tier supports memory-optimized tables and natively compiled stored procedures for low-latency workloads.

## SQL Server on Azure Virtual Machines (IaaS)

- Provides maximum control over SQL Server and the underlying Windows/Linux operating system.
- Suitable for applications requiring:
  - Specific SQL Server versions.
  - OS-level access.
  - Custom database engine configurations.
  - Features unavailable in PaaS offerings.

SQL IaaS Agent Extension:

- Automated backups.
- Automatic patching during maintenance windows.
- Azure Key Vault integration.
- `tempdb` configuration through Azure Portal.

Additional capabilities:

- SQL Best Practices Assessment validates configurations.
- I/O performance analysis identifies storage bottlenecks.
- Always On Availability Groups and Failover Cluster Instances provide customizable HA and failover configurations.

## SQL Database in Microsoft Fabric

- Developer-friendly transactional database built on Azure SQL Database technology.
- Integrates OLTP (transactional processing) with Fabric's analytics ecosystem.

Automatic Mirroring:

- Replicates operational database changes into OneLake as Delta Parquet files.
- Synchronizes INSERT, UPDATE, and DELETE operations automatically.
- Requires no ETL pipelines, triggers, or additional configuration.

SQL Analytics Endpoint:

- Provides a read-only analytical view of mirrored data.
- Supports cross-database queries using three-part naming.
- Can query across Fabric warehouses, lakehouses, and other SQL databases.
- Analytical queries run against Delta Parquet copies instead of live operational tables, preventing reporting workloads from slowing down transactions.

Additional Features:

- Automatic index creation based on query patterns.
- Semantic search and Retrieval-Augmented Generation (RAG) support.
- `SqlPackage` for `.bacpac` and `.dacpac` portability.
- Git integration through Fabric Source Control.
- GraphQL APIs for modern application interfaces.

## Platform Comparison

| Platform                   | Deployment | Key Strength                                                 |
| -------------------------- | ---------- | ------------------------------------------------------------ |
| Azure SQL Database         | PaaS       | Fully managed, scalable cloud databases                      |
| Azure SQL Managed Instance | PaaS       | High SQL Server compatibility and instance-level features    |
| SQL Server on Azure VM     | IaaS       | Maximum infrastructure and configuration control             |
| SQL Database in Fabric     | PaaS       | Transactional workloads with automatic analytics integration |

## Quick Review: When to Choose Each Platform

- Azure SQL Database: Modern cloud applications requiring managed infrastructure, scalability, and automatic tuning.
- Azure SQL Managed Instance: Migrations from existing SQL Server environments requiring instance-level features and compatibility.
- SQL Server on Azure VM: Legacy or specialized applications requiring OS-level access and complete SQL Server control.
- SQL Database in Fabric: Transactional applications that need seamless integration with real-time analytics and OneLake.

Key takeaway: Understand each platform's management responsibilities and capabilities before designing database objects. The platform determines which features are available and how much infrastructure management is required.

# Build Effective Tables

## Table Design and Implementation

- Tables are fundamental relational database objects that organize data into rows and columns.
- They represent entities and their attributes, enforce relationships through foreign keys, and support queries and reporting.
- In analytical databases:
  - Fact Tables: Store measurable events and transactions.
  - Dimension Tables: Provide descriptive context for analysis.
- Table design directly affects storage efficiency, query performance, data integrity, and scalability.

## Choose Appropriate Data Types

Selecting the correct data type during initial schema design prevents storage waste, performance issues, data loss, and expensive production migrations.

| Category  | Data Types                            | Storage / Usage                                                                     |
| --------- | ------------------------------------- | ----------------------------------------------------------------------------------- |
| Numeric   | `INT`, `BIGINT`, `DECIMAL`, `FLOAT`   | INT: 4 bytes; BIGINT: 8 bytes; choose based on range and precision                  |
| String    | `VARCHAR`, `CHAR`, `NVARCHAR`         | VARCHAR: variable-length; CHAR: fixed-length; NVARCHAR: Unicode (2 bytes/character) |
| Date/Time | `DATE`, `DATETIME2`, `DATETIMEOFFSET` | DATE: 3 bytes; DATETIME2: 6–8 bytes; DATETIMEOFFSET: 10 bytes                       |
| Binary    | `VARBINARY`, `IMAGE`                  | Stores binary data such as images and documents                                     |
| Special   | `UNIQUEIDENTIFIER`, `XML`, `JSON`     | GUID: 16 bytes; XML: XML documents; JSON: native binary JSON (SQL Server 2025+)     |

### Important Data Type Considerations

- DECIMAL vs. FLOAT: Use `DECIMAL` for financial values because it provides exact precision. `FLOAT` can introduce rounding errors.
- INT vs. UNIQUEIDENTIFIER: Use `INT` when sufficient. GUIDs consume 16 bytes compared to INT's 4 bytes, increasing index size and potentially slowing JOIN operations.
- VARCHAR vs. NVARCHAR:
  - `VARCHAR`: Generally uses 1 byte per character for ASCII data.
  - `NVARCHAR`: Uses 2 bytes per character and supports Unicode.
  - Use `NVARCHAR` for international characters and `VARCHAR` for ASCII-only data when appropriate.
- DATETIME2 vs. DATETIME: Prefer `DATETIME2` for greater precision and modern date/time handling.

Rule: Choose the smallest appropriate data type that safely accommodates the expected values and precision requirements.

## Estimate Table Size Requirements

Table size affects more than storage costs. It also impacts:

- Backup and restore duration.
- Index rebuild times.
- Query performance and I/O requirements.
- Cloud database resource costs.

Example:

- 100 million transactions daily.
- An unnecessary additional 50 bytes per row.
- Storage waste: 5 GB/day or approximately 1.8 TB/year.

### Estimating Row Size

Example `Employee` table:

```
CREATE TABLE Employee (
    EmployeeID INT,              -- 4 bytes
    FirstName NVARCHAR(50),      -- ~40 bytes average
    LastName NVARCHAR(50),       -- ~40 bytes average
    HireDate DATE,               -- 3 bytes
    Salary DECIMAL(10,2)         -- 5 bytes
);
```

Estimated row size:

| Column             | Estimated Size |
| ------------------ | -------------- |
| EmployeeID         | 4 bytes        |
| FirstName          | 40 bytes       |
| LastName           | 40 bytes       |
| HireDate           | 3 bytes        |
| Salary             | 5 bytes        |
| Total              | 92 bytes       |
| Row overhead       | \~7 bytes      |
| Estimated row size | \~99 bytes     |

- 1 million rows ≈ 94 MB.
- Actual storage can vary depending on variable-length values, row overhead, and other storage structures.

## Design Effective Columns

Example of a properly designed `Product` table:

```
CREATE TABLE Product (
    ProductID INT PRIMARY KEY IDENTITY(1,1),
    ProductName NVARCHAR(100) NOT NULL,
    Category NVARCHAR(50) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    StockQuantity INT NOT NULL DEFAULT 0,
    LastRestocked DATETIME2 DEFAULT GETUTCDATE()
);
```

### Design Principles Applied

- Appropriate Data Types: INT for IDs, DECIMAL for financial values, and DATETIME2 for timestamps.
- Right-Sized Columns: Allocate column lengths based on expected data.
- NOT NULL: Prevents missing values in required columns.
- DEFAULT: Automatically supplies values when none are provided.
- IDENTITY(1,1): Automatically generates sequential IDs, starting at 1 and incrementing by 1.
- Efficient Primary Key: INT uses less storage than UNIQUEIDENTIFIER (4 vs. 16 bytes).

### VARCHAR vs. NVARCHAR Storage Example

For a 30-character string:

- `VARCHAR(100)` ≈ 30 bytes.
- `NVARCHAR(100)` ≈ 60 bytes.
- Across 10 million rows, using VARCHAR could save approximately 300 MB.

## Table Design Best Practices

| Practice               | Purpose                                                    |
| ---------------------- | ---------------------------------------------------------- |
| Appropriate Data Types | Reduce storage requirements and improve performance        |
| Estimate Table Size    | Plan storage, indexing, and resource requirements          |
| Meaningful Constraints | Enforce data quality at database level                     |
| Plan for Growth        | Accommodate increasing data volumes                        |
| Strategic Indexing     | Index columns frequently used in WHERE, JOIN, and ORDER BY |
| Columnstore Indexes    | Optimize large analytical workloads                        |
| Normalization          | Reduce unnecessary data duplication                        |
| Row/Page Compression   | Reduce storage requirements for large tables               |

### Rowstore vs. Columnstore

- Rowstore: Stores data by rows; generally suitable for transactional workloads (OLTP).
- Columnstore: Stores data by columns; generally suitable for large analytical workloads (OLAP).

Key takeaway: Good database performance starts with proper table design. Choosing appropriate data types, estimating storage requirements, defining constraints, and selecting suitable index types early prevents expensive migrations and performance bottlenecks later.

# Optimize with Indexes

- Indexes are data structures that accelerate data retrieval by creating optimized lookup paths to table rows.
- Without indexes, SQL Server may perform a Full Table Scan, examining every row to find matching records.
- Indexes work like a book's index: they help locate information without reading every page.

Trade-off:

- Faster `SELECT` queries and data retrieval.
- Additional storage requirements.
- Slower `INSERT`, `UPDATE`, and `DELETE` operations because indexes must also be maintained.

Poor indexing, missing indexes, and over-indexing are common causes of database performance problems.

## Rowstore Indexes

Rowstore indexes store data in row format, keeping all columns of a row together. They are ideal for OLTP workloads involving individual record retrieval and frequent modifications.

### Clustered Index

- Determines the physical storage order of table rows based on index key values.
- Only ONE clustered index per table because rows can only have one physical ordering.
- Best for:
  - Range queries.
  - Sequential or stable keys.
  - Frequently accessed primary data paths.
  - Natural ordering, such as identity columns or dates.

### Nonclustered Index

- Maintains a separate index structure from the actual table data.
- Contains index key values and pointers to corresponding data rows.
- Multiple nonclustered indexes can exist on a table.
- Best for:
  - Frequently searched columns.
  - JOIN and WHERE predicates.
  - Alternative sorting patterns.
  - Covering queries using included columns to avoid additional key lookups.

### Creating Rowstore Indexes

```
-- Clustered index
CREATE CLUSTERED INDEX IX_Product_ProductID
ON Product(ProductID);

-- Nonclustered index with included columns
CREATE NONCLUSTERED INDEX IX_Product_Category
ON Product(Category)
INCLUDE (ProductName, Price);
```

Key distinction:

| Feature      | Clustered                      | Nonclustered                          |
| ------------ | ------------------------------ | ------------------------------------- |
| Storage      | Determines row storage order   | Separate index structure              |
| Quantity     | One per table                  | Multiple per table                    |
| Main purpose | Primary data access path       | Alternative lookup paths              |
| Best for     | Range scans and ordered access | Specific lookups and covering queries |

## Columnstore Indexes

- Store data column-by-column instead of row-by-row.
- Optimized for analytical workloads (OLAP) that scan millions of rows and perform aggregations such as `SUM()`, `AVG()`, and `COUNT()`.
- Read only the columns required by a query, reducing unnecessary I/O.
- Provide high compression and efficient analytical processing.

### Columnstore Architecture

1\. Rowgroups

- A logical group containing up to 1,048,576 rows.
- Each rowgroup contains separately stored column segments.

2\. Column Segments

- Store individual columns independently within a rowgroup.
- Compressed separately for efficient storage and retrieval.

3\. Deltastore

- Temporary rowstore structure using a B+ tree index.
- Receives small batches of inserted rows before columnstore compression.

4\. Tuple-Mover

- Background process that compresses eligible delta rowgroups into columnstore format.
- Delta rowgroups containing at least 102,400 rows become eligible for compression.
- Bulk loads of 102,400 or more rows can bypass the deltastore and load directly into columnstore.

### When to Use Columnstore

| Scenario                   | Recommendation | Reason                                    |
| -------------------------- | -------------- | ----------------------------------------- |
| Data warehouse fact tables | Use            | Efficient analytics on millions of rows   |
| Reporting databases        | Use            | Optimized for aggregate queries           |
| Historical data            | Use            | High compression for rarely modified data |

# Use specialized table types

## Specialized Table Types in SQL Server

SQL Server provides specialized table types for workloads that standard disk-based tables cannot efficiently handle.

| Table Type | Primary Purpose                                       |
| ---------- | ----------------------------------------------------- |
| In-Memory  | High-performance, low-latency data access             |
| Temporal   | Automatic historical data tracking                    |
| External   | Query data stored outside the database                |
| LEDGER     | Cryptographic verification and tamper-evident records |
| GRAPH      | Model complex relationships between entities          |

## In-Memory Optimized Tables

- Store table data entirely in RAM instead of traditional disk-based storage.
- Use lock-free, optimistic concurrency to reduce contention and improve performance.
- Designed for high-throughput workloads requiring millisecond or microsecond response times.

### Common Use Cases

- Session State: Managing millions of concurrent web application sessions.
- Real-Time Analytics: Financial trading systems requiring extremely low latency.
- High-Frequency OLTP: Order processing systems handling 10,000+ transactions/second.
- Caching Layer: Frequently accessed reference data, such as product catalogs and configurations.
- Staging Tables: ETL processes involving intensive INSERT and UPDATE operations.

### Trade-offs

- Requires sufficient RAM because table data resides in memory.
- Data size is limited by available RAM.
- Doesn't support large object types such as `VARCHAR(MAX)`, `NVARCHAR(MAX)`, and `VARBINARY(MAX)`.
- Transaction logs are still written to disk to ensure durability.
- Committed transactions can be recovered into memory after a server restart.

### Creating an In-Memory Table

```
CREATE TABLE dbo.OrderCache (
    OrderID INT PRIMARY KEY NONCLUSTERED,
    CustomerID INT,
    OrderDate DATETIME2,
    Amount DECIMAL(10,2),
    INDEX IX_CustomerID NONCLUSTERED (CustomerID)
) WITH (
    MEMORY_OPTIMIZED = ON,
    DURABILITY = SCHEMA_AND_DATA
);
```

- `MEMORY_OPTIMIZED = ON`: Enables in-memory optimization.
- `DURABILITY = SCHEMA_AND_DATA`: Preserves both table schema and data across restarts.

## Temporal Tables

- Automatically maintain historical versions of records.
- When a row is updated or deleted, SQL Server stores its previous version in an associated history table.
- Uses timestamps to track when each version was valid.
- No custom triggers or application-level versioning logic required.

### Common Use Cases

- Compliance & Auditing: Track changes to financial records.
- Troubleshooting: Investigate historical account balances.
- Trend Analysis: Analyze product price changes over time.
- Data Recovery: Retrieve previous values after accidental updates.
- Slowly Changing Dimensions (SCD Type 2): Maintain historical dimension records in data warehouses.

### Benefits and Trade-offs

- No application code changes required.
- Automatic history tracking.
- Supports point-in-time queries.
- Automatically manages historical versions.
- Storage requirements can roughly double because historical records are retained.

### Creating a Temporal Table

Temporal tables require:

- Two `DATETIME2` columns representing the start and end of each row's validity.
- `GENERATED ALWAYS AS ROW START` and `GENERATED ALWAYS AS ROW END`.
- `PERIOD FOR SYSTEM_TIME` to define the validity period.
- `SYSTEM_VERSIONING = ON` to enable automatic history tracking.

```
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    EmployeeName NVARCHAR(100),
    Department NVARCHAR(50),

    SysStartTime DATETIME2
        GENERATED ALWAYS AS ROW START,

    SysEndTime DATETIME2
        GENERATED ALWAYS AS ROW END,

    PERIOD FOR SYSTEM_TIME (
        SysStartTime,
        SysEndTime
    )
) WITH (SYSTEM_VERSIONING = ON);
```

### Query Historical Data

```
SELECT *
FROM Employee
FOR SYSTEM_TIME AS OF '2026-01-01'
WHERE EmployeeID = 1;
```

`FOR SYSTEM_TIME AS OF` retrieves the record as it existed at a specific point in time.

SQL Server automatically creates and maintains the associated history table.

## External Tables

- Allow querying data stored outside the database without importing or physically moving it.
- Implement data virtualization, reducing ETL complexity and duplicate storage.
- Useful when data is distributed across data lakes, blob storage, and external systems.

### Common Use Cases

- Data Lake Integration: Query Parquet and CSV files in Azure Data Lake Storage.
- Data Exploration: Analyze raw data before importing it.
- Cost Optimization: Avoid duplicating externally stored data.
- Federated Queries: Join database tables with external files.
- Archival Storage: Access historical data stored in cheaper blob storage.

### Benefits and Trade-offs

- No data movement or storage duplication.
- Supports querying across distributed sources.
- Often slower than native tables due to network latency and file parsing.
- Generally read-only; UPDATE and DELETE are unavailable in most scenarios.
- Limited indexing and query optimization.

### Creating an External Table

```
CREATE EXTERNAL TABLE dbo.ExternalSalesData (
    OrderID INT,
    CustomerID INT,
    OrderAmount DECIMAL(10,2),
    OrderDate DATE
) WITH (
    LOCATION = '/raw/sales/',
    DATA_SOURCE = DataLakeSource,
    FILE_FORMAT = ParquetFormat
);
```

- `LOCATION`: External file or directory location.
- `DATA_SOURCE`: Defines the external data source.
- `FILE_FORMAT`: Specifies the external file format.

## LEDGER Tables

- Use cryptographic verification inspired by blockchain technology to create tamper-evident records.
- Provide independently verifiable proof of data integrity.
- Designed for regulatory compliance, auditing, and applications requiring trustworthy records.

### Common Use Cases

- Financial transactions and banking.
- Supply chain tracking and product authenticity.
- Legal contracts and agreements.
- Healthcare records and patient consent.
- Government records, voting, and land registries.

### Types of Ledger Tables

1\. Updatable Ledger Tables

- Allow `INSERT`, `UPDATE`, and `DELETE`.
- Cryptographically track every modification.
- Automatically preserve previous versions in a history table.
- Similar to temporal tables but with additional tamper-evident verification.

2\. Append-Only Ledger Tables

- Only allow `INSERT` operations.
- Create immutable records.
- Suitable for records that must never be modified or deleted.

Combining Ledger and Temporal Tables:

A table can use both technologies to provide cryptographic verification and point-in-time historical queries.

### Creating Ledger Tables

```
-- Updatable ledger table
CREATE TABLE dbo.FinancialTransaction (
    TransactionID INT PRIMARY KEY IDENTITY,
    AccountNumber NVARCHAR(20),
    Amount DECIMAL(15,2),
    TransactionType NVARCHAR(20)
) WITH (LEDGER = ON);

-- Append-only ledger table
CREATE TABLE dbo.AuditLog (
    LogID INT PRIMARY KEY IDENTITY,
    EventDescription NVARCHAR(500),
    EventTimestamp DATETIME2
) WITH (
    LEDGER = ON,
    APPEND_ONLY = ON
);
```

### How Ledger Verification Works

- SQL Server automatically adds hidden columns and supporting database objects.
- Every modification generates a cryptographic hash linked to previous operations.
- Creates a tamper-evident cryptographic chain.

Verification tools:

- `sys.database_ledger_transactions`: System view for inspecting ledger transactions.
- `sp_verify_database_ledger`: Stored procedure for verifying the integrity of the cryptographic chain.

## GRAPH Tables

- Designed for highly connected data involving complex relationships.
- Uses nodes to represent entities and edges to represent relationships.
- Simplifies multi-hop relationship queries that would otherwise require numerous JOIN operations.

### Common Use Cases

- Social networks (friends of friends).
- Product recommendation relationships.
- Organizational relationships.
- Complex interconnected data.

### Benefits and Trade-offs

- Intuitive modeling of connected data.
- Simplifies relationship traversal queries.
- Supports flexible relationship structures.
- Can improve multi-hop query performance.
- Requires learning specialized `MATCH` syntax.
- Best suited for read-heavy relationship queries.

Avoid GRAPH tables when:

- Simple parent-child relationships can be handled with foreign keys.
- Data is primarily transactional without complex relationships.
- Schemas are highly structured and stable.

### Graph Table Structure

1\. Node Tables

- Store entities.
- Automatically include hidden `$node_id` columns that uniquely identify nodes.

2\. Edge Tables

- Store relationships between nodes.
- Automatically include hidden columns:
  - `$edge_id`: Identifies the edge.
  - `$from_id`: Identifies the source node.
  - `$to_id`: Identifies the destination node.

### Creating Graph Tables

```
-- Create node and edge tables
CREATE TABLE Person AS NODE;
CREATE TABLE Manages AS EDGE;
CREATE TABLE Knows AS EDGE;
```

### Inserting and Querying Relationships

```
-- Insert nodes
INSERT INTO Person
VALUES (1, 'Alice'), (2, 'Bob'), (3, 'Charlie');

-- Insert relationships
INSERT INTO Manages
VALUES (1, 2), (2, 3);

-- Traverse relationships
SELECT Person1.name, Person2.name
FROM Person AS Person1, Manages, Person AS Person2
WHERE MATCH (Person1-(Manages)->Person2)
AND Person1.id = 1;
```

SQL Server automatically manages the hidden system columns required for graph traversal.

## Specialized Table Types: Quick Comparison

| Table Type | Main Advantage                   | Main Trade-off                            |
| ---------- | -------------------------------- | ----------------------------------------- |
| In-Memory  | Extremely fast data access       | Requires RAM                              |
| Temporal   | Automatic historical tracking    | Increased storage                         |
| External   | Query data without importing     | Network latency and limited optimization  |
| LEDGER     | Cryptographic tamper detection   | Restricts modifications depending on type |
| GRAPH      | Simplifies complex relationships | Requires specialized syntax               |

Key takeaway: Select specialized table types based on workload requirements rather than using standard tables for everything. In-memory tables optimize speed, temporal tables preserve history, external tables enable data virtualization, ledger tables provide tamper evidence, and graph tables simplify complex relationships. These architectural decisions are best made during initial database design because changing them after deployment can be difficult.