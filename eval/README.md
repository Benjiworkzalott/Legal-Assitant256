# Evaluation set

One JSON object per line in `questions.jsonl`:

```json
{"id": "q001", "question_lang": "fr", "question": "...", "gold": [{"law_id": "SR ...", "article_num": "Art. ..."}]}
```

Rules:
- Write questions in French and English only (languages you can validate yourself).
- Every question needs at least one gold article, checked by hand against Fedlex.
- Include some questions whose answer is NOT in the corpus (the system must say "no answer").
- Never edit gold labels after seeing system output without a commit message explaining why.
