# [Short title of solved problem and applied decision]

* Status: [draft | proposed | rejected | accepted | deprecated | superseded by [ADR-0005](0005-xxx.md)]
* Deciders: [List of decision makers]
* Date: [YYYY-MM-DD]

Technical Story: [Issue / Jira Ticket link or description]

## Context and Problem Statement

[Describe the context and problem that requires a decision. What forces are at play?]

## Decision Drivers

* [Driver 1, e.g., low-latency requirements]
* [Driver 2, e.g., team familiarity with tech stack]
* [Driver 3, e.g., operational complexity]

## Considered Options

* [Option 1, e.g., Event-driven architecture with Kafka]
* [Option 2, e.g., RESTful polling]
* [Option 3, e.g., gRPC streaming]

## Decision Outcome

Chosen option: "[Option 1]", because [justification, citing drivers].

### Positive Consequences

* [Consequence 1, e.g., Decouples producers and consumers]
* [Consequence 2, e.g., Replayability of messages]

### Negative Consequences

* [Consequence 1, e.g., Requires managing Kafka cluster or cloud broker]
* [Consequence 2, e.g., Eventual consistency handling required in UI]

## Pros and Cons of the Options

### [Option 1]

* Good, because [argument a]
* Bad, because [argument b]

### [Option 2]

* Good, because [argument a]
* Bad, because [argument b]
