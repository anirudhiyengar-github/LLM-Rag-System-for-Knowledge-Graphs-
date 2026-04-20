import os
from dotenv import load_dotenv
from src.core.neo4j_client import Neo4jClient
from src.core.llm_service import LLMOrchestrator

load_dotenv()

def main():
    # Initialize components
    db = Neo4jClient(os.getenv("NEO4J_URI"), "neo4j", os.getenv("NEO4J_PASSWORD"))
    llm = LLMOrchestrator(os.getenv("OPENAI_API_KEY"))

    print("--- Student Intelligence Interface ---")
    user_query = input("Ask a question about the students: ")

    # 1. Translate
    cypher = llm.generate_cypher(user_query)
    print(f"\n[Generated Cypher]: {cypher}")

    # 2. Execute
    results = db.execute_query(cypher)
    print(f"[Raw Results]: {results}")

    # 3. Grounded Synthesis
    answer = llm.synthesize_answer(user_query, results)
    print(f"\n[Final Answer]: {answer}\n")

    db.close()

if __name__ == "__main__":
    main()
