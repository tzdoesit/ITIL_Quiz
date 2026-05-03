
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
        "question": "Which guiding principle recommends eliminating a process, service or action if it does not provide value or a useful outcome?",
        "options": [ "Collaborate and promote visibility", "Progress iteratively with feedback",
                     "Think and work holistically", "Keep it simple and practical"],
        "answer": 3,
        "topic": "ITIL",
        "reasoning": """
                    The guiding principle 'collaborate and promote visibility' recommends involving many people in improvement activities. It is not concerned with eliminating process and services. "When initiatives involve the right people in the correct roles, efforts benefit from better buy-in, more relevance (because better information is available for decision-making) and increased likelihood of long-term success".
                    the correct answer was:

                    Keep it simple and practical
                    """
        
    },
     
    {
        "question": "Identify the missing word in the following sentence.   The purpose of the 'information security management practice' is to [?] the organization's information.",
        "options": [ "protect", "store",
                     "provide", "audit"],
        "answer": 0,
        "topic": "ITIL",
        "reasoning": """
                    "The purpose of the information security management practice is to protect the information needed by the organization to conduct its business. This includes understanding and managing risks to the confidentiality, integrity and availability of information, as well as other aspects of information security such as authentication (ensuring someone is who they claim to be) and non-repudiation (ensuring that someone can’t deny that they took an action)."
                    the correct answer was:

                    protect
                    """
        
    },
     
    {
        "question": "Which practice provides support for managing feedback, compliments and complaints from users?",
        "options": [ "Problem management", "Incident management",
                     "Change control", "Service request management"],
        "answer": 3,
        "topic": "ITIL",
        "reasoning": """
                    "The purpose of the service request management practice is to support the agreed quality of a service by handling all pre-defined, user-initiated service requests in an effective and user-friendly manner," and "Each service request may include one or more of the following: ... feedback, compliments, and complaints (for example, complaints about a new interface or compliments to a support team)."
                    the correct answer was:

                    Service request management
                    """
        
    },
     
    {
        "question": "Which does the 'supplier management' practice support?",
        "options": [ "Alignment of the organization's services with business needs", "Provision of seamless, quality products and services",
                     "Handling pre-defined, user-initiated service requests", "Capturing demand for incident resolution and service requests"],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """
                    The purpose of the 'supplier management' practice is "to ensure that the organization’s suppliers and their performances are managed appropriately to support the seamless provision of quality products and services."
                    the correct answer was:

                    Provision of seamless, quality products and services
                    """
        
    },
     
    {
        "question": "How does customer engagement contribute to the 'service level management' practice? 1. It captures information that metrics can be based on 2. It ensures the organization meets defined service levels 3. It defines the workflows for service requests 4. It supports progress discussions",
        "options": [ "1 and 2", "2 and 3",
                     "3 and 4", "1 and 4"],
        "answer": 3,
        "topic": "ITIL",
        "reasoning": """
                    (2) Service level management "ensures the organization meets the defined service levels through the collection, analysis, storage, and reporting of the relevant metrics for the identified services," not just through customer engagement.
                    the correct answer was:

                    1 and 4
                    """
        
    },
     
    {
        "question": "Which practice has a purpose that includes helping the organization to maximize value, control costs and manage risks?",
        "options": [ "Release management", "Service Desk",
                     "IT asset management", "Relationship management"],
        "answer": 2,
        "topic": "ITIL",
        "reasoning": """
                    "The purpose of the relationship management practice is to establish and nurture the links between the organization and its stakeholders at strategic and tactical levels."
                    the correct answer was:

                    IT asset management
                    """
        
    },
     
    {
        "question": "What role do service providers and service consumers have in relation to risk?",
        "options": [ "Consumers should manage the detailed level of risk on behalf of the service provider", "Service providers should manage the detailed level of risk on behalf of the consumer",
                     "Consumers help service providers to achieve outcomes, which reduces service provider risk", ""],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """
                    "It is the duty of the provider to manage the detailed level of risk on behalf of the consumer".
                    the correct answer was:

                    Service providers should manage the detailed level of risk on behalf of the consumer
                    """
        
    },
     
    {
        "question": "Which is a recommendation of the 'continual improvement' practice?",
        "options": [ "All improvements should be managed as multi-phase projects", "Continual improvement' should be isolated from other practices",
                     "External suppliers should be excluded from improvement initiatives", """There should at least be a small team dedicated to leading 'continual improvement' efforts"""],
        "answer": 1,
        "topic": "ITIL",
        "reasoning": """

                    """
    }
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # },
     
    # {
    #     "question": "",
    #     "options": [ "", "",
    #                  "", ""],
    #     "answer": ,
    #     "topic": "ITIL",
    #     "reasoning": """

    #                 """
        
    # }
# endregion    
    
]

with open("questions.json", "w") as f:
    json.dump(questions, f, indent=2)
    
print(f"Generated {len(questions)} questions.")