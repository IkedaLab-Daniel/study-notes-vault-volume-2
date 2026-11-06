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