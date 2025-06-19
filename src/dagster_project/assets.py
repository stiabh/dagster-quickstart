from dagster import asset


@asset
def my_asset():
    """An example asset that does nothing."""
    pass
