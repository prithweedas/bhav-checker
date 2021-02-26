from redisearch import Client, Query

client = Client('bhav-index', host='redis', port=6379)


def search_equity_by_name(name: str) -> list[dict]:
    query = Query(name)
    query.limit_fields('name')
    result = client.search(query)
    results = []
    for doc in result.docs:
        data = doc.__dict__
        del data['payload']
        results.append(data)
    return results
