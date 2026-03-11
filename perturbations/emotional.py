def emotional(prompt):

    prompts = [

        # Polite tone
        "Please explain kindly: " + prompt,
        "Could you politely explain: " + prompt,

        # Angry tone
        "Explain this right now: " + prompt,
        "Why is this so confusing? Explain: " + prompt,

        # Excited tone
        "Wow! Can you explain this amazing topic: " + prompt,
        "I'm really curious! Explain: " + prompt,

        # Sad tone
        "I'm feeling a bit lost, please explain: " + prompt,
        "This topic makes me confused and sad, explain: " + prompt,

        # Fearful tone
        "I'm worried I don't understand this, explain: " + prompt,
        "This topic scares me, please explain: " + prompt,

        # Sarcastic tone
        "Obviously everyone knows this... but explain: " + prompt,
        "Maybe I'm the only one who doesn't get it, explain: " + prompt,

        # Curious tone
        "I'm really curious about this, explain: " + prompt,
        "Can you help me understand: " + prompt
    ]

    return prompts