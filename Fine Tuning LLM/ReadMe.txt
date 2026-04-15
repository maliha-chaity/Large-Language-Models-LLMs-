# Fine-Tuned Transformer Model for Text Classification

## Project Overview
This project demonstrates how to fine-tune a pre-trained transformer model for a specific text classification task using the Hugging Face ecosystem. The model is trained to classify text inputs into predefined categories such as Normal or Suspicious behavior.

This is a practical example of transfer learning in Natural Language Processing (NLP), where a pre-trained model is adapted to a custom dataset.

---

## Objective
- Fine-tune a pre-trained transformer model on a custom dataset
- Improve classification performance on domain-specific text
- Demonstrate transfer learning using modern NLP techniques

---

## Model Used
- DistilBERT (pre-trained transformer model)
- Hugging Face Transformers Library

---

## Dataset
A small custom dataset was created containing labeled text samples:

Example:
Text: "Multiple failed login attempts detected"
Label: Suspicious

Text: "User logged in successfully"
Label: Normal


Labels:
- 0 → Normal
- 1 → Suspicious

---

## Technologies Used
- Python
- PyTorch
- Hugging Face Transformers
- Hugging Face Datasets

---

## Project Workflow

1. Load dataset
2. Tokenize text using tokenizer
3. Load pre-trained transformer model
4. Fine-tune model on labeled dataset
5. Evaluate model performance
6. Save trained model for inference

---
## Example Output:
Input: Multiple failed login attempts detected
Prediction: Suspicious (1)

Input: User logged in successfully
Prediction: Normal (0)
