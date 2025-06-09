from openai import OpenAI
from dotenv import load_dotenv
from pinecone.grpc import PineconeGRPC as Pinecone

import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
pc = Pinecone(api_key=os.getenv("pineconekey"))
index = pc.Index("ragwithrbac")

def get_response(query: str, role: str):

    #get embeddings of query
    response = client.embeddings.create(
    input=query,
    model="text-embedding-3-large"
    )

    embeddings = response.data[0].embedding



    context = index.query(
        namespace="demo",
        vector=embeddings, 
        top_k=1,
        filter={
            "role": {"$eq": role}
        },
        include_metadata=True,
        include_values=False
    )

    print(context)

    completion = client.chat.completions.create(
        model="gpt-4.1",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant. You are given context use that to answer the question. If you don't find the answer from the context, say 'I don't know'."
            },
            {
                "role": "user",
                "content": f"""Here is the context and user question:
                context: {context}
                user_question: {query}
                """
            }
        ]
    )

    return completion.choices[0].message.content


