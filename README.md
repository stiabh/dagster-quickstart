```
uvx create-dagster .
dg scaffold defs dagster.asset assets/hello_word.py
```

IMPORTANT: Every subdirectory in `dagster_project` and `dagster_project_tests` **must** contain a `__init__.py` file, otherwise imports will not work, and pytest will fail with cryptic error messages.