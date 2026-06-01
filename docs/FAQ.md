# FAQ

## Is Qruba a quantum circuit builder?

Qruba is not primarily a circuit builder. It is a visual semantic computation platform powered by QDSV.

Circuits can appear when a backend requires them, but users do not need to start by writing circuits.

## Does Qruba replace Qiskit, QPanda, Classiq or other quantum tools?

No. Qruba addresses a different layer: problem formulation, semantic execution, workflow construction and evidence.

Other tools can still be useful for circuit-level work, hardware access or algorithm development.

## What is QDSV?

QDSV is the semantic model behind Qruba, QIntent and QDSV Bridge.

It focuses on intention, predicates, state spaces, operations, ranking, distribution and evidence.

## What is QIntent?

QIntent is the declarative language surface for QDSV.

It lets technical users express problems in a controlled language without installing the private QDSV runtime.

Repository:

[https://github.com/qdsvquantum-afk/qintent](https://github.com/qdsvquantum-afk/qintent)

## What is QDSV Bridge?

QDSV Bridge is a separate developer-preview SDK and API for compiling supported semantic problem families into IR, oracle specs or circuit blueprints.

Repository:

[https://github.com/qdsvquantum-afk/qdsv-bridge](https://github.com/qdsvquantum-afk/qdsv-bridge)

## Does Qruba guarantee quantum advantage?

No. Qruba does not claim general quantum advantage.

Its value is in formulation, semantic representation, execution routing, evidence, auditability and controlled experimentation across backends.

## Can Qruba run on real IBM quantum hardware?

Yes, when IBM access is configured and the deployment/license allows it.

Real hardware results should be interpreted with reliability reports, not only with final metrics.

## Does this repository contain the Qruba source code?

No. This repository is a public product and documentation repository.

The private platform code, QDSV runtime and infrastructure components are not included.
