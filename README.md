# Session 1: RL Agent

## 🤖 Q-Learning Robot Navigation

This project demonstrates **Q-Learning in a Grid World** using Python.  
The robot learns to navigate from a **start position (S)** to a **goal (G)** while avoiding obstacles (X), maximizing cumulative rewards, and balancing exploration vs. exploitation.  

The environment includes:
- ✅ **Rewards for reaching the goal**  
- 🚧 **Penalties for hitting obstacles**  
- 📉 **Distance-based shaping rewards** (guides the robot closer to the goal)  
- 📊 **Visualization** of Q-values, paths, and learning progress  

---

### 📸 Demo Preview
The robot learns to move around obstacles and reach the goal optimally.  
- **Grid world visualization** (Start, Goal, Obstacles, Path)  
- **Q-Table text view** with best actions per state  
- **Plots** for:
  - Grid world & robot position  
  - Q-values heatmap  
  - Learning curve (reward per episode)  
  - Epsilon decay (exploration rate)  

---

### 🛠 Features
- **Epsilon-greedy action selection** with decay  
- **Distance-based reward shaping**  
- **Obstacle handling** with penalties  
- **Matplotlib visualizations** for training and optimal policy  
- **Dynamic obstacle addition** after training  
- **Text + graphical grid world representation**  



[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/18oXJzKvAuvCKiCcex57-FFcRLOs0ZDnS)  




# Session 1: No-code Automation
## Automated TXT File Processing Pipeline with n8n  
*(Google Drive → Google Sheets → Gmail)*

### 📌 Overview
This project provides an **n8n Cloud workflow** that automates the processing of short text documents.  
The workflow:  
1. Watches a Google Drive folder for new `.txt` files  
2. Downloads the files and extracts key keywords/phrases  
3. Appends the results (filename, text, keywords) to a Google Sheet  
4. Sends a summary email via Gmail with extracted data  

A simple, reusable pipeline for lightweight document automation.

---

### ⚡ Features
- Automated ingestion of `.txt` files from Google Drive  
- Customizable keyword extraction logic (Regex in Code node)  
- Google Sheets integration for structured storage  
- Gmail summary reports for quick insights  
- Runs fully in **n8n Cloud** (no servers required)

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- n8n Cloud account → [app.n8n.cloud](https://app.n8n.cloud)  
- Google account with access to:
  - Google Drive (for `.txt` storage)  
  - Google Sheets (for output storage)  
  - Gmail (for sending email reports)  
- A target Google Sheet with columns: `Filename | Text | Keywords`

---

### 2. Import the Workflow
1. Clone/download this repo  
2. Open n8n Cloud → **Workflows** → **Import from File**  
3. Upload `workflow.json` from this repo

---

### 3. Configure Google Credentials
- In n8n, create new credentials for **Google Drive**, **Google Sheets**, and **Gmail**  
- Use the **“Sign in with Google”** option in each node for easy setup  
- Update the following in the workflow:
  - **Google Drive Trigger:** set your Drive folder ID  
  - **Google Sheets:** set your spreadsheet ID and range (default: `Sheet1!A:C`)  
  - **Gmail Node:** set your recipient email

---

### 4. Run the Workflow
1. Upload `.txt` files into the watched Drive folder  
2. Click **Execute Workflow** in n8n to test  
3. Once confirmed, toggle **Active** to run automatically

---

## 📊 Example Output

### Google Sheet
| Filename   | Text (excerpt)        | Keywords       |
|------------|-----------------------|----------------|
| notes1.txt | "...AI is booming..." | ai             |



# Session 2: Rapid Prototyping

Create a Python script that generates assignments and quizzes based on a provided document or topic. 
-The script should accept input text (document or topic) and output 2 assignment questions (e.g., essay prompts) and 3 multiple-choice quiz questions with options and answers. 
-Use simple logic to parse the input (e.g., split by sentences or keywords) and print the results. 
-Add Streamlit for the frontend.


# 📚 Educational Content Generator

An interactive **Streamlit-based tool** that generates **assignments** and **quiz questions** from text or PDF documents.  
This project is designed for educators, students, and researchers who need quick educational content creation.

---

## ✨ Features

- 📝 **Input Options**
  - Upload a **PDF file** (up to 50MB)
  - Paste or type text directly
  - Use the built-in **sample text** demo

- 📄 **Assignments**
  - Generates **2 essay-style questions**
  - Comparative and analytical prompts

- 🎯 **Quizzes**
  - Creates **3 multiple-choice questions**
  - Includes distractors and correct answers

- 🔍 **Concept Extraction**
  - Automatically identifies **key concepts** from text

- 📤 **Export**
  - Download generated results as a `.txt` file

- 🎨 **Beautiful UI**
  - Styled with custom CSS for clean display


