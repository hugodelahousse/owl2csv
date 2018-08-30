import sys
import click
import json
import csv
from rdflib import Graph, Namespace, URIRef, Literal


def observe_dataset(datasets, query, prefixes, lang):
    g = Graph()
    if prefixes:
        prefixes = json.load(prefixes)
        for name, url in prefixes.items():
            g.bind(name, Namespace(url.strip('<>')))
    for dataset in datasets:
        g.parse(dataset)

    kwargs = {}
    if lang:
        kwargs = {'initBindings':{'wantedLang': Literal('fr')}}
    return g, g.query(query, **kwargs)


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
@click.argument('datasets', type=click.File('r'), nargs=-1)
@click.argument('query', type=click.File('r'))
@click.option('--prefixes', '-p', default=None, type=click.File('r'))
@click.option('--output', '-o', default=sys.stdout, type=click.File('w'))
@click.option('--lang', '-l', default=None)
def command(datasets, query, prefixes, output, lang):
    graph, query_result = observe_dataset(datasets, query, prefixes, lang)
    create_csv(graph, query_result, output)


if __name__ == '__main__':
    command()
