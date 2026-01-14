# Futurelab AI Assistant 🤖

The **Futurelab AI Assistant** is a customer-facing conversational interface designed to represent **Futurelab Studios** and communicate its offerings, expertise, and approach to AI enablement.

🔗 **Live Demo**  
👉 https://futurelab-ai-assistant.vercel.app/

The assistant provides structured, context-aware responses aligned with Futurelab’s real services, workshops, and AI capabilities. It is designed to support professional interactions with organizations and teams across geographies, keeping global usability and clarity at the core.

---

## About Futurelab Studios

Futurelab Studios is a technology and AI enablement studio that helps organizations and individuals adopt artificial intelligence in a **practical, responsible, and meaningful way**.

The studio operates at the intersection of **technology, education, and product development**, with a strong focus on real-world impact rather than hype-driven AI adoption. Futurelab works with a global audience across industries and regions, helping teams build confidence, capability, and clarity around AI.

---

## Key Capabilities

- Customer-facing AI assistant aligned with Futurelab’s brand and positioning  
- Context-aware responses grounded in verified company knowledge  
- Coverage of AI services, consulting, and adoption planning  
- AI enablement workshops for beginner, intermediate, and advanced teams  
- Custom AI tools including chatbots, voice agents, and retrieval-augmented systems  
- Global-ready design suitable for international audiences  
- Production-ready FastAPI backend with a modern React frontend  

---

## Technology Stack

### Backend
- Python  
- FastAPI  
- Uvicorn  
- Rule-based intent detection  
- Knowledge-driven response engine  

### Frontend
- React  
- Vite  
- Modern chat UI  
- REST API integration  

---

## Project Structure
Futurelab-AI-Assistant/
│
├── backend/
│ ├── knowledge/
│ │ ├── futurelab_profile.txt
│ │ ├── services.txt
│ │ └── workshops.txt
│ │
│ ├── chatbot_engine.py
│ ├── intent_mapper.py
│ └── main.py
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ │
│ ├── index.html
│ ├── package.json
│ └── vite.config.js
│
├── requirements.txt
└── README.md


---

## Typical Use Cases

The Futurelab AI Assistant is designed to support conversations such as:

- Explaining Futurelab Studios’ role as an AI enablement partner  
- Discussing AI consulting, adoption strategy, and workflow automation  
- Providing information on AI enablement workshops and training programs  
- Presenting Futurelab’s custom AI solutions, including chatbots and voice agents  
- Supporting inquiries from global teams evaluating AI initiatives  

These interactions closely mirror real conversations Futurelab engages in with clients, partners, and stakeholders.

---

## Running Locally
### Backend

```bash
cd backend
pip install -r ../requirements.txt
uvicorn main:app --reload

The backend runs at:
http://127.0.0.1:8000

Frontend
cd frontend
npm install
npm run dev

The frontend runs at:
http://localhost:5173

Deployment
Backend

Platform: Render
Runtime: Python

Start Command:
uvicorn main:app --host 0.0.0.0 --port 10000

Frontend
Platform: Vercel

Framework: React (Vite)
Build Command:
npm run build

Design Philosophy
This assistant is intentionally designed as a focused AI representation of Futurelab Studios, emphasizing clarity, trust, and real-world applicability.
Rather than acting as a generic chatbot, it mirrors how Futurelab communicates with organizations—balancing technical depth with accessibility and business relevance. The project demonstrates the ability to independently design, build, and deploy a customer-facing AI interface aligned with a real company’s positioning and values.
