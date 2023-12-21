{{
  config(
    dagster_freshness_policy={"maximum_lag_minutes": 2},
  )
}}

select * from {{ source('lake', 'hourly_partitioned_main_code_location') }}
