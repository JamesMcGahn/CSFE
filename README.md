# Summary
This is a personal curriculum, shared publicly for transparency and reuse.

This curriculum is a **professional-grade education in computer science**, designed for
working software engineers who want deep, durable foundations and senior/staff-level judgment.

It is inspired by OSSU’s original goal — a complete CS education — but **restructured for
learning efficiency, transfer to real systems, and modern engineering practice**.

Unlike the original OSSU curriculum, this version:
- Is **not restricted to free materials**
- Prioritizes **best-in-class books, courses, and lectures**
- Emphasizes **thinking discipline, system design, and tradeoff reasoning**
- Separates **theory, practice, and application intentionally**

This curriculum is **not interview prep** and **not framework training**.
It is a long-horizon, depth-first path intended to build the kind of understanding that:
- scales across languages and paradigms
- improves architectural judgment
- supports long-term technical leadership


## Why this repo exists

This repository serves three purposes:

1. **Personal tracking**  
   A structured, honest record of my computer science study path,
   including what I studied, why I chose it, and what it was meant to develop.

2. **Professional signal**  
   A transparent demonstration of foundational CS knowledge, learning discipline,
   and long-term technical investment.

3. **A pragmatic OSSU reinterpretation**  
   A reference for others who value OSSU’s goals but struggle with:
   - free-only constraints
   - academic pacing
   - lack of focus on engineering judgment

This is not a replacement for OSSU, nor a criticism of it.
It is a **quality-first, experience-aware reinterpretation** of the same ideals.

# Curriculum

## Curriculum Overview
> Note: Tiers represent conceptual progression, not strict sequencing.
> Some tiers intentionally overlap in practice.


