# Key Management Commands

Once your docker-compose.yml file is ready, use the following Docker CLI commands to manage your instance:

- Start the cluster: `docker compose up -d`
- Access the CQL shell: `docker exec -it cassandra-node cqlsh`
- Check cluster status: `docker exec -it cassandra-node nodetool status`
- Stop and remove containers: `docker compose down`

## Best Practices

- P**ersistence:** Always use named volumes (e.g., `/var/lib/cassandra`) to ensure data is kept even if the container is destroyed.
- **Resources:** Multi-node clusters are resource-intensive. It is recommended to have at least 4GB of RAM available for a 3-node cluster.
- **Healthchecks:** Use `nodetool status` in your healthcheck to ensure dependent nodes only start after the seed node is fully initialized.

### Additional Resources

- kayvansol/Cassandra - <https://github.com/kayvansol/Cassandra>
- Running Apache Cassandra® Single and Multi-Node Clusters on Docker with Docker Compose - <https://www.instaclustr.com/blog/running-apache-cassandra-single-and-multi-node-clusters-on-docker-with-docker-compose/>
- cassandra (Docker Official Image) - <https://hub.docker.com/_/cassandra>
