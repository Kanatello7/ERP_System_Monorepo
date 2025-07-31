## ERP System Skeleton

This repository contains a microservices-based ERP skeleton built with:

* **FastAPI** for backend microservices (Products & Customers)
* **React + Vite** for frontend UI
* **PostgreSQL** databases per service
* **Alembic** for database migrations
* **Docker & Docker Compose** for containerized development
* **Shared Python library** (`shared_lib`) for common data structures (UniversalTable)

---

### Prerequisites

* **Docker** and **Docker Compose** installed on your machine
* A `.env` file in the project root with the following variables:

  ```ini
  DB_HOST=localhost
  DB_PORT=5432
  DB_USER=postgres
  DB_PASSWORD=postgres
  DB_NAME=erp

  CORS_ORIGINS="http://localhost:5173"
  ```

### Repository Structure

```
erp-skeleton/
├── docker-compose.yml       # Orchestrates all services
├── .env                     # Environment variables (do not commit)
├── README.md                # Project documentation
├── shared_lib/              # Shared Python library
└── services/
    ├── products_service/    # Products microservice
    │   ├── app/
    │   ├── alembic.ini
    │   └── migrations/
    └── customers_service/   # Customers microservice
        ├── app/
        ├── alembic.ini
        └── migrations/
└── frontend/                # React + Vite application
```

### Running the Full Stack

1. **Build and start all containers**

   From the project root, run:

   ```bash
   docker compose up --build -d
   ```

   This will:

   * Pull/build images for all services and databases
   * Run database migrations via Alembic
   * Start FastAPI services on ports **8001** (customers) and **8002** (products)
   * Serve the frontend on port **5173** via Nginx

2. **Verify running containers**

   ```bash
   docker compose ps
   ```

   You should see:

   ```
   Name                                Command               State           Ports
   --------------------------------------------------------------------------------------
   erp_system-customers-db-1           postgres              running         5432/tcp
   erp_system-customers-service-1      uvicorn app.main…    running         0.0.0.0:8001->8000/tcp
   erp_system-products-db-1            postgres              running         5432/tcp
   erp_system-products-service-1       uvicorn app.main…    running         0.0.0.0:8002->8000/tcp
   erp_system-frontend-1               nginx -g daemon off; running         0.0.0.0:5173->80/tcp
   ```

3. **Access the applications**

   * **Frontend UI**: [http://localhost:5173](http://localhost:5173)
   * **Customers API docs**: [http://localhost:8001/docs](http://localhost:8001/docs)
   * **Products API docs**: [http://localhost:8002/docs](http://localhost:8002/docs)

4. **Stopping the stack**

   ```bash
   docker compose down
   ```



