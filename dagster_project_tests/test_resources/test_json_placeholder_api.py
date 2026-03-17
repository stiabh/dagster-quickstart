from collections.abc import Generator

import dagster as dg
import pytest

from dagster_project.defs.resources import JsonPlaceholderApi


@pytest.fixture
def json_placeholder_api() -> Generator[JsonPlaceholderApi]:
    resource = JsonPlaceholderApi(api_key="")
    context = dg.build_init_resource_context()
    resource.setup_for_execution(context)

    yield resource

    resource.teardown_after_execution(context)


@pytest.mark.integration
def test_posts__number_of_posts(json_placeholder_api: JsonPlaceholderApi) -> None:
    posts = json_placeholder_api.get_posts()
    assert len(posts) == 100
