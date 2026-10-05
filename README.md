# Multilingual Toxicity Detection — SNLP

Group 21's course project for **ELEC-E5550 — Statistical Natural Language Processing D**, Aalto University (2025). The project explores toxicity classification in **English, German, and Finnish** using an LSTM baseline and transformer models with LoRA fine-tuning.

**Result: 2nd place, with multilingual F1 of 0.85 — less than 1% behind first place.** Both teams' multilingual F1 scores round to 0.85 in the supplied leaderboard.

## Competition results

Group 21 · submission **260468** · **2025-04-06 15:23**.

| Evaluation | F1 | Accuracy | Precision | Recall |
| --- | ---: | ---: | ---: | ---: |
| Multilingual | **0.85** | 0.87 | 0.81 | 0.90 |
| English | 0.95 | 0.95 | 0.94 | 0.97 |
| German | 0.65 | 0.80 | 0.56 | 0.76 |
| Finnish | 0.91 | 0.85 | 0.93 | 0.89 |

## Code in this repository

This repository publishes Nguyen Vu Minh's German toxicity-detection code. The team's English and Finnish implementations are kept locally and excluded from version control.

- **German:** transformer/LoRA training, preprocessing, and inference experiments.

## Competition rules

- Classify short texts as **toxic or non-toxic**.
- The provided training data is **English**; development and test data contain **English, German, and Finnish** texts.
- The course data is licensed under a specific agreement and **must not be redistributed**.
- Techniques covered in the course and other approaches are allowed.
- Additional data is allowed if it is **publicly available**.
- Avoid extreme-scale models.
- Methods must be usable in a **Jupyter Notebook with a single GPU**.

## Team and contributions

This is a **team project**.

| Contributor | GitHub | Contribution |
| --- | --- | --- |
| Nguyen Vu Minh | [nguyenvuminhh](https://github.com/nguyenvuminhh) | German toxicity detection. |
| Aapo Eronen | [aapoero](https://github.com/aapoero) | Finnish toxicity detection. |
| Jere Malinen | [proteinbor](https://github.com/proteinbor) | LSTM baseline. |
| Pouya Amiri | [Pouya-Amiri](https://github.com/Pouya-Amiri) | English toxicity detection. |
