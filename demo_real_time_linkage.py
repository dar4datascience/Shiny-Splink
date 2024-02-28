import json
from splink.datasets import splink_datasets
from splink.duckdb.linker import DuckDBLinker
import altair as alt
alt.renderers.enable('html')

with open("../../demo_settings/real_time_settings.json") as f:
    trained_settings = json.load(f)

df = splink_datasets.fake_1000

linker = DuckDBLinker(df, trained_settings)