# Digital Economy Exam Prep

Study platform for **Management and Organization in the Digital Economy** (Università Cattolica, 2026–2027), built from my course notes for the written exam on 2 December 2026.

- **Learn**: key points and definitions for all 18 lectures
- **Flashcards**: 205 cards; mark "Got it" or "Again"
- **Quiz**: 182 multiple-choice + 50 true/false questions, with explanations
- **Mock exam**: Part A has 30 questions in 30 minutes; Part B is a 90-minute written assignment
- **Assignments**: 14 cases with model answers and self-scoring checklists
- **Mistakes**: review and retry questions you got wrong

Progress is saved in your browser.

## Run it

Open with any static web server (it loads `bank.json`):

```
python3 -m http.server
```

Then go to http://localhost:8000. You can also enable GitHub Pages on this repo.

## Edit the questions

The question bank is in `source/` (`bank1.py` to `bank4.py`, `assign.py`). After editing, rebuild:

```
cd source && python3 build_data.py && cp bank.json ..
```
