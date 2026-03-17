import dagster as dg

from dagster_project.defs.resources import JsonPlaceholderApi

# https://docs.dagster.io/guides/build/external-resources


@dg.definitions
def defs() -> dg.Definitions:
    resources = {
        "json_placeholder_api": JsonPlaceholderApi(
            api_key=dg.EnvVar("JSON_PLACEHOLDER_API_KEY"),
        ),
    }

    return dg.Definitions(resources=resources)
