# AI Reasoning-Powered Assistant (LLM + JAX + Flask + PostgreSQL)

## Project Overview
This project is an AI-powered assistant that combines a reasoning module with a large language model (LLM) to generate intelligent responses. The system enhances user queries using a custom reasoning layer before sending them to an LLM, improving the quality and context of responses.

The application is built as a full-stack system with a Flask backend and PostgreSQL database for storing interactions.

---

## Objective
- Build an intelligent AI assistant using modern LLM APIs
- Enhance user queries using a reasoning module
- Store and manage conversation history using a database
- Demonstrate real-world AI system architecture

---

## Key Components

### Reasoning Layer
- Implemented using JAX
- Adds contextual understanding to user queries
- Classifies and enriches input before sending to LLM

### LLM Integration
- Uses Google Gemini API (or Claude API)
- Generates structured and meaningful responses

### Backend
- Flask-based web application
- Handles user input, processing, and response delivery

### Database
- PostgreSQL used to store:
  - User queries
  - Enhanced prompts
  - LLM responses
  - Timestamps

---

## System Architecture

User → Flask → JAX Reasoning → Prompt Enhancement → LLM API → Response → PostgreSQL

---

## Technologies Used
- Python
- Flask
- JAX
- Hugging Face (optional / future integration)
- Google Gemini API (or Claude API)
- PostgreSQL
- SQLAlchemy

---

## Features
- Intelligent query understanding
- Prompt enhancement using reasoning logic
- LLM-based response generation
- Persistent chat history storage
- Simple web interface

