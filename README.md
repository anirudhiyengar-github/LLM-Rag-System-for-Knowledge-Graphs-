# LLM-Rag-System-for-Knowledge-Graphs-
Student-Graph-RAG: Knowledge-Grounded Retrieval System

This repository contains the complete implementation of a Knowledge-Grounded Student Retrieval System built with Neo4j Aura and LLM-driven orchestration.

Project Structure

database/: Contains Cypher scripts for schema initialization and indexing.

src/: Core Python logic.

core/: Driver abstractions and LLM service logic.

utils/: Logging and xAPI event formatting.

scripts/: Data ingestion and maintenance scripts.

data/: Sample synthetic dataset (50 students).

Setup Instructions

Neo4j Aura: Create a free instance at Neo4j Aura.

Environment Variables: Create a .env file with your NEO4J_URI, NEO4J_PASSWORD, and your LLM API key.

Install Dependencies: pip install -r requirements.txt

Initialize DB: Run the scripts in database/ via the Neo4j Browser.

Ingest Data: Run python scripts/ingest_data.py

Query: Run python src/main.py to start the natural language interface.
