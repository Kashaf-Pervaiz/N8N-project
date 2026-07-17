<h1 align="center">Fankaar Khana — Business Automation System</h1>
<p align="center">
  <i>A connected system of AI agents that takes orders, answers customers, tracks deliveries, and watches the market — so nothing runs on memory alone.</i>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Pinecone-000000?style=flat&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Sheets-34A853?style=flat&logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat" />
</p>
The Problem

Every order for Fankaar Khana used to start as a message, a call, or a walk-in note. Handled manually, that meant:

Manual order handling — orders scattered across calls, texts, and DMs with no single place to track them
Slow customer response — customers waiting hours for answers to simple stock or delivery questions
No delivery visibility — pending deliveries tracked from memory, with no follow-up system
Lost complaints — issues raised in chat with no record, often left unresolved
No market insight — competitor pricing and trends never checked systematically
Disconnected inventory — stock updated by hand, with mistakes slipping through


The Solution

Fankaar Khana runs on an automation layer built in n8n. Six agents each own one job — taking orders, answering customers, chasing deliveries, handling complaints, managing inventory, and tracking competitors — feeding into a shared dashboard so nothing runs on memory alone.

The Agents

1. Order Intake Agent

Webhook → Edit Fields → Get row(s) in sheet → If (new vs. returning customer)


New customer → logged via Groq Chat Model → row appended to sheet → confirmation email sent (Gmail) → order synced via HTTP Request
Returning customer → row appended/updated → confirmation email sent → order synced via HTTP Request


2. Chatbot & Voice Agent

Webhook → Question and Answer Chain → Respond to Webhook


Backed by a Groq Chat Model + Pinecone Vector Store (retrieval) with HuggingFace Embeddings, so customer questions are answered using live shop data and policy context.


3. Admin Inventory Agent & Launch Bot

When chat message received → AI Agent (Groq) → routes to: Add Product / Append row in Google Sheets / Update Product / Delete product


Lets the owner manage inventory directly through chat — no manual spreadsheet editing.


4. Delivery Tracking Agent

Schedule Trigger → Read Order sheet → Filter Pending Deliveries → If any pending


If pending → builds an owner delivery report (sent via HTTP Request) and a customer WhatsApp update (rate-limited via a Limit node)
If none pending → no operation


5. Complaint Agent

Webhook → Edit Fields → AI Agent (Groq) → Append row in sheet → HTTP Request → Email notification (Gmail)


Also includes a manual knowledge-base ingestion flow: Execute workflow → Download file from Google Drive → HuggingFace Embeddings → Pinecone Vector Store, so complaint responses stay grounded in reference documents.


6. Competitor Data Analysis Agent

Schedule Trigger → Get row(s) in sheet → HTTP Request → AI Agent (Groq)


Second branch: Edit Fields → Append row in sheet → Code (JavaScript) → Send message — pulls competitor pricing, compares it to current listings, and reports back to the owner.


7. Dashboard

Webhook → Get row(s) in sheet → Code (JavaScript) → Respond to Webhook


Pulls live data from the shared sheets into a single view of the operation.


Tech Stack

ComponentToolAutomation / orchestrationn8nLLMGroq (Chat Model, multiple agents)Vector search / RAGPinecone Vector StoreEmbeddingsHuggingFaceData storageGoogle SheetsNotificationsGmail, WhatsApp (HTTP Request)File ingestionGoogle DriveCustom logicJavaScript Code nodes, Python (app.py)

Getting Started


Import the workflow into your n8n instance:

Go to n8n → Workflows → Import from File
Select fankaar khana.json



Set up credentials for each connected service: Google Sheets, Gmail, Google Drive, Groq, Pinecone, HuggingFace, and your WhatsApp API endpoint.
Point each Sheet node at your actual order/inventory/complaint/competitor sheets.
Activate the workflow — the agents will begin listening for triggers and running automatically.


Repository Structure

├── fankaar khana.json   # Main n8n workflow (all six agents + dashboard)
├── app.py                # Supporting Python automation script
└── README.md             # Project documentation

 Author

Kashaf Pervaiz
 kashafpervaiz15@gmail.com
 LinkedIn


⭐ If you find this project interesting, feel free to star the repo!
