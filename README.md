# 🍹 Cocktail Advisor Chat 🗨️  
A **FastAPI-based chat application** that integrates a **Hugging Face LLM** and **FAISS vector database** to provide **cocktail recommendations** and **ingredient-based searches** using **Retrieval-Augmented Generation (RAG)**.

---

## **🚀 Features**
- ✅ **Chatbot Interface** – Simple web-based UI for asking cocktail-related questions.  
- ✅ **LLM-Powered Answers** – Uses **Hugging Face’s Falcon-7B** for intelligent responses.  
- ✅ **Vector Database (FAISS)** – Finds **similar cocktails** based on ingredients.  
- ✅ **Memory Storage** – Stores **user’s favorite ingredients** for personalized recommendations.  

---

## **🛠️ Tech Stack**
- **Backend**: FastAPI  
- **Frontend**: HTML, JavaScript  
- **LLM**: Hugging Face (`Falcon-7B`, `sentence-transformers/all-MiniLM-L6-v2`)  
- **Vector Database**: FAISS  
- **Dockerized**: Runs with `docker-compose`  

---

## **📦 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/cocktail-advisor-chat.git
cd cocktail-advisor-chat





1️⃣ Build and Run the Container
docker-compose up --build



2️⃣ Test API
curl -X 'POST' 'http://localhost:8000/api/chat' \
     -H 'Content-Type: application/json' \
     -d '{"question": "What are the 5 cocktails containing lemon?"}'