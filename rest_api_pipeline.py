import dlt
from dlt.sources.rest_api import rest_api_source

def lower_email(record):
    record['email'] = record['email'].lower()
    return record

source = rest_api_source({
    'client': {
        'base_url': 'https://jsonplaceholder.typicode.com'
    },
    'resources': [
        {
            "name": "users",
            "processing_steps": [
                {"filter": lambda x: x['id'] % 2 != 0},
                {"map": lower_email}
            ]
        },
        "posts"
    ]
})

pipeline = dlt.pipeline(
    pipeline_name="jsonplaceholder_api",
    destination="duckdb"
)

if __name__ == "__main__":
    pipeline.run(source)

    with pipeline.sql_client() as con:
        # Add primary keys manually
        con.execute("ALTER TABLE jsonplaceholder_api_dataset.users ADD CONSTRAINT users_pk PRIMARY KEY (id);")
        con.execute("ALTER TABLE jsonplaceholder_api_dataset.posts ADD CONSTRAINT posts_pk PRIMARY KEY (id);")
