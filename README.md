# Qruba

[![Status](https://img.shields.io/badge/status-developer%20preview-0ea5e9.svg)](#public-project-scope)
[![Powered by](https://img.shields.io/badge/powered%20by-QDSV-14b8a6.svg)](https://qdsv.cloud/)
[![Platform](https://img.shields.io/badge/platform-cloud%20%7C%20private%20docker-111827.svg)](#access)

Documentation site: https://qdsvquantum-afk.github.io/qruba/

**Qruba** is the visual semantic computation platform powered by **QDSV - Quantum Declarative Semantic Value**.

It helps teams explore quantum-ready computation from prepared data, problem intention, predicates, rankings, reliability policies and evidence without forcing users to start by designing quantum circuits.

Qruba is designed for practical exploration by business analysts, data teams, researchers, software engineers, innovation groups and technical decision makers.

![Qruba dashboard](./assets/dashboard.png)

## 5 Minute Product View

Qruba lets a user build an auditable workflow:

```text
prepared data
-> candidates
-> semantic intention
-> predicates / state spaces
-> execution route
-> evidence
```

The user works with visual nodes. QDSV decides how the problem can be represented and executed across logical, simulated, statevector or quantum-capable routes.

Circuits remain valid, but in QDSV they are a possible materialization when a backend requires them. They are not the required starting point for the user.

## What Qruba Is

- A visual workflow platform for semantic computation.
- A practical interface for trying QDSV without starting from low-level quantum programming.
- A way to run prepared data through predicates, decision/ranking models, QIntent, combinatorial search, traces and reliability reports.
- A demo and pilot surface for organizations exploring quantum-ready workflows.

## What Qruba Is Not

- It is not a public release of the private QDSV Runtime.
- It is not a claim of guaranteed quantum advantage.
- It is not a replacement for expert quantum software stacks.
- It is not a production cryptography or production sensing certification platform.
- It is not a repository containing Qruba source code or private backend orchestration.

## Why Qruba Matters

Most quantum tools ask users to think in terms of gates, circuits, encodings, ansatz choices or backend-specific programs.

Qruba starts from the problem:

- What candidates exist?
- What condition defines a valid solution?
- What should be ranked or selected?
- What evidence should be accepted?
- Which route can execute the problem?

This makes Qruba useful as a practical bridge between business or scientific problems and logical, simulated, statevector or quantum-capable execution.

## Main Capabilities

- Visual workflow builder for semantic computation.
- Prepared-data ingestion through CSV or JSON.
- Predicate and oracle construction.
- Decision and ranking workflows over prepared values.
- QIntent execution inside visual flows.
- Combinatorial search across candidate spaces.
- Controlled mathematical and semantic operations.
- Semantic AI exploration for selection, routing, sampling and model-building decisions.
- Sensing evidence experiments over sensor or simulated sensor readings.
- Experimental Crypto QDSV workflows.
- Noise, reliability and mitigation policies.
- Output export and trace / verification reports.
- Cloud and private Docker deployment options.

## Core Nodes

| Node | Purpose |
|---|---|
| Dataset Input | Load prepared CSV/JSON data into the workflow. |
| Predicate / Oracle | Convert rules over prepared rows into executable predicates and oracle-ready structures. |
| Semantic Operation | Apply controlled mathematical or semantic operations to prepared values. |
| Decision Model | Build auditable selection, scoring and ranking workflows over prepared values. |
| Combinatorial Search | Explore bounded combinations across candidate spaces. |
| QIntent | Write declarative QDSV-native instructions for flexible problem expression. |
| QDSV Console | Run commands, compile QIntent, inspect jobs, export results and review evidence. |
| Output | Review and export enriched results. |
| Traces / Verification | Inspect execution route, backend, evidence and reliability reports. |

## Experimental Nodes

| Node | Purpose |
|---|---|
| Semantic AI Explorer | Explore AI lifecycle decisions such as configuration search, routing, sampling, boundary evaluation and scientific ranking. |
| Crypto QDSV | Experimental semantic-quantum cryptography workflows such as challenge-response and commitments. Not production cryptography. |
| Sensing Evidence QDSV | Interpret sensor or simulated sensor readings as events, rankings, confidence and evidence. |

Experimental nodes are meant for research, pilots and controlled validation. They should not be presented as production security, production sensing certification or guaranteed quantum advantage.

## Decision, Hardware And Reliability Layers

Qruba separates semantic decisions from hardware evidence.

This matters because a workflow can produce a strong semantic result while real hardware may return noisy or incomplete physical evidence. Qruba keeps these layers visible instead of hiding them inside one metric.

Typical enriched outputs can include:

- semantic selection;
- hardware-reconstructed selection when available;
- reliability status;
- final recommended decision;
- execution route;
- backend;
- probabilities, counts or solution mass when supported;
- trace and evidence summaries.

This separation helps users avoid confusing semantic accuracy with hardware-confirmed reliability.

## Case Study Evidence

The public documentation includes an EEG signal classification case study showing how Qruba/QDSV can preserve prepared signal structure and compare semantic execution routes against circuit-first baselines.

Read the case study:

- [EEG signal classification case study](./docs/CASE_STUDY_EEG_CLASSIFICATION.md)

## Access

- Qruba Cloud: https://cloud.qruba.site/
- Private Docker access: https://qruba.site/ when the private node is available
- QDSV model site: https://qdsv.cloud/
- QIntent SDK: https://github.com/qdsvquantum-afk/qintent
- QDSV Bridge SDK: https://github.com/qdsvquantum-afk/qdsv-bridge

## Learn More

- [Getting started](./docs/GETTING_STARTED.md)
- [Node overview](./docs/NODES.md)
- [Access, privacy and deployment](./docs/ACCESS_PRIVACY.md)
- [EEG signal classification case study](./docs/CASE_STUDY_EEG_CLASSIFICATION.md)
- [FAQ](./docs/FAQ.md)
- [Roadmap](ROADMAP.md)

## Public Project Scope

This repository is a public product page and documentation space for Qruba.

It does not include:

- private QDSV runtime;
- Qruba platform source code;
- CAP internals;
- backend orchestration;
- lowering logic;
- QuEST/Aer/IBM adapters;
- infrastructure secrets;
- production configuration;
- proprietary execution components.

## Contact

For pilots, research collaboration, technical integration or investment conversations, use the contact form on:

https://qdsv.cloud/
