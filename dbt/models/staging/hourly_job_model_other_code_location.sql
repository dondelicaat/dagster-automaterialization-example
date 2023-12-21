{{
  config(
    dagster_freshness_policy={"maximum_lag_minutes": 2, "cron_schedule": "0 * * * *"},
  )
}}

select * from {{ source('lake', 'hourly_partitioned_other_code_location') }}
