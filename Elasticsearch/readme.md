# Elasticsearch, Logstash, Kibana - Stack

To run a specific file, for example, `compose.multi-node.not-working.yml`, run the following command,

```bash
docker compose -f compose.multi-node.not-working.yml up -d
# or
docker compose -f compose.multi-node.not-working.yml down
```

Otherwise, the following should suffice,

```bash
# to spin up
docker compose up -d

# and, to shout down
docker compose down
```

## Resources

- [Install Elasticsearch with Docker](https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html)
- [Getting started with the Elastic Stack and Docker Compose: Part 1](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose)
- [Getting started with the Elastic Stack and Docker Compose: Part 2](https://www.elastic.co/blog/getting-started-with-the-elastic-stack-and-docker-compose-part-2)
