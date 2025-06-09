# RBAC in RAG: Role-Based Access Control for Retrieval-Augmented Generation

This project demonstrates a scalable and secure architecture for applying **Role-Based Access Control (RBAC)** in a **Retrieval-Augmented Generation (RAG)** pipeline — using a **single vector database**.

## 🔍 Problem Statement

Traditional RAG pipelines lack access control. Anyone using the system can retrieve any document that's semantically relevant — which is unacceptable in an enterprise setting where departments handle confidential, role-specific data.

## ✅ Solution Overview

Instead of maintaining multiple vector databases per department or role, this approach uses **metadata tagging** during ingestion and **token-based filtering** during retrieval.

- Each document chunk is tagged with metadata such as `department` or `access_scope`
- Users authenticate via Identity Provider (SSO/OIDC)
- JWT token includes `roles` or `groups` claim
- During query time, vector search is filtered based on the user’s role
- Only authorized documents are retrieved

This allows a **single vector store** to serve the entire organization securely.

## 🧱 Key Components

- **Vector Store**: Any that supports metadata filtering (e.g., Qdrant, Pinecone, Weaviate)
- **Document Ingestion Pipeline**: Parses documents and embeds metadata for department/role
- **Identity Provider**: Auth0 / Azure AD / Okta with role claims in ID token
- **RAG App Layer**: Extracts roles from token and applies them as filters during search

## 🎯 Use Case Example

> Alice from Sales searches for "leave policy."  
> HR docs match the query semantically, but only Sales-tagged documents are returned — ensuring security.

## 🚀 Benefits

- Centralized vector DB
- Dynamic, role-based access at retrieval time
- Supports multi-role users and future departments
- Reduces operational overhead

## 🔐 Security Practices

- Relies on live tokens, not hardcoded ACLs
- Enforces access at the retrieval layer (not UI)
- Metadata cannot be bypassed by client requests

## 📚 Related Concepts

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases
- Role-Based Access Control (RBAC)
- Zero Trust Architecture

## How to
- Clone the repo
- cd into rag_with_rbac
- make .env file with two variables: pineconekey and OPENAI_API_KEY
- run: streamlit run streamlita_app.py

## Reach out to me
- <i>Author: <b>Sarmad Afzal</b></i>
- <i>Linkedin: https://www.linkedin.com/in/sarmadafzal/</i>
- <i>Github: https://github.com/sarmadafzalj</i>
- <i>Youtube: https://www.youtube.com/@sarmadafzalj</i>
- <i>Medium Blog: https://medium.com/@sarmadafzalj</i>
---


