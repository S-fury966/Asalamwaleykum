from transformers import pipeline
import torch
import wikipedia
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer


class HallucinationDetector:

    def __init__(self):

        # GPU usage
        device = 0 if torch.cuda.is_available() else -1

        print(f"Hallucination model running on {'GPU' if device == 0 else 'CPU'}")

        # NLI model
        self.nli = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
            device=device
        )

        # embedding model for contradiction detection
        self.embedder = SentenceTransformer(
            "all-MiniLM-L6-v2",
            device="cuda" if torch.cuda.is_available() else "cpu"
        )

    # ------------------------------------------------
    # 1. NLI Plausibility Check
    # ------------------------------------------------
    def nli_check(self, response):

        labels = ["factually correct", "hallucinated"]

        result = self.nli(
            response,
            candidate_labels=labels
        )

        prediction = result["labels"][0]

        return 1 if prediction == "hallucinated" else 0

    # ------------------------------------------------
    # 2. Wikipedia Verification
    # ------------------------------------------------
    def wikipedia_check(self, response):

        try:

            keyword = response.split()[0]

            summary = wikipedia.summary(keyword, sentences=2)

            if keyword.lower() in summary.lower():
                return 0

            return 1

        except:

            return 1

    # ------------------------------------------------
    # 3. Response Contradiction Detection
    # ------------------------------------------------
    def contradiction_check(self, responses):

        embeddings = self.embedder.encode(responses)

        sim_matrix = cosine_similarity(embeddings)

        contradictions = 0

        for i in range(len(responses)):
            for j in range(i + 1, len(responses)):

                if sim_matrix[i][j] < 0.3:
                    contradictions += 1

        max_pairs = len(responses) * (len(responses) - 1) / 2

        return contradictions / max_pairs if max_pairs > 0 else 0

    # ------------------------------------------------
    # Final Hallucination Score
    # ------------------------------------------------
    def detect(self, responses):

        nli_score = 0
        wiki_score = 0

        for r in responses:

            print("\nChecking response:", r)

            nli_score += self.nli_check(r)
            wiki_score += self.wikipedia_check(r)

        nli_score /= len(responses)
        wiki_score /= len(responses)

        contradiction_score = self.contradiction_check(responses)

        # weighted hallucination risk
        risk = (
            0.4 * nli_score +
            0.3 * wiki_score +
            0.3 * contradiction_score
        )

        return risk