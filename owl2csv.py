import sys
import click
import json
import csv
from rdflib import Graph, Namespace, URIRef


def observe_dataset(dataset, query, prefixes):
    g = Graph()
    if prefixes:
        prefixes = json.load(prefixes)
        for name, url in prefixes.items():
            g.bind(name, Namespace(url.strip('<>')))
    g.parse(dataset)
    return g, g.query(query.read())


def create_csv(graph, query_result, f):
    def normalize_field(field):
        if not field:
            return None
        elif isinstance(field, URIRef):
            return field.n3(graph.namespace_manager)
        return field
    writer = csv.writer(f)
    writer.writerow(query_result.vars)
    for row in query_result:
        writer.writerow(map(normalize_field, row))


@click.command()
@click.argument('dataset', type=click.File('r'))
@click.argument('query', type=click.File('r'))
@click.option('--prefixes', '-p', default=None, type=click.File('r'))
@click.option('--output', '-o', default=sys.stdout, type=click.File('w'))
def command(dataset, query, prefixes, output):
    graph, query_result = observe_dataset(dataset, query, prefixes)
    create_csv(graph, query_result, output)


if __name__ == '__main__':
    command()
