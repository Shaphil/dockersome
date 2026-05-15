# SolrCloud Configuration (with ZooKeeper)

For more complex distributed setups, Solr requires ZooKeeper for coordination.

## Quick Commands

To manage your Solr container, use these standard Docker Compose commands:

- **Start:** `docker compose up -d`
- **Stop:** `docker compose down`
- **Access Admin UI:** Open your browser to <http://localhost:8983/solr>.
- **Manually create a core:** If you didn't use the precreate command, run: `docker exec -it solr_instance solr create_core -c new_core_name`
