# Getting Started with Qruba

Qruba is built for users who want to formulate, execute and audit semantic computation workflows without starting from circuits.

## 1. Prepare Your Data

Qruba expects prepared data.

Recommended dataset characteristics:

- one row per candidate;
- a stable candidate identifier, usually `candidate_index`;
- numeric or boolean prepared values;
- clear scales, for example 0 to 1000;
- validation labels kept separate from decision inputs;
- no empty critical fields;
- no raw unstructured text as the main decision input.

Qruba does not replace normal data preparation, EDA, cleaning or domain modeling. It amplifies well-formulated problems.

## 2. Build a Workflow

Typical workflow:

```text
Dataset Input
-> Predicate / Oracle or Decision Model or QIntent
-> Output
-> Traces / Verification
```

For advanced use:

```text
Dataset Input
-> Semantic Operation
-> Decision Model
-> Output
-> Traces / Verification
```

or:

```text
Dataset Input
-> QIntent
-> Output
-> Traces / Verification
```

## 3. Choose an Execution Route

Qruba can work with different execution routes depending on deployment and license:

- logical or semantic validation;
- QuEST/statevector route;
- Aer-style simulation routes;
- IBM hardware routes when configured;
- private Docker routes for controlled environments.

The user does not need to start by writing circuits. QDSV decides the representation and route according to the problem and backend.

## 4. Review Results

After execution, review:

- selected candidates;
- ranking;
- generated columns;
- backend used;
- execution path;
- reliability status;
- output export;
- trace and evidence report.

For hardware workflows, avoid reading a single accuracy metric as full physical validation. Qruba separates semantic decisions from hardware evidence and reliability.

## 5. Export and Audit

Use the Output node to export enriched rows.

Use Traces / Verification to inspect:

- execution route;
- backend;
- evidence;
- reliability summary;
- decision layers;
- generated artifacts when available.
