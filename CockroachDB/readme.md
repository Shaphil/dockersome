# Setup

To set up a CockroachDB cluster using Docker Compose, you typically define multiple services in a docker-compose.yml file and then use the cockroach commands to join and initialize the nodes. For local development and testing, an insecure 3-node cluster is common.

## Prerequisites

- Docker and Docker Compose (v2 recommended) installed on your machine.
- Basic understanding of Docker networking and volumes.

## 3-Node Insecure Cluster Configuration

This configuration uses an `insecure` cluster for simplicity, suitable for local development environments only.

### 1. Create a `docker-compose.yml` file

Create a new directory for your project and a `docker-compose.yml` file within it. Copy the following configuration into the file. This configuration sets up three services (`roach1`, `roach2`, `roach3`) and an `haproxy` service for load balancing.

```yaml
version: '3.8'

services:
  roach1:
    image: cockroachdb/cockroach:latest
    ports:
      - '26257:26257'
      - '8080:8080'
    volumes:
      - roach1-data:/cockroach/data
    command: start --insecure --join=roach1,roach2,roach3 --advertise-addr=roach1
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8080/health?ready=1']
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  roach2:
    image: cockroachdb/cockroach:latest
    volumes:
      - roach2-data:/cockroach/data
    command: start --insecure --join=roach1,roach2,roach3 --advertise-addr=roach2
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8080/health?ready=1']
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  roach3:
    image: cockroachdb/cockroach:latest
    volumes:
      - roach3-data:/cockroach/data
    command: start --insecure --join=roach1,roach2,roach3 --advertise-addr=roach3
    healthcheck:
      test: ['CMD', 'curl', '-f', 'http://localhost:8080/health?ready=1']
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  haproxy:
    image: haproxy:2.4
    ports:
      - '26258:26258'
      - '8081:8080'
    volumes:
      - ./haproxy.cfg:/usr/local/etc/haproxy/haproxy.cfg:ro
    depends_on:
      - roach1
      - roach2
      - roach3

volumes:
  roach1-data:
  roach2-data:
  roach3-data:
```

### 2. Create a `haproxy.cfg` file

Create a new file named `haproxy.cfg` in the same directory as your `docker-compose.yml` file. This configures HAProxy to load balance connections across the three nodes.

```config
global
    maxconn 4096

defaults
    mode tcp
    timeout connect 10s
    timeout client 1m
    timeout server 1m

listen cockroachdb
    bind *:26258
    mode tcp
    option tcplog
    balance roundrobin
    server roach1 roach1:26257 check inter 1s
    server roach2 roach2:26257 check inter 1s
    server roach3 roach3:26257 check inter 1s

listen admin_ui
    bind *:8081
    mode tcp
    option tcplog
    balance roundrobin
    server roach1 roach1:8080 check inter 1s
    server roach2 roach2:8080 check inter 1s
    server roach3 roach3:8080 check inter 1s
```

### 3. Start the cluster

Run the following command in your terminal from the directory containing your `docker-compose.yml` and `haproxy.cfg` files:

```bash
docker-compose up -d
```

This command starts all containers in the background. The nodes will automatically discover each other via the Docker network using their service names (`roach1`, `roach2`, `roach3`) and the `--join` flag.

### 4. Initialize the cluster

Run the `init` command on one of the nodes (e.g., `roach1`) to bootstrap the cluster. This only needs to be done once.

```bash
docker-compose exec roach1 ./cockroach init --insecure
```

### 5. Verify the cluster status

You can check the node status to confirm all three nodes have joined the cluster:

```bash
docker-compose exec roach1 ./cockroach node status --insecure
```

### 6. Access the DB Console (Admin UI)

Open your web browser and navigate to `http://localhost:8081` to view the CockroachDB Admin UI. The load balancer (HAProxy) forwards requests to the admin interface of one of the running nodes.

## Next Steps

- Connect via SQL client: Use the built-in SQL client from any container to interact with the database:

```bash
docker-compose exec roach1 ./cockroach sql --insecure
```

- **Run a sample workload:** You can simulate a workload to see the cluster in action and monitor the metrics in the Admin UI.

- Stop and wipe data: To stop the cluster and remove all data volumes, use:

```bash
docker-compose down -v
```

- **Secure your cluster:** For production environments, running in insecure mode is strongly discouraged. Refer to the Cockroach Labs documentation on how to set up a secure cluster using TLS certificates
