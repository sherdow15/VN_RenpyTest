# Ren'Py Narrative Systems Demo

This repository contains a small Ren'Py prototype created to demonstrate branching narrative logic, state-driven dialogue, and conditional story flow.

The project implements a short interactive "Moment" where the player reconnects with a friend after a long time apart. The conversation dynamically changes depending on past memories the player chooses to recall.

This sample focuses on **narrative systems design and scripting**, not on art or production assets.

---

## Purpose

This project was built as a technical demonstration of how narrative logic can be translated into Ren'Py code using:

- state variables
- conditional dialogue
- branching choices
- narrative consequences

The goal is to showcase a clean and testable implementation of a small narrative interaction similar to the "Moments" structure used in many visual novel pipelines.

---

## Features

- Branching dialogue structure
- State-driven narrative responses
- Conditional choices and outcomes
- Memory-based narrative influence
- Multiple endings
- Debug overlay for rapid testing

---

## Core Systems

The narrative interaction is driven by several state variables:

| Variable | Description |
|--------|-------------|
| `tone` | Overall emotional tone of the conversation |
| `trust` | How open Alex is to continuing the relationship |
| `mem_pos` | Number of positive memories recalled |
| `mem_pain` | Number of painful memories recalled |
| `apology_made` | Tracks whether the player attempted reconciliation |
| `bold` | Personality toggle that changes dialogue style |

Memories influence the conversation more strongly than present-day dialogue choices.

For example:

- Positive memories increase emotional tone and trust.
- Painful memories create tension and unlock different dialogue paths.
- Certain thresholds unlock new conversation options or endings.

---

## Debug Tools

A debug overlay is included to quickly test different narrative states.

Press:

to open the debug panel.

From the overlay you can:

- modify tone and trust
- toggle flags
- increment memory counters
- jump directly to the narrative moment

This allows rapid testing of different story routes without replaying the entire scene.

---

## Structure
