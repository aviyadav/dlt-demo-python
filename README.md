# dlt-demo-python



uv venv
<br>source .venv/bin/activate

uv pip install dlt
<br>dlt --version
<br>dlt init rest_api duckdb

uv pip install -r requirements.txt
<br>uv pip install "dlt[duckdb]" streamlit
<br>uv pip freeze > requirements.txt

python rest_api_pipeline.py
<br>dlt pipeline jsonplaceholder_api show


TODO - https://github.com/hnawaz007/pythondataanalysis/blob/main/ETL%20Pipeline/dltproject/fxrate_pipeline.py
