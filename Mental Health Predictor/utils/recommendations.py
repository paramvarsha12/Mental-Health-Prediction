def get_advice(user_input):
    advice = []

    if user_input.get("benefits") == "No":
        advice.append("Your workplace does not offer mental health benefits. Consider seeking external support through NGOs, online counseling, or independent therapists.")

    if user_input.get("care_options") == "Don't know":
        advice.append("You're unsure about available care options. Check your company's HR portal or talk to a trusted colleague or manager.")

    if user_input.get("remote_work") == "Yes":
        advice.append("Since you work remotely, try to stay socially connected. Isolation can increase stress, so make time for calls or virtual meetups.")

    if user_input.get("mental_health_interview") == "Maybe":
        advice.append("If you're unsure about discussing mental health during interviews, practice safe responses like 'I focus on personal wellness and work-life balance'.")

    if user_input.get("wellness_program") == "No":
        advice.append("Your company doesn't offer wellness programs. Explore free wellness resources or apps like Wysa or MindShift.")

    if user_input.get("family_history") == "Yes":
        advice.append("Since you have a family history of mental health issues, being proactive with mindfulness, check-ins, and therapy is a great idea.")

    if user_input.get("coworkers") in ["No", "Some of them"]:
        advice.append("If you're uncomfortable speaking to coworkers about mental health, consider talking to an external therapist or support group.")

    if not advice:
        advice.append("You're doing well based on your answers. Keep checking in with yourself and stay mentally fit.")

    return advice
