import glob

from setuptools import find_packages, setup

setup(
    name="dbt_automaterialization_test",
    packages=find_packages(),
    # package data paths are relative to the package key
    package_data={
        "dbt_automaterialization_test": ["../" + path for path in glob.glob("dbt/**", recursive=True)]
    },
    install_requires=[
        "dbt-core",
        "dagster==1.5.10",
        "dagster-webserver",
        "dagster-dbt",
        "dbt-duckdb",
        # packaging v22 has build compatibility issues with dbt as of 2022-12-07
        "packaging<22.0",
    ],
    extras_require={"dev": ["dagster-webserver"]},
)
