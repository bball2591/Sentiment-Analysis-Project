from nltk.sentiment import SentimentIntensityAnalyzer

class SentimentAnalyzer:
    """
    This will be a simple class for a sentiment analyzer using NLTK's Vader 
    """
    
    def __init__(self):
        self._analyzer = SentimentIntensityAnalyzer()
        
    def score(self, text: str ) -> dict:
        """
        Return VADER scores for the given text.
        Scores include:
          - neg: negativity (0 to 1)
          - neu: neutrality (0 to 1)
          - pos: positivity (0 to 1)
          - compound: overall sentiment from -1 (very negative) to +1 (very positive)

        """
        if not isinstance(text, str):
           raise TypeError("text must be a string")
        return self._analyzer.polarity_scores(text)
    
    def label(self, text: str, pos_threshold: float = 0.05, neg_threshold: float = -0.05) -> str:
        """
        Turn the compound score into a label: 'positive', 'negative', or 'neutral'.
        Thresholds can be adjusted to make the classifier more or less strict.
        """
        scores = self.score(text)
        compound = scores["compound"]

        if compound >= pos_threshold:
            return "positive"
        elif compound <= neg_threshold:
            return "negative"
        else:
            return "neutral"

    def analyze(self, text: str) -> dict:
        """
        Convenience method that returns both scores and label.
        """
        scores = self.score(text)
        scores["label"] = self.label(text)
        return scores

