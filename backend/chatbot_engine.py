from pathlib import Path
from intent_mapper import detect_intent

BASE_DIR = Path(__file__).resolve().parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"

def load_text(filename: str) -> str:
    return (KNOWLEDGE_DIR / filename).read_text(
        encoding="utf-8"
    ).strip()

# Knowledge sources (NOT returned directly)
PROFILE_TEXT = load_text("futurelab_profile.txt")
SERVICES_TEXT = load_text("services.txt")
WORKSHOPS_TEXT = load_text("workshops.txt")


def get_response(user_input: str) -> str:
    intent = detect_intent(user_input)
    q = user_input.lower()

    # -------------------------------
    # COMPANY / OVERVIEW
    # -------------------------------
    if intent == "company":
        if "what is" in q or "kind of company" in q:
            return (
                "Futurelab Studios is an AI enablement studio. We help organizations "
                "and individuals adopt artificial intelligence in a practical, "
                "responsible, and meaningful way."
            )

        if "who are you" in q or "about you" in q:
            return (
                "I represent Futurelab Studios. We work at the intersection of "
                "technology, education, and product development, helping teams "
                "use AI effectively in real-world scenarios."
            )

        return (
            "Futurelab Studios focuses on enabling thoughtful and practical AI adoption "
            "across organizations and communities globally."
        )

    # -------------------------------
    # SERVICES / CONSULTING
    # -------------------------------
    if intent == "services":
        if "consult" in q or "consulting" in q:
            return (
                "Yes, Futurelab provides AI consulting. We help organizations identify "
                "real use cases, design AI-driven workflows, and plan structured AI "
                "adoption aligned with business goals."
            )

        if "automation" in q or "workflows" in q:
            return (
                "We help teams automate and improve workflows using AI by applying it "
                "to real business challenges, with a strong focus on usability and "
                "long-term impact."
            )

        if "solutions" in q or "tools" in q:
            return (
                "Futurelab builds custom AI solutions such as knowledge chatbots, "
                "voice-based AI agents, and retrieval-augmented systems that integrate "
                "smoothly into existing business processes."
            )

        return (
            "Futurelab helps organizations adopt AI through strategic consulting, "
            "custom-built AI tools, and structured adoption planning."
        )

    # -------------------------------
    # WORKSHOPS / TRAINING
    # -------------------------------
    if intent == "workshops":
        if "beginner" in q or "essentials" in q:
            return (
                "We offer AI Essentials workshops designed for all team members, "
                "focusing on AI fundamentals, safe usage, and everyday productivity."
            )

        if "advanced" in q or "builders" in q:
            return (
                "For advanced teams, we run AI Builder programs where participants "
                "prototype and develop real AI tools through guided, hands-on sessions."
            )

        return (
            "Futurelab conducts hands-on AI enablement workshops for individuals, "
            "teams, and organizations, focused on practical skills and real-world use cases."
        )

    # -------------------------------
    # TOOLS / PRODUCTS
    # -------------------------------
    if intent == "tools":
        return (
            "Futurelab builds AI-first tools including knowledge chatbots, AI voice agents, "
            "and retrieval-augmented systems that support customer service, learning, "
            "sales, and internal operations."
        )

    # -------------------------------
    # FRACTIONAL CTO
    # -------------------------------
    if intent == "cto":
        return (
            "Through Fractional CTO-as-a-Service, Futurelab provides on-demand "
            "technology leadership, AI strategy guidance, and architecture planning "
            "without the need for a full-time CTO."
        )

    # -------------------------------
    # GLOBAL
    # -------------------------------
    if intent == "global":
        return (
            "Yes, Futurelab Studios works with a global audience across industries "
            "and regions. Our programs and tools are designed to be culturally and "
            "organizationally adaptable."
        )

    # -------------------------------
    # CONTACT / NEXT STEPS
    # -------------------------------
    if intent == "contact":
        return (
            "You can get in touch with Futurelab Studios through our website to "
            "discuss AI workshops, custom solutions, or strategic support."
        )

    # -------------------------------
    # SMART FALLBACK (NEVER DUMB)
    # -------------------------------
    return (
        "Futurelab Studios helps organizations and individuals adopt AI through "
        "training, custom tools, and strategic guidance. You can ask about services, "
        "workshops, AI tools, or how to get started."
    )
