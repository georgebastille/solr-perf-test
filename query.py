from concurrent.futures import ThreadPoolExecutor, as_completed
from random import shuffle

import click
import requests
from tqdm.auto import tqdm

THREADS = 2


def run_query(query):
    query = query.replace(" ", "+")
    url = f"http://localhost:8983/solr/hn_stories-8.8/select?df=title&facet.range.end=2014-05-29T08%3A25%3A40Z&facet.range.gap=%2B1DAY&facet.range.start=2006-10-09T00%3A00%3A00Z&facet.range=created_at&facet=true&rows=0&q={query}"
    return requests.get(url).json()["responseHeader"]["QTime"]


@click.command()
@click.argument("query_file", type=click.File("r"), required=True)
def run_queries(query_file):
    queries = query_file.read().splitlines()
    shuffle(queries)
    with ThreadPoolExecutor(max_workers=THREADS) as t:
        futures = []
        for query in queries:
            futures.append(t.submit(run_query, query=query))
        for future in tqdm(as_completed(futures), total=len(queries)):
            pass
            # print(future.result())


if __name__ == "__main__":
    run_queries()
