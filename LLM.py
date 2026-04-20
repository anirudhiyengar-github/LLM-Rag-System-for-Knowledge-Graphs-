import os
from openai import OpenAI

class LLMOrchestrator:
    """
    Handles Text-to-Cypher translation and Grounding logic.
    """
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-3.5-turbo" # Or Llama-3 via Groq

    def generate_cypher(self, user_prompt):
        system_prompt = """
        You are a Neo4j Cypher Expert. Translate the user prompt into Cypher.
        SCHEMA: (:Student {studentId, name, major, gpa, seniority})
        RULES:
        - Use s.gpa for sorting/filtering.
        - Seniority: 'Freshman', 'Sophomore', 'Junior', 'Senior'.
        - Return ONLY the Cypher query.
        """
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0
        )
        return response.choices[0].message.content.strip()

    def synthesize_answer(self, user_prompt, graph_results):
        """
        Grounded generation: Synthesis based ONLY on graph results.
        """
        prompt = f"User asked: {user_prompt}\nGraph Data: {graph_results}\nFinal Answer:"
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Explain the graph results to the user. If results are empty, say no data found."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
