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