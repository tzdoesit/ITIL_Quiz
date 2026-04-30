
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
    },
    
    {
        "question": "What is the PRIMARY use of a change schedule?",
        "options": ["To support 'incident management' and improvement planning", "To manage emergency changes",
                    "To plan changes and help avoid conflicts", "To manage standard changes"],
        "answer": 2,
        "topic": "ITIL",
        "reasoning": """
                    While it can be used after deploying a change, this is not the main use of the change schedule. "The change schedule is used to help plan changes, assist in communication, avoid conflicts, and assign resources. It can also be used after changes have been deployed to provide information needed for incident management, problem management, and improvement planning."
                    the correct answer was:

                    To plan changes and help avoid conflicts
                    """
        
    },
     
    {
        "question": "Which is the BEST example of an emergency change?",
        "options": [ "The implementation of a planned new release of a software application", "A low-risk computer upgrade implemented as a service request",
                     "The implementation of a security patch to a critical software application", "A scheduled major hardware and software implementation"],
        "answer": 2,
        "topic": "ITIL",
        "reasoning": """
                    
                    
                    
                    """
        
    },
     
    {
        "question": "What are the key inputs to the ITIL service value system?",
        "options": [ "Products and services", "Opportunity and demand",
                     "Outcomes and value", "Governance and practices"],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """
                    The ITIL Service value system: "continually co-creates value with all stakeholders through the use and management of products and services" but these products and services are created by the service value system, they are not inputs to it.
                    the correct answer was:

                    Opportunity and demand            
                    """
        
    },
     
    {
        "question": "Which value chain activity provides a good understanding of stakeholder needs?",
        "options": [ "Deliver and support", "Engage",
                     "Design and transition", "Plan"],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """
                    The purpose of the 'engage' value chain activity "is to provide a good understanding of stakeholder needs, transparency, and continual engagement and good relationships with all stakeholders."
                    the correct answer was:

                    Engage                  
                    """
        
    },
# region Test
    {
        "question": "What is the correct order for change control activities?",
        "options": [ "Authorize, assess, deploy", "Assess, deploy, authorize",
                     "Assess, authorize, deploy", "Authorize, deploy, assess"],
        "answer": 2,
        "topic": "ITIL",
        "reasoning": """
                    Correct.  "All changes should be assessed by people who are able to understand the risks and the expected benefits; the changes must then be authorized before they are deployed."
                    the correct answer was:

                    Assess, authorize, deploy
                    """
        
    },
     
    {
        "question": """Identify the missing word in the following sentence.   The purpose of the 'service request management' practice is to support the agreed quality of a service by handling all [?], user-initiated service requests in an effective and user-friendly manner.""",
        "options": [ "manual", "low-priority",
                     "pre-defined", "emergency"],
        "answer": 2,
        "topic": "ITIL",
        "reasoning": """
                    "The purpose of the service request management practice is to support the agreed quality of a service by handling all pre-defined, user-initiated service requests in an effective and user-friendly manner."
                    the correct answer was:

                    pre-defined
                    """
        
    },
     
    {
        "question": "Which phase of 'problem management' includes analysing incident trends?",
        "options": [ "Error control", "Problem identification",
                     "Change control", "Problem control"],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """
                    "Problem identification activities identify and log problems. This includes: Performing trend analysis of incident records"
                    the correct answer was:

                    Problem identification
                    """
        
    },
     
    {
        "question": "Which TWO are required for successful continual improvement?    1. A single continual improvement register 2. High level commitment and leadership 3. Including contribution to improvement in staff objectives 4. A wide variety of improvement methods",
        "options": [ "1 and 2", "1 and 4",
                     "3 and 4", "2 and 3"],
        "answer": 3,
        "topic": "ITIL",
        "reasoning": """
                    (2) "The highest levels of the organization need to take responsibility for embedding continual improvement into the way that people think and work. Without their leadership and visible commitment to continual improvement, attitudes, behaviour and culture will not evolve to a point where improvements are considered in everything that is done, at all levels." (3) "To ensure this is more than a good intention, it is wise to include contribution to continual improvement in all job descriptions and every employee’s objectives".
                    the correct answer was:

                    2 and 3
                    """
        
    },
     
    {
        "question": "Which guiding principle emphasizes the need to understand the flow of work in progress, identify bottlenecks, and uncover waste?",
        "options": [ "Collaborate and promote visibility", "Think and work holistically",
                     "Keep it simple and practical", "Focus on value"],
        "answer": 0,
        "topic": "ITIL",
        "reasoning": """
                    ‘Collaborate and promote’ visibility states "Insufficient visibility of work leads to poor decision-making, which in turn impacts the organization’s ability to improve internal capabilities. It will then become difficult to drive improvements as it will not be clear which ones are likely to have the greatest positive impact on results. To avoid this, the organization needs to perform such critical analysis activities as: understanding the flow of work in progress; identifying bottlenecks, as well as excess capacity; and uncovering waste".
                    the correct answer was:

                    Collaborate and promote visibility
                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    },
     
    {
        "question": "",
        "options": [ "", "",
                     "", ""],
        "answer": ,
        "topic": "ITIL",
        "reasoning": """

                    """
        
    }
# endregion    
    
]

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)
    
print(f"Generated {len(questions)} questions.")