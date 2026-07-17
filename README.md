<h1 align="center"> Fankaar Khana — Business Automation System</h1>

<p align="center">
  <i>A connected system of AI agents that takes orders, answers customers, tracks deliveries, and watches the market — so nothing runs on memory alone.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/n8n-EA4B71?style=flat&logo=n8n&logoColor=white" />
  <img src="https://img.shields.io/badge/Groq-F55036?style=flat&logo=groq&logoColor=white" />
  <img src="https://img.shields.io/badge/Pinecone-000000?style=flat&logo=pinecone&logoColor=white" />
  <img src="https://img.shields.io/badge/HuggingFace-FFD21E?style=flat&logo=huggingface&logoColor=black" />
  <img src="https://img.shields.io/badge/Google_Sheets-34A853?style=flat&logo=googlesheets&logoColor=white" />
  <img src="https://img.shields.io/badge/Gmail-EA4335?style=flat&logo=gmail&logoColor=white" />
  <img src="https://img.shields.io/badge/WhatsApp-25D366?style=flat&logo=whatsapp&logoColor=white" />
  <img src="https://img.shields.io/badge/Google_Drive-4285F4?style=flat&logo=googledrive&logoColor=white" />
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat&logo=javascript&logoColor=black" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=flat" />
</p>

---

##  The Problem

Every order for Fankaar Khana used to start as a message, a call, or a walk-in note. Handled manually, that meant:

- **Manual order handling** — orders scattered across calls, texts, and DMs with no single place to track them
- **Slow customer response** — customers waiting hours for answers to simple stock or delivery questions
- **No delivery visibility** — pending deliveries tracked from memory, with no follow-up system
- **Lost complaints** — issues raised in chat with no record, often left unresolved
- **No market insight** — competitor pricing and trends never checked systematically
- **Disconnected inventory** — stock updated by hand, with mistakes slipping through

## The Solution

Fankaar Khana runs on an automation layer built entirely in **n8n**. Instead of one monolithic bot trying to handle everything, the system is split into seven focused agents, each owning a single job — taking orders, answering customers, chasing deliveries, handling complaints, managing inventory, tracking competitors, and reporting back through a shared dashboard.

Every agent reads from and writes to the same **Google Sheets** backend, so there's one consistent record of truth across the whole operation instead of information scattered across chats and memory. Customer-facing agents respond over **WhatsApp and email**, so the experience still feels personal even though it's fully automated. The **Chatbot & Complaint agents** are backed by a retrieval-augmented pipeline (**Pinecone + HuggingFace embeddings**) so their answers stay grounded in actual shop policy and product data rather than guessing. And because the **Admin Inventory** and **Competitor Analysis** agents run on schedules and chat triggers, the owner can manage stock and stay aware of market pricing without ever opening a spreadsheet.

The result is a shop that runs itself in the background — while still feeling like a real person is on the other end of every message.

##  Key Areas of Impact

| Area | Before | After |
|---|---|---|
| **Order handling** | Orders scattered across calls, texts, and DMs | Every order automatically logged, confirmed, and tracked in one place |
| **Customer response time** | Hours-long waits for simple stock/delivery questions | Instant, always-on answers via chatbot and voice |
| **Delivery follow-up** | Depended entirely on memory | Scheduled checks automatically flag and notify pending deliveries |
| **Complaint resolution** | No record, often forgotten | Every complaint logged, answered with context, and tracked to closure |
| **Inventory management** | Manual spreadsheet updates, prone to mistakes | Owner updates stock directly through chat — errors reduced |
| **Market awareness** | No systematic competitor tracking | Competitor pricing pulled and compared automatically on a schedule |
| **Business visibility** | No single view of operations | A live dashboard pulling data from every agent in real time |
| **Customer trust** | Text-only, impersonal interactions | Real-time product images shared in chat to build confidence before purchase |
| **Marketing effort** | Manual caption-writing for every new product | Social media captions generated automatically when new products are added |


##  The Outcome

- Every order captured and logged automatically
-  Customer questions answered without delay
- Deliveries followed up before customers have to ask
-  Complaints tracked and resolved with a record
-  Pricing decisions backed by real market data
-  An order never gets missed again

##  Repository Structure

```
├── fankaar khana.json   # Main n8n workflow (all six agents + dashboard)
└── README.md             # Project documentation
```

##  Author

**Kashaf Pervaiz**
 [kashafpervaiz15@gmail.com](mailto:kashafpervaiz15@gmail.com)
 [LinkedIn](https://www.linkedin.com/in/kashaf-pervaiz-67a23038a)

---

⭐ If you find this project interesting, feel free to star the repo!
