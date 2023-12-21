## How to reproduce

```bash
pip install .
```

and then run using:

```bash
dagster dev -m dbt_automaterialization_test.other_code_location.repo -m dbt_automaterialization_test.code_location.repo
```

Then turn on automaterialization and materialize all source partitions in both code locations and then trigger the downstream assets. 

After `max_lag_minutes` the assets depending on the upstream code_location will say they are overdue because of the upstream source not being up to date. 

However, the ones sourcing from the different code locations will only be overdue after `max_lag_minutes` since then they themselves seem overdue? Not really sure what goes wrong but it seems to not respect the upstream dependencies.
