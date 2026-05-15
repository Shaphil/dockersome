# Apache Kafka docker compose

Setting up Apache Kafka with Docker Compose is the most efficient way to run a local development environment. Modern setups typically use KRaft mode, which removes the need for a separate Zookeeper container, simplifying the architecture.

## Single-Node Kafka (KRaft Mode)

This configuration uses the official [Apache Kafka Docker image](https://hub.docker.com/r/apache/kafka) and includes Kafka UI for easy management through a browser.

## How to Run

- **Start the services:** Run `docker compose up -d` in your terminal.Access the UI: Open <http://localhost:8080> in your browser to view topics, messages, and broker status.
- **Test the connection:** You can produce and consume messages using local scripts or the Kafka CLI tools within the container

## Key Configuration Tips

- **Advertised Listeners:** Clients connecting from outside the Docker network (like your local machine) must use the address defined in `KAFKA_CFG_ADVERTISED_LISTENERS`.
- **Persistence:** For development, the above setup uses ephemeral storage. To keep your data after restarts, add a volume mapping for `/bitnami/kafka`.
- **Hardware:** Ensure Docker has at least **4GB of RAM** allocated for smooth Kafka performance.

## Resources

- How to run Kafka locally with Docker - <https://developer.confluent.io/confluent-tutorials/kafka-on-docker/>
- apache/kafka (Docker Hub) - <https://hub.docker.com/r/apache/kafka>
