# Basic Standalone Configuration

This setup starts a single Solr server and pre-creates a core named mycore so it's ready to use immediately.

## Key Components

- **Image:** Uses the official `solr:9` image.
- **Ports:** Maps the default [Solr port 8983](https://solr.apache.org/guide/solr/latest/deployment-guide/solr-in-docker.html) to your host machine.
- **Volumes:** Persists your [index data and configuration](https://solr.apache.org/guide/solr/latest/deployment-guide/solr-in-docker.html) in a named volume so it isn't lost when the container stops.
- **Command:** `solr-precreate [corename]` is a helper script that sets up a core before starting the server.
