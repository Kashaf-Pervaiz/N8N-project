# Fankaar Khana — Business Automation System

*A connected system of AI agents that takes orders, answers customers, tracks deliveries, and watches the market — so nothing runs on memory alone.*

<p>
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat&logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/Pinecone-000000?style=flat&logo=pinecone&logoColor=white" />
  <img src="https://img.shields.io/badge/Google%20Sheets-34A853?style=flat&logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-2E8B57?style=flat" />
</p>

## The Problem

Every order for Fankaar Khana used to start as a message, a call, or a walk-in note. Handled manually, that meant lost orders, no delivery visibility, unresolved complaints, stale inventory, and no clear read on competitor pricing.

## The Solution

Fankaar Khana runs on an automation layer built in n8n. Six AI agents each own one job — taking orders, answering customers, chasing deliveries, handling complaints, managing inventory, and tracking competitors — feeding into a shared dashboard so nothing runs on memory.

## The Agents

1. **Order Intake Agent** — Captures new and returning customer orders via chat, logs them to Google Sheets, and sends confirmations.
2. **Chatbot & Voice Agent** — Answers customer questions live using RAG over shop data and policies (Groq + Pinecone).
3. **Admin Inventory Agent & Launch Bot** — Lets the owner add, update, or delete products via chat — no spreadsheets.
4. **Delivery Tracking Agent** — Checks pending deliveries on a schedule and notifies the owner and customer.
5. **Complaint Agent** — Logs every complaint, pulls context from a knowledge base, and sends a response.
6. **Competitor Data Analysis Agent** — Scrapes and logs competitor pricing on a schedule.
7. **Dashboard** — Pulls live data from all agents into a single view of the operation.

## Tech Stack

n8n · Groq (LLM Chat Model) · Pinecone (vector search/RAG) · HuggingFace Embeddings · Google Sheets · Gmail/WhatsApp notifications · Google Drive (file ingestion) · JavaScript · Python (app.py)

## Getting Started

1. Import the workflow into your n8n instance (Workflows → Import from File → select `fankaar khana.json`).
2. Set up credentials: Google Sheets, Gmail, Google Drive, Groq, Pinecone, HuggingFace, and your WhatsApp API endpoint.
3. Point each Sheet at your actual order/inventory/complaint/competitor sheets.
4. Activate the workflow — agents start listening for triggers automatically.

## Repository Structure

```
├── fankaar khana.json   # Main n8n workflow (all six agents + dashboard)
├── app.py                # Supporting Python automation script
└── README.md             # Project documentation
```

## Author

**Kashaf Pervaiz** — [kashafpervaiz15@gmail.com](mailto:kashafpervaiz15@gmail.com) 
·[LinkedIn](https://www.linkedin.com/in/kashaf-pervaiz-67a23038a)

⭐ If you find this project interesting, feel free to star the repo!
