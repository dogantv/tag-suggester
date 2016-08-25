## Tag Suggester

A simple restful api which takes a string as input (preferably a long one like an article), talks to elasticsearch and then returns suggested word groups as result. For now suggestions mostly relies on term frequency in documents.



## Requirements

This project depends on Elasticsearch with
[TurkishStemmer](https://github.com/skroutz/elasticsearch-analysis-turkishstemmer) plugin. Also requires python modules which is specified in `requirements.txt`


## Installation

 In order to install:

    git clone https://github.com/dogantv/tag_suggester.git


## Usage


First edit `src/config.py`

Then create your Elasticsearch index with settings in `settings.json`

Run `src/run.py`

POST to `http://your-tag-suggester-api-address/api/suggest`  with header `content-type application/json`

    {
         "text": "... some long text..."
    }

Response will be:

    {
        "suggestions": "... some suggestion..."
    }
