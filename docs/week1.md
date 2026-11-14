# Week 1: foundations and a first cited answer

Goal by Sunday: CI is green, you can load real Fedlex articles into chunks, and a question returns a cited answer locally.

## Day 1: repo and tooling (about 2 h)
- [ ] Create a GitHub repo named `fedlexqa` and push this scaffold (`git init`, first commit, push).
- [ ] Create a venv and run `pip install -e ".[dev]"`.
- [ ] Run `pytest`, `ruff check .`, `ruff format .`, and `mypy`. Fix anything red.
- [ ] Confirm the GitHub Actions run is green. Add the CI badge to the README.
- [ ] Work on a branch per task and merge through pull requests, even though you are alone. Small commits.

## Day 2: reach the data (about 2 h)
- [ ] Work through the Fedlex SPARQL tutorial: https://swiss.github.io/fedlex-jolux/introduction.html
- [ ] Try `run_sparql` in `src/fedlexqa/ingestion/fedlex.py` against https://fedlex.data.admin.ch/sparqlendpoint
- [ ] Pick a **small starter corpus** of 5 to 10 laws that exist in FR and DE (e.g. data protection, a civil code excerpt, consumer protection). Do not ingest everything yet.
- [ ] Note in `docs/design.md` which laws you chose, and why.

## Day 3: download and parse (about 3 h)
- [ ] Download the XML for your starter laws into `data/raw/` (this folder is git-ignored).
- [ ] Run `chunk_articles` on the real files. Fix the parser where real documents differ from the test fixture (nested articles, tables, annexes). Add a test for each bug you fix.
- [ ] Print chunk length statistics. Decide what to do with very long articles (split by paragraph?). Write the decision in `docs/design.md`.

## Day 4: first retrieval (about 3 h)
- [ ] Install LlamaIndex and a multilingual embedding model (start with one, e.g. multilingual-e5-small, to keep it fast on a laptop).
- [ ] Build a simple dense index over your chunks. Keep the chunk metadata (law, article, language).
- [ ] Write a script that takes a question and prints the top 5 chunks with their citations.

## Day 5: first answer (about 2 h)
- [ ] Add a generation step through one cheap LLM API behind a small interface (`generate(question, chunks) -> answer`), so you can swap providers later.
- [ ] Prompt rule: answer only from the provided articles, cite them, and say "no answer found" when they do not contain it.

## Weekend: evaluation set, first batch (about 3 h)
- [ ] Write the first 20 questions in `eval/questions.jsonl` (FR and EN), with gold articles verified by hand on fedlex.admin.ch.
- [ ] Include at least 3 questions that should return "no answer".
- [ ] Compute recall@5 on those 20. This is your baseline number. Write it down in the README.

## Definition of done
- CI green on `main`
- At least 15 commits with meaningful messages
- A baseline recall@5 number recorded
- `docs/design.md` has your corpus choice and chunking decision
