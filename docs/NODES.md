# Qruba Node Overview

Qruba workflows are built with visual nodes. Each node exposes a controlled capability of the QDSV platform.

## Dataset Input

Loads prepared CSV or JSON data.

Use it when:

- the dataset is already cleaned;
- each row is a candidate;
- fields are ready to be evaluated;
- `candidate_index` or another stable identifier exists.

## Predicate / Oracle

Creates a predicate from configured conditions.

Use it when:

- you need a clear rule;
- you want to mark candidates that satisfy a condition;
- you want to inspect how a rule becomes oracle-ready evidence.

## Semantic Operation

Applies controlled operations to prepared values.

Examples include arithmetic, comparison, tolerance, safe division, null handling, similarity and vector similarity where supported.

Use it to create an intermediate value that can later feed a Decision Model, predicate or QIntent workflow.

## Decision Model

Combines prepared values into an auditable decision, selection or ranking.

Use it when:

- several prepared criteria matter;
- the output should be easy to audit;
- candidates need to be selected or ranked;
- the workflow should preserve decision and evidence layers.

## Combinatorial Search

Explores bounded combinations across candidate spaces.

Use it with controlled datasets and limits. Combinatorial spaces can grow quickly.

## QIntent

QIntent is the declarative language surface for QDSV.

Use it when visual forms are not enough or when a technical user wants to write a compact intention such as:

```text
find_rows("candidate_index").where("score", ">=", 850).rank_by("score").top_k(10)
```

QIntent does not run free Python. It is a controlled QDSV language.

## QDSV Console

Operational console for technical users.

Use it to:

- run quick commands;
- compile QIntent;
- inspect jobs;
- query evidence;
- export recent results;
- review backend behavior.

## Output

Displays and exports final enriched results.

## Traces / Verification

Shows execution route, evidence and verification information.

Use it when:

- validating a run;
- comparing simulator and hardware behavior;
- checking reliability;
- preparing evidence for review.

## Experimental Nodes

### Semantic AI Explorer

Explores semantic decisions across AI workflows:

- configuration search;
- candidate sampling;
- decision boundary review;
- action routing;
- representation interactions;
- QML feature preparation;
- scientific candidate ranking.

### Crypto QDSV

Experimental workflows for semantic-quantum cryptography research.

Not for production cryptography.

### Sensing Evidence QDSV

Interprets sensor or simulated sensor outputs as states, events, confidence and evidence.

It does not replace sensor hardware or laboratory calibration.
