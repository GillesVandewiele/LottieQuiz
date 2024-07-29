import streamlit as st

# Mockup data for the quiz
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic", "Indian", "Arctic", "Pacific"],
        "answer": "Pacific"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "J.K. Rowling", "William Shakespeare", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    {
        "question": "What is the smallest prime number?",
        "options": ["0", "1", "2", "3"],
        "answer": "2"
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Gold", "Oxygen", "Silver", "Hydrogen"],
        "answer": "Oxygen"
    },
    {
        "question": "In which year did the Titanic sink?",
        "options": ["1912", "1916", "1920", "1925"],
        "answer": "1912"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "options": ["Gold", "Iron", "Diamond", "Platinum"],
        "answer": "Diamond"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
        "answer": "Blue Whale"
    }
]

def main():
    st.title("Simple Quiz App")

    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answers = []

    current_question = st.session_state.current_question
    score = st.session_state.score
    answers = st.session_state.answers

    if current_question < len(questions):
        q = questions[current_question]
        st.subheader(f"Question {current_question+1}")
        user_answer = st.radio(q["question"], q["options"], key=f"q{current_question}")
        
        if st.button("Submit"):
            if user_answer == q["answer"]:
                st.session_state.score += 1
            st.session_state.answers.append(user_answer)
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.subheader("Your Results")
        st.write(f"Your score: {score} out of {len(questions)}")
        
        if score == len(questions):
            st.success("Perfect score! You're a quiz master!")
        elif score >= len(questions) * 0.7:
            st.success("Great job! You know your stuff!")
        elif score >= len(questions) * 0.4:
            st.warning("Not bad, but there's room for improvement.")
        else:
            st.error("You might want to brush up on your knowledge.")

if __name__ == "__main__":
    main()