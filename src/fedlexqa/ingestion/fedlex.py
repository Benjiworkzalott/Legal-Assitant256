"""Access to the Fedlex SPARQL endpoint (metadata and links to law documents).

Start with the interactive tutorial: https://swiss.github.io/fedlex-jolux/introduction.html
Note: not yet tested against the live endpoint. Do that on day 2.
"""

import httpx

SPARQL_ENDPOINT = "https://fedlex.data.admin.ch/sparqlendpoint"


def run_sparql(query: str, timeout: float = 60.0) -> list[dict[str, str]]:
    """Run a SPARQL SELECT query and return rows as {variable: value} dicts."""
    response = httpx.post(
        SPARQL_ENDPOINT,
        data={"query": query},
        headers={"Accept": "application/sparql-results+json"},
        timeout=timeout,
    )
    response.raise_for_status()
    bindings = response.json()["results"]["bindings"]
    return [{key: cell["value"] for key, cell in row.items()} for row in bindings]