- [Mathematics for Computer Science & Engineering](#mathematics-for-computer-science--engineering)
- [Tier 0 — Prerequisites](#tier-0--prerequisites)
- [Tier 1 — Core Programming & Data Modeling](#tier-1--core-programming--data-modeling)
- [Tier 2 — Programming in the Large (Paradigm Bridge)](#tier-2--programming-in-the-large-paradigm-bridge)
- [Tier 3 — Algorithms & Data Structures](#tier-3--algorithms--data-structures)
- [Tier 4 — Formal Reasoning For Engineers](#tier-4--formal-reasoning-for-engineers) 
- [Tier 5 — Computer Systems Fundamentals](#tier-5--computer-systems-fundamentals)
- [Tier 6 — Operating Systems & Concurrency](#tier-6--operating-systems--concurrency)
- [Tier 7 — Networking & Distributed Systems](#tier-7--networking--distributed-systems)
- [Tier 8 — Databases & Data Systems](#tier-8--databases--data-systems)
- [Tier 9 — Software Design & Architecture](#tier-9--software-design--architecture)
- [Tier 10 — Operating Systems in Production](#tier-10--operating-systems-in-production)
- [Tier 11 — Security & Risk](#tier-11--security--risk)
- [Tier 12 — Engineering Leadership & Judgment](#tier-12--engineering-leadership--judgment)


## Mathematics for Computer Science & Engineering

> Purpose:
> Build mathematical intuition and fluency needed for algorithms, systems,
> performance analysis, and AI/ML — without unnecessary proof burden.
>
> This math track runs **in parallel** with Core Programming and Algorithms,
> and is paced for long-term retention, not speed.

---

### Core Areas
**Topics covered**:
`Foundational Maths`
`Calculus`
`Discrete Mathematics`
`Linear Algebra`
`Probability & Statistics`

Take Math Academy Assessment or Start from Mathematical
Foundations I
> 🚧 **Under construction**
>
> This math track is intentionally staged.
> Foundational fluency comes first; discrete math, probability,
> and linear algebra will be layered in deliberately.

| Completed | Resource                                                                 | Institution / Author | Type      | Focus                                                     | Completed Assignments |
| :-------: | ------------------------------------------------------------------------ | -------------------- | --------- | --------------------------------------------------------- | :-------------------: |
| ✅        | [Mathematical Foundations I](https://mathacademy.com/courses/mathematical-foundations-i) | MathAcademy          | Platform  | Algebraic fluency, functions, core mathematical reasoning | On Platform                  |
| ⏳        | [Mathematical Foundations II](https://mathacademy.com/courses/mathematical-foundations-ii) | MathAcademy          | Platform  | Advanced algebra, functional thinking, math stamina       | On Platform                   |

---

**Study approach**:
- Follow MathAcademy’s recommended sequence
- Prioritize mastery over speed
- Allow this track to run continuously at low intensity
- Treat math as *infrastructure*, not a project

---


## Tier 0 — Prerequisites

> Purpose:
> Establish basic programming fluency required to engage meaningfully
> with Core Programming, Algorithms, and Systems topics.

**Topics Covered**  
`Basic programming`  
`Control flow`  
`Functions`  
`Basic data types`

---

| Completed | Resource                                                                 | Institution / Author | Type          | Focus                                              | Completed Assignments |
| :-------: | ------------------------------------------------------------------------ | -------------------- | ------------- | -------------------------------------------------- | :-------------------: |
| ✅        | [Python for Everybody](https://www.py4e.com/lessons)                     | Dr. Chuck (UMich)    | Book / Course | Basic programming, data handling, scripting        | n/a                   |
| ✅        | [CS50P: Introduction to Programming with Python](https://cs50.harvard.edu/python/) | Harvard              | Course        | Program structure, problem solving, Python fluency | n/a                   |

---

### Optional / Supplemental

| Completed | Resource                                                                 | Institution / Author | Type   | Focus                                                  | Completed Assignments |
| :-------: | ------------------------------------------------------------------------ | -------------------- | ------ | ------------------------------------------------------ | :-------------------: |
| ✅        | [Web Developer Bootcamp](https://www.udemy.com/course/the-web-developer-bootcamp/) | Udemy / Colt Steele  | Course | Programming fluency, JavaScript fundamentals, full-stack exposure | n/a |



## Tier 1 — Core Programming & Data Modeling
> Purpose:
> Establish disciplined reasoning about data and behavior that transfers
> directly to algorithms, systems design, and correctness-critical code.

**Topics Covered**
`Data definitions and invariants`
`Structural recursion`
`Designing functions from data`
`Error handling and total functions`
`Immutability and state modeling`
`Correctness reasoning`


| Completed | Resource                                                                 | Institution / Author      | Type          | Focus                                              | Completed Assignments |
| :-------: | ------------------------------------------------------------------------ | ------------------------- | ------------- | -------------------------------------------------- | :-------------------: |
| ⬜        | [How to Design Programs, 2e](https://htdp.org/2023-8-14/Book/index.html)  | Matthias Felleisen et al. | Book / Course | Data-driven design, structural recursion, correctness | [assignments](https://github.com/JamesMcGahn/OSSU/tree/main/core_cs/how_to_design_programs) |


**Study notes**
- Book-driven; lectures are optional and secondary  
- Exercises are selected, not exhaustive  
- Emphasis is on understanding invariants and design rationale  
- Concepts are translated mentally into modern languages when applicable


---

## Tier 2 — Programming in the Large (Paradigm Bridge)
> Applying disciplined thinking in real systems

- Mutable state and side effects
- Object-oriented design fundamentals
- Interfaces and contracts
- Composition vs inheritance
- Functional techniques in OO systems
- Managing complexity over time

---

## Tier 3 — Algorithms & Data Structures
> Mechanical sympathy and problem-solving tools

- Core data structures
- Algorithmic patterns
- Complexity intuition
- Time vs space tradeoffs

---

## Tier 4 — Formal Reasoning for Engineers
> Formal reasoning without proof obsession

- Sets, relations, functions
- Graphs, trees, DAGs
- State spaces and transitions
- Invariants and correctness
- Asymptotic thinking

---

## Tier 5 — Computer Systems Fundamentals
> What code runs on

- Processes and threads
- Memory hierarchy
- Scheduling intuition
- Concurrency models
- Synchronization primitives

---

## Tier 6 — Operating Systems & Concurrency
> Managing shared resources safely

- Process lifecycle
- Threading models
- Async vs sync
- Deadlocks and race conditions
- Resource contention

---

## Tier 7 — Networking & Distributed Systems
> Systems beyond a single machine

- Networking fundamentals
- RPC and messaging
- Partial failure
- Consistency models
- Distributed coordination (high level)

---

## Tier 8 — Databases & Data Systems
> Persistent state and correctness

- Relational model
- Transactions and isolation
- Indexing and query planning
- Schema design and evolution
- Caching strategies

---

## Tier 9 — Software Design & Architecture
> Systems that survive change

- Abstraction and modularity
- Architectural patterns
- Dependency management
- System decomposition
- Tradeoff analysis

---

## Tier 10 — Operating Systems in Production
> Operating systems in production

- Profiling and benchmarking
- Latency vs throughput
- Monitoring and alerting
- Debugging production systems
- Capacity planning

---

## Tier 11 — Security & Risk
> Defensive engineering

- Authentication vs authorization
- Secure credential handling
- Common vulnerability classes
- Threat modeling
- Dependency risk

---

## Tier 12 — Engineering Leadership & Judgment
> Senior / Staff-level operation

- Technical decision documents
- Making tradeoffs explicit
- Mentorship
- Cross-team influence
- Long-term technical direction
