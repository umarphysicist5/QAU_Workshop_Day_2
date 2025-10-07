import streamlit as st
import random
import re

def extract_key_concepts(text):
    """Extract key concepts from text by finding important words."""
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 
                  'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
                  'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
                  'could', 'should', 'may', 'might', 'can', 'this', 'that', 'these',
                  'those', 'it', 'its', 'they', 'them', 'their'}
    
    # Clean and split text
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    # Filter out stop words and get unique important words
    concepts = [w.capitalize() for w in words if w not in stop_words]
    return list(set(concepts))[:10]  # Return up to 10 unique concepts

def generate_assignments(text, topic):
    """Generate 2 essay assignment questions."""
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 20]
    concepts = extract_key_concepts(text)
    
    assignments = []
    
    # Assignment 1: Analysis/Explanation
    if concepts:
        assignment1 = f"Write an essay explaining the relationship between {concepts[0]} and {concepts[1] if len(concepts) > 1 else 'the main concepts'} discussed in the material. Provide specific examples and analyze their significance."
    else:
        assignment1 = f"Write an essay analyzing the key concepts presented in the material about {topic}. Support your analysis with specific examples."
    assignments.append(assignment1)
    
    # Assignment 2: Critical Thinking/Application
    if len(concepts) >= 2:
        assignment2 = f"Critically evaluate how {concepts[random.randint(0, min(2, len(concepts)-1))]} applies to real-world scenarios. Discuss potential benefits and limitations with supporting evidence."
    else:
        assignment2 = f"Discuss the practical applications and implications of the concepts covered. How might these ideas be applied in different contexts?"
    assignments.append(assignment2)
    
    return assignments

def generate_quiz_questions(text, topic):
    """Generate 3 multiple-choice quiz questions."""
    sentences = [s.strip() for s in text.split('.') if len(s.strip()) > 20]
    concepts = extract_key_concepts(text)
    
    questions = []
    
    # Question 1: Definition/Concept
    if concepts and len(concepts) >= 3:
        correct = concepts[0]
        options = [correct] + random.sample(concepts[1:], min(3, len(concepts)-1))
        while len(options) < 4:
            options.append(f"Alternative {len(options)}")
        random.shuffle(options)
        
        question1 = {
            'question': f"Which of the following is a key concept discussed in the material about {topic}?",
            'options': options,
            'answer': correct
        }
        questions.append(question1)
    
    # Question 2: Comprehension
    if sentences:
        selected_sentence = random.choice(sentences[:min(3, len(sentences))])
        question2 = {
            'question': f"According to the material, which statement best describes the main idea?",
            'options': [
                f"{selected_sentence[:60]}..." if len(selected_sentence) > 60 else selected_sentence,
                "This concept is not discussed in the material",
                "The opposite of what is stated in the text",
                "An unrelated concept"
            ],
            'answer': f"{selected_sentence[:60]}..." if len(selected_sentence) > 60 else selected_sentence
        }
        questions.append(question2)
    
    # Question 3: Application/Analysis
    if concepts:
        primary_concept = concepts[0]
        question3 = {
            'question': f"How would you best apply the concept of {primary_concept} in a practical scenario?",
            'options': [
                f"By understanding and implementing the principles related to {primary_concept}",
                "By ignoring the foundational concepts",
                "By only memorizing definitions",
                "By avoiding practical application"
            ],
            'answer': f"By understanding and implementing the principles related to {primary_concept}"
        }
        questions.append(question3)
    
    return questions

# Streamlit UI
st.set_page_config(page_title="Assignment & Quiz Generator", page_icon="📝", layout="wide")

st.title("📝 Assignment & Quiz Generator")
st.markdown("Generate assignments and quiz questions from any document or topic!")

# Sidebar for input
with st.sidebar:
    st.header("Input Settings")
    input_method = st.radio("Choose input method:", ["Enter Topic", "Paste Document"])
    
    if input_method == "Enter Topic":
        topic = st.text_input("Enter a topic:", placeholder="e.g., Photosynthesis, World War II, Machine Learning")
        document_text = st.text_area("Optional: Add context/details", height=150, 
                                     placeholder="Add any additional information about the topic...")
    else:
        topic = st.text_input("Topic/Document Title:", placeholder="e.g., Chapter 3: Climate Change")
        document_text = st.text_area("Paste your document here:", height=200,
                                     placeholder="Paste the text content of your document here...")

generate_button = st.button("🎯 Generate Assignments & Quiz", type="primary", use_container_width=True)

# Main content area
if generate_button:
    if not topic and not document_text:
        st.error("Please provide either a topic or document text!")
    else:
        # Use topic as fallback if no document text
        text_to_analyze = document_text if document_text else topic
        topic_name = topic if topic else "the provided material"
        
        with st.spinner("Generating assignments and quiz questions..."):
            # Generate content
            assignments = generate_assignments(text_to_analyze, topic_name)
            quiz_questions = generate_quiz_questions(text_to_analyze, topic_name)
            
            # Display results
            st.success("✅ Generation complete!")
            
            # Assignments Section
            st.header("📄 Assignment Questions")
            for i, assignment in enumerate(assignments, 1):
                with st.expander(f"Assignment {i}", expanded=True):
                    st.write(assignment)
            
            st.divider()
            
            # Quiz Section
            st.header("❓ Quiz Questions")
            for i, q in enumerate(quiz_questions, 1):
                with st.expander(f"Question {i}", expanded=True):
                    st.write(f"**{q['question']}**")
                    st.write("")
                    for j, option in enumerate(q['options'], 1):
                        st.write(f"{chr(64+j)}. {option}")
                    
                    # Show answer button
                    if st.button(f"Show Answer", key=f"answer_{i}"):
                        st.success(f"✓ Correct Answer: {q['answer']}")
            
            # Download section
            st.divider()
            st.subheader("📥 Export Results")
            
            # Create downloadable text
            export_text = f"ASSIGNMENTS & QUIZ\nTopic: {topic_name}\n\n"
            export_text += "=" * 50 + "\nASSIGNMENTS\n" + "=" * 50 + "\n\n"
            for i, assignment in enumerate(assignments, 1):
                export_text += f"Assignment {i}:\n{assignment}\n\n"
            
            export_text += "=" * 50 + "\nQUIZ QUESTIONS\n" + "=" * 50 + "\n\n"
            for i, q in enumerate(quiz_questions, 1):
                export_text += f"Question {i}: {q['question']}\n"
                for j, option in enumerate(q['options'], 1):
                    export_text += f"  {chr(64+j)}. {option}\n"
                export_text += f"  Answer: {q['answer']}\n\n"
            
            st.download_button(
                label="Download as Text File",
                data=export_text,
                file_name=f"{topic_name.replace(' ', '_')}_assignments_quiz.txt",
                mime="text/plain"
            )

else:
    # Instructions when no content generated
    st.info("👈 Enter a topic or paste a document in the sidebar, then click 'Generate' to create assignments and quiz questions!")
    
    st.markdown("""
    ### How to use:
    1. **Choose input method**: Select whether you want to enter a topic or paste a document
    2. **Provide content**: Enter your topic and/or paste your document text
    3. **Generate**: Click the generate button to create assignments and quiz questions
    4. **Review**: Examine the generated assignments and quiz questions
    5. **Export**: Download the results as a text file for later use
    
    ### Features:
    - ✏️ Generates 2 essay-style assignment questions
    - ❓ Creates 3 multiple-choice quiz questions with answers
    - 📊 Extracts key concepts from your input
    - 💾 Download results as a text file
    """)

# Footer
st.markdown("---")
st.markdown("*Built with Streamlit | Simple AI-powered content generation*")