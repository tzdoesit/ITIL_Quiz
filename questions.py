
import json

questions = [
    
    {
        "question": "What does ITIL stand for?",
        "options": ["Internal Technology Intrinsic Language", "Information Technology Internal Learning",
                   "Interoperability Trust Infrastructure Language", "Information Technology Infrastructure Library"],
        "answer": 3,
        "topic": "Information Technology"
    },
    
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit", "Computer Personal Unit",
                    "Central Program Utility", "Core Processing Unit"],
        "answer": 0,    #index of correct option 
        "topic": "Hardware"
    },
    
    {
        "question": "Which data structure uses LIFO order?",
        "options": ["Queue", "Stack", "Array", "Linked List"],
        "answer": 1,
        "topic": "Data Structures"
    },
    
    {
        "question": "What is Big-O Notation used for?",
        "options": ["Styling Code", "Naming Variables",
                    "Measuring algorithm effiency", "Writing comments"],
        "answer": 2,
        "topic": "Algorithms"
    }
 
    
]

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)
    
print(f"Generated {len(questions)} questions.")