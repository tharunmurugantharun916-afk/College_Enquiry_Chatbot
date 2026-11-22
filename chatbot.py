import re

# Replace these sample details with your college's verified information.
COLLEGE_DATA = {
    "courses": {
        "keywords": ["course", "courses", "degree", "program", "programs"],
        "answer": (
            "Our college offers various undergraduate and postgraduate courses. "
            "Please contact the admission office or check the official college website "
            "for the current course list."
        ),
    },
    "admission": {
        "keywords": ["admission", "join", "joining", "apply", "application"],
        "answer": (
            "Admission depends on the course eligibility and the current admission "
            "process. Please contact the college admission office for application dates "
            "and required documents."
        ),
    },
    "fees": {
        "keywords": ["fee", "fees", "cost", "payment", "tuition"],
        "answer": (
            "Fees vary by course and academic year. Please contact the college office "
            "for the latest official fee structure."
        ),
    },
    "hostel": {
        "keywords": ["hostel", "room", "accommodation", "stay"],
        "answer": (
            "For hostel availability, facilities, rules and fees, please contact "
            "the college hostel office."
        ),
    },
    "departments": {
        "keywords": ["department", "departments", "branch", "branches"],
        "answer": (
            "Our college has academic departments for different fields of study. "
            "Please refer to the official college website for the current department list."
        ),
    },
    "placements": {
        "keywords": ["placement", "placements", "job", "jobs", "company", "companies"],
        "answer": (
            "The placement cell may provide career guidance, training and recruitment "
            "support. Contact the placement office for current placement information."
        ),
    },
    "facilities": {
        "keywords": ["facility", "facilities", "library", "lab", "laboratory", "sports"],
        "answer": (
            "Campus facilities may include libraries, laboratories and sports areas. "
            "Contact the college office for the facilities available at your campus."
        ),
    },
    "contact": {
        "keywords": ["contact", "phone", "email", "office", "number"],
        "answer": (
            "Please visit the official college website or contact the college office "
            "for verified phone numbers and email addresses."
        ),
    },
    "location": {
        "keywords": ["location", "address", "where", "directions", "map"],
        "answer": (
            "Please check the official college website for the verified campus address "
            "and map directions."
        ),
    },
}

def get_response(message: str) -> str:
    text = re.sub(r"[^a-zA-Z\s]", " ", message.lower())
    words = set(text.split())

    if not words:
        return "Please enter a question."

    if words.intersection({"hi", "hello", "hey"}):
        return (
            "Hello! Welcome to the College Enquiry Chatbot. "
            "You can ask me about courses, admission, fees, hostel, placements, "
            "departments, facilities, contact details or location."
        )

    if words.intersection({"thanks", "thank"}):
        return "You're welcome! Feel free to ask another college enquiry."

    best_answer = None
    best_score = 0

    for item in COLLEGE_DATA.values():
        score = sum(1 for keyword in item["keywords"] if keyword in words)
        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    if best_answer:
        return best_answer

    return (
        "Sorry, I couldn't find an answer to that question. "
        "Try asking about courses, admission, fees, hostel, placements or facilities."
    )
