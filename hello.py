import flask
import pyodbc
import kmeans
import config
import time

server = config.server
database = config.database
username = config.username
password = config.password

driver = '{ODBC Driver 18 for SQL Server}'

connection_string = (
    'DRIVER=' + driver +
    ';SERVER=' + server +
    ';PORT=1433' +
    ';DATABASE=' + database +
    ';UID=' + username +
    ';PWD=' + password +
    ';Encrypt=yes;' +
    ';TrustServerCertificate=no;'
)

# Azure SQL connection
print("Connecting to Azure SQL Database...")

dest = pyodbc.connect(
    connection_string,
    timeout=30
)

dcursor = dest.cursor()

print("Azure SQL Connected Successfully")


app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():

    return """
    <h1>Welcome to Intellipaat Demo</h1>
    <p>
    This site is a prototype API for moving ML prediction data.
    Use /migrate to start the job.
    </p>
    """


@app.route('/migrate', methods=['GET'])
def migrate():

    start_time = time.time()

    print("Migration started")

    # Run ML prediction
    data = kmeans.predict()

    print("Prediction completed")
    print("Records generated:", len(data))


    insert_query = """
    INSERT INTO dbo.Person5
    (
        CustomerID,
        Amount,
        Frequency,
        Recency,
        ClusterID
    )
    VALUES (?, ?, ?, ?, ?)
    """


    records = []

    print("Preparing SQL batch data...")


    for _, row in data.iterrows():

        records.append(
            (
                int(row.CustomerID),
                float(row.Amount),
                int(row.Frequency),
                int(row.Recency),
                int(row.Cluster_Id)
            )
        )


    print("Starting bulk insert...")


    try:

        # Enable batch insert optimization
        dcursor.fast_executemany = True

        dcursor.executemany(
            insert_query,
            records
        )

        dest.commit()


        execution_time = round(
            time.time() - start_time,
            2
        )


        print(
            f"Migration completed successfully in {execution_time} seconds"
        )


        return f"""
        <h1>Prediction Done</h1>
        <p>
        Records inserted: {len(records)}
        </p>
        <p>
        Execution time: {execution_time} seconds
        </p>
        """


    except Exception as e:

        dest.rollback()

        print("Database Error:", e)

        return f"""
        <h1>Migration Failed</h1>
        <p>{e}</p>
        """


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000
    )