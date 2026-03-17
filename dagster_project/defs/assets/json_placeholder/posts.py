import json

import dagster as dg

from dagster_project.defs.resources import JsonPlaceholderApi


@dg.asset
def json_placeholder__posts(
    context: dg.AssetExecutionContext, json_placeholder_api: JsonPlaceholderApi
) -> None:
    posts = json_placeholder_api.get_posts()

    context.log.info(json.dumps(posts[0], ensure_ascii=False, indent=4))
