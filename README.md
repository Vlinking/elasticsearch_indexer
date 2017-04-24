# elasticsearch_indexer
Gets data from Instagram API, inserts into Elasticsearch and displays via Django.

# Philosophy

## Crawler for getting data from Instagram API and indexing Elasticsearch

Due to Sandbox mode limitations (only access to media from max. 20 registered users), this demo only gets the recent media. It could also get the list of tags from Instagram and iterate through recent media from them when in unrestricted mode.

## Application for displaying the indexed data by search

Simple search trough indexed data and displaying the photos.

# Usage

## Setup

A client_secrets.json file is needed, with data same as an app registered on Instagram. It should go into utils/

```
  "installed": {
    "client_id": "CLIENT_ID",
    "client_secret":"CLIENT_SECRET",
    "redirect_uris": ["http://www.whatever.com/"],
    "auth_uri": "https://api.instagram.com/oauth/authorize",
    "token_uri": "https://api.instagram.com/oauth/access_token"
  }
```  

You also need Elasticsearch installed (which requires Java) and running. Refer to Elasticsearch documentation for that.

## Crawler

Run utils/crawler.py script which will first authorize you on Instagram. Then, copy the code. On subsequent uses, the access token will be stored in a file inside the utils folder.

## Web Server

Run it in a standard Django way by:

python manage.py runserver
