# elasticsearch_indexer
Gets data from Instagram API, inserts into Elasticsearch and displays via Django.

# Philosophy

## Crawler for getting data from Instagram API and indexing Elasticsearch

Due to Sandbox mode limitations (only access to media from max. 20 registered users), this demo only gets the recent media. It could also get the list of tags from Instagram and iterate through recent media from them.

## Application for displaying the indexed data by search

Simple search trough indexed data.
