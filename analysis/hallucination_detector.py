class HallucinationDetector:

    def detect(self, responses):

        hallucination_phrases = [

            "i don't know",
            "i do not know",
            "not sure",
            "cannot determine",
            "unknown",
            "no information",
            "not available",
            "as an ai",
            "cannot find"
        ]

        hallucination_count = 0

        for response in responses:

            text = response.lower()

            for phrase in hallucination_phrases:

                if phrase in text:

                    hallucination_count += 1
                    break

        risk = hallucination_count / len(responses)

        return risk