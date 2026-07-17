# Fankaar Khana: n8n Multi-Agent Business Automation System

> **Transforming "Memory-Only" Operations into an Autonomous, Intelligent Creative Enterprise.**

Fankaar Khana is an artisanal creative business transitioning from chaotic, manual workflows to a streamlined, multi-agent backend engine built entirely on **n8n**. This repository houses the architecture, database schemas, and prompt templates for a 7-agent system designed to handle customer interaction, back-office logistics, and competitor intelligence.

---

## System Architecture Overview

The system is designed with a **decentralized hub-and-spoke model**. Agents do not loop endlessly; instead, they communicate asynchronously using a centralized PostgreSQL/Supabase database as a single source of truth.

```mermaid
graph TD
    A[WhatsApp / Web / Form] -->|Webhook| B(n8n Global Router)
    B --> C{Intent Classifier}
    C -->|Order Intake| D[Order Intake Agent]
    C -->|General FAQ| E[Front Desk Chat Agent]
    C -->|Logistics / Tracking| F[Delivery Tracking Agent]
    C -->|Support / Complaints| G[Complaint Agent]
    
    H[Owner Voice/Text] -->|Admin Chat| I[Admin & Inventory Agent]
    
    D & E & F & G & I <--> J[(Supabase Database)]
    
    K[Weekly Cron] --> L[Competitor Analysis Agent]
    M[Gateway Webhooks] --> N[Audit & Settlement Agent]
    L & N <--> J
