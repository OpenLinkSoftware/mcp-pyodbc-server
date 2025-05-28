import argparse
import logging
import os

from .server import (
    podbc_get_schemas,
    podbc_get_tables,
    podbc_describe_table,
    podbc_filter_table_names,
    podbc_execute_query,
    podbc_execute_query_md,
    mcp,
    podbc_query_database,
    podbc_spasql_query,
    podbc_virtuoso_support_ai,
    podbc_sparql_func,
    podbc_sparql_get_entity_types,
    podbc_sparql_get_entity_types_detailed,
    podbc_sparql_get_entity_types_samples,
    podbc_sparql_get_ontologies
)

# Optionally expose other important items at package level
__all__ = [
    "podbc_get_schemas",
    "podbc_get_tables",
    "podbc_describe_table",
    "podbc_filter_table_names",
    "podbc_execute_query",
    "podbc_execute_query_md",
    "podbc_query_database",
    "podbc_spasql_query",
    "podbc_virtuoso_support_ai",
    "podbc_sparql_func",
    "podbc_sparql_get_entity_types",
    "podbc_sparql_get_entity_types_detailed",
    "podbc_sparql_get_entity_types_samples",
    "podbc_sparql_get_ontologies"
]


def main():
    parser = argparse.ArgumentParser(description="MCP PyODBC Server")
    parser.add_argument("--transport", type=str, default="stdio", choices=["stdio", "sse"],
                        help="Transport mode: stdio or sse")
    
    args = parser.parse_args()
    logging.info(f"Starting server with transport={args.transport} ")
    mcp.run(transport=args.transport)

if __name__ == "__main__":
    main()
