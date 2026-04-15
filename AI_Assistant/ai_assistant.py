# jax_reasoner
import jax.numpy as jnp

def reason_query(text):
    keywords = {
        "security": 1,
        "attack": 1,
        "login": 1,
        "data": 1
    }

    score = 0
    for k in keywords:
        if k in text.lower():
            score += 1

    score = jnp.array(score)

    if score > 1:
        return "High priority analytical question requiring deep reasoning."
    else:
        return "General informational query."

# llm_client
import google.generativeai as genai

genai.configure(api_key="API_KEY")

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_llm(prompt):
    response = model.generate_content(prompt)
    return response.text

#db
from sqlalchemy import create_engine

engine = create_engine("postgresql://user:password@localhost:5432/db_name")

# app
from flask import Flask, request, render_template
#from jax_reasoner import reason_query
#from llm_client import ask_llm
#from db import engine
import sqlalchemy

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form["query"]

        reasoning = reason_query(user_input)

        prompt = f"""
        Context: {reasoning}

        User Query:
        {user_input}

        Provide a structured and clear answer.
        """

        response = ask_llm(prompt)

        # Save to PostgreSQL
        with engine.connect() as conn:
            conn.execute(
                sqlalchemy.text("""
                    INSERT INTO chat_history (user_query, enhanced_prompt, llm_response)
                    VALUES (:u, :p, :r)
                """),
                {"u": user_input, "p": prompt, "r": response}
            )

        return render_template("index.html", result=response)

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(debug=True)