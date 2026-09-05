# Charter — the stochastics thread

## Purpose

Master the material of Ross, *Introduction to Probability Models* — **but not through Ross.**

Build first (simulations, notebooks, real data), formalise after. Ross is the **benchmark and
examination layer, not the curriculum**. The text is opened only after a build, with a named
question, for no more than twenty minutes.

This method is settled. It was tested both ways over two months and text-first reliably killed
the thread. Boredom and energy collapse are a *format* signal, not a signal about the material.

## Success criterion

Open a chapter's exercises cold and ace them — because the knowledge is deep, not because the
prose was read.

That is the only test that counts. "I read the chapter" and "the notebook runs" are both
insufficient. The exercises are attempted **LLM-free, at the start of the following session**,
before anything new is built.

## Invariants

These hold for every lab and every notebook in this repo.

1. **Every claim runs.** No assertion sits in prose without code that witnesses it.
2. **Predictions on paper before running.** The gap between gut and truth is the curriculum;
   losing the prediction loses the lesson. Wrong guesses get recorded, not quietly corrected.
3. **Tripwires against theory, not against output.** Each invariant gets its own named test
   asserting a hand-derived closed form. A test that checks a result against its own arithmetic
   is worth nothing.
4. **A hand-checkable example for anything with an index in it.** Small enough to count by eye.
5. **Own words, or it didn't happen.** Prose cells marked ✍️ are written unaided. The writing
   *is* the revision; an LLM-written explanation is a skipped rep.
6. **Surprises go to `notes/LORE.md`** — one line, dated. Bugs are curriculum. Decisions are not
   lore; they go in the charter or an ADR.

## The cord

**Three consecutive text-decoding exchanges without running code = stop and build instead.**

Either party can pull it. This is the single most load-bearing rule here; it is what stops the
thread dying the way it died before.

## Scope ladder

**Supported now**
- Ch. 4 Markov chains: definitions, Markov property, state augmentation, Chapman–Kolmogorov,
  classification (accessible / communicating / recurrent / transient), stationary distributions,
  mean first passage, spell lengths
- The founding example: the 3-state bunker-price regime chain
- Bonus-Malus premium ladder, end-to-end, nature-vs-posited split

**Next**
- Notebook 01 prose backfill (✍️ cells) + Ross ch.4 exercise numbers pencilled in
- Ross ch.4 exercises attempted cold — this is the open audit, nothing has been examined yet
- Notebook 02: hidden regimes — HMM on real price data, how many regimes reality supports

**Deferred**
- 03 ruin and absorption (4.5-ish) · 04 arrival streams / Poisson (ch. 5) ·
  05 Bonus-Malus as a full pricing study
- Ch. 4.4 limiting probabilities read properly (already computed empirically — the section will
  be confirmation, not new material)

**Out of scope**
- Reading Ross front-to-back
- Building a curriculum, syllabus or study plan. That failure mode is what
  `archive/maths-notes/` is a monument to. Time-boxed stage plans with "search keywords" are the
  thing that did not work.
- Physics / biology / complex-systems tracks. Parked in the archive; not this thread.

## Non-goals

The code here is not a library and will not be packaged for anyone else. It exists to be
*written*, and its readability to a future self is worth more than its reusability. Where a
choice arises between a clean abstraction and a legible derivation, the derivation wins.

## Anchor numbers

Everything downstream is checked against these. If one of them moves, something is wrong.

| Quantity | Value |
|---|---|
| Regime chain π (Quiet / Trending / Volatile) | 0.6338 / 0.2676 / 0.0986 |
| Mean first passage Volatile → Quiet, h_V | 20/3 ≈ 6.667 |
| Mean first passage Trending → Quiet, h_T | 50/9 ≈ 5.556 |
| Mean pure-Volatile spell | 1/(1−0.6) = 2.5 |
| Bonus-Malus π at λ=1 | 0.0707 / 0.1214 / 0.2594 / 0.5484 |
| Bonus-Malus average premium at λ=1 | €477.34 |
