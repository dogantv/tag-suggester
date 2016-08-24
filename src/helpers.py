from elasticsearch import Elasticsearch


def suggest(es, text):

    """ Sends document to elasticsearch and returns top 20 result as response.
    """


    respond_index = es.index(index='tag_suggester',
                       doc_type='content',
                       body=text)

    _id = respond_index['_id']

    respond_vector = es.mtermvectors(index='tag_suggester',
                                      doc_type='content',
                                      ids=_id)

    term_vectors = respond_vector['docs'][0]['term_vectors']['text']

    terms = []
    for term, values in term_vectors['terms'].items():
        terms.append((term, values['term_freq']))


    sorted_by_freq = sorted(terms, key=lambda (t, f): f, reverse=True)

    filtered = []
    for term, freq in sorted_by_freq:
        if '_ ' in term or ' _' in term:
            continue
        filtered.append(term)

    return filtered[:20]
