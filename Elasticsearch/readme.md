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
