from dagster import (
    Definitions, define_asset_job,
    build_schedule_from_partitioned_job, HourlyPartitionsDefinition, asset
)


@asset(
    partitions_def=HourlyPartitionsDefinition(start_date="2023-12-20-14:00")
)
def hourly_partitioned_other_code_location():
    return [1, 2, 3]


hourly_partitioned_other_code_location_job \
    = define_asset_job("hourly_partitioned_other_code_location_job", selection=[hourly_partitioned_other_code_location])

hourly_partitioned_other_code_location_schedule = build_schedule_from_partitioned_job(
    hourly_partitioned_other_code_location_job,
)


defs = Definitions(
    assets=[
        hourly_partitioned_other_code_location,
    ],
    jobs=[
        hourly_partitioned_other_code_location_job,
    ],
    schedules=[
        hourly_partitioned_other_code_location_schedule,
    ],
)
