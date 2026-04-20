import json
import os
from src.core.neo4j_client import Neo4jClient
from dotenv import load_dotenv

load_dotenv()

def run_ingestion():
    client = Neo4jClient(
        os.getenv("NEO4J_URI"), 
        "neo4j", 
        os.getenv("NEO4J_PASSWORD")
    )

    # Sample Data (Representing Objective 2 & 3)
    students = [
        {"id": "S1001", "name": "Alice Chen", "major": "Data Science", "gpa": 3.92, "seniority": "Senior"},
        {"id": "S1002", "name": "Bob Miller", "major": "Finance", "gpa": 3.45, "seniority": "Junior"},
        # ...Imagine 48 more entries
    ]

    ingest_query = """
    UNWIND $batch AS row
    MERGE (s:Student {studentId: row.id})
    SET s.name = row.name,
        s.major = row.major,
        s.gpa = toFloat(row.gpa),
        s.seniority = row.seniority
    RETURN count(s)
    """

    print(f"Ingesting {len(students)} student records...")
    client.execute_query(ingest_query, {"batch": students})
    print("Ingestion complete.")
    client.close()

if __name__ == "__main__":
    run_ingestion()
