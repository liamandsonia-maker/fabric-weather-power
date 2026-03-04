# Project Architecture

This project uses a Bronze → Silver → Gold data model.

- **Bronze**: Raw ingested data from weather and power usage sources.
- **Silver**: Cleaned and typed tables.
- **Gold**: Analytics-ready tables for reporting.

Fabric is treated as disposable; GitHub is the source of truth.
