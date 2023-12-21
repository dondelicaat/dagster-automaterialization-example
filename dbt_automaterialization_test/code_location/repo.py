from pathlib import Path

from dagster import (
    Definitions, asset,
    AssetExecutionContext, HourlyPartitionsDefinition, define_asset_job,
    build_schedule_from_partitioned_job
)
from dagster._utils import file_relative_path
from dagster_dbt import DbtCliClientResource, \
    DbtCliResource, load_assets_from_dbt_project

DBT_PROJECT_DIR = file_relative_path(__file__, "../../dbt")
DBT_PROFILES_DIR = file_relative_path(__file__, "../../dbt")

dbt_assets = load_assets_from_dbt_project(
    DBT_PROJECT_DIR,
    DBT_PROFILES_DIR,
)
# manifest_path = "/Users/4468379/Documents/fedex/dagster-test-automaterialization/dagster-dbt/dbt/target/manifest.json"
# @dbt_assets(manifest=Path(manifest_path))
# def yield_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
#     yield from dbt.cli(["build"], context=context).stream()



@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2023-12-20-14:00")
)
def hourly_partitioned_main_code_location():
    return [1, 2, 3]


hourly_partitioned_main_code_location_job \
    = define_asset_job("hourly_partitioned_main_code_location_job", selection=[hourly_partitioned_main_code_location])

hourly_partitioned_main_code_location_schedule = build_schedule_from_partitioned_job(
    hourly_partitioned_main_code_location_job,
)


resources = {
    "dbt": DbtCliClientResource(project_dir=DBT_PROJECT_DIR, profiles_dir=DBT_PROFILES_DIR),
}

defs = Definitions(
    assets=[
        # yield_dbt_assets,
        *dbt_assets,
        hourly_partitioned_main_code_location
    ],
    resources={
        "dbt": DbtCliResource(
            project_dir=DBT_PROJECT_DIR,
            target="dev",
        )
    },
    jobs=[
        hourly_partitioned_main_code_location_job,
    ],
    schedules=[
        hourly_partitioned_main_code_location_schedule,
    ],
)
