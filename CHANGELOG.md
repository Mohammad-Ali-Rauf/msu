# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] - 2025-09-04
### Added
- Initial project structure: `core/`, `data/`, `comparisons/`.
- Added 100 scraped Urdu stories (raw + cleaned).
- Implemented typo mapping and frequency analysis scripts.
- Draft `lexicon.json` file created.

### Notes
- First research prototype for **Modern Standard Urdu (MSU)**.  
- Lays the foundation for grammar, lexicon, and style guide development.  
- Not intended for production use — this version is exploratory and experimental.

## [0.1.1] - 2025-09-05
### Added
- Completed **grammar module**:
  - `beginner.md` – Basic grammar rules and beginner exercises.
  - `intermediate.md` – Intermediate grammar rules and complex exercises.
  - `advanced.md` – Advanced grammatical structures and nuances.
  - `native_speakers.md` – Guidelines for natural, idiomatic Urdu usage.
- Updated `lexicon/dict.json` to match frequency analysis outputs.
- Improved **typo_mapper.py** and **frequency_analyzer.py** for full tokenization and lexicon integration.

### Notes
- This release solidifies the **MSU Standard Urdu Grammar** foundation.
- Ready for iterative enrichment with new stories, lexicon entries, and style refinements.

