# QIntent Hardware Optimization Profiles

Qruba exposes the same per-job hardware optimization policy as the QIntent
Python SDK. The QIntent node sends the selected value to the shared QDSV
hardware worker; it does not create a second compiler or execution path.

## Available profiles

- baseline: default for end-user runs. Performs the required semantic,
  reversible, target-compatibility, and readiness checks for one eligible
  logical/physical candidate, then selects it directly without alternative
  target-profile materialization.
- balanced: evaluates a bounded set of physical candidates and applies the
  existing Pareto/resource selection.
- advanced: keeps the largest configured candidate and replay budgets for
  deliberate optimization campaigns.

Choose the profile in the QIntent node under Execution settings. Baseline is
recommended for ordinary QPU submissions and constrained Docker workers.
Balanced or Advanced can use more CPU time and memory before the provider job
is submitted.

## Asynchronous job behavior

The node submits a persisted hardware job and displays its state and evidence.
Normal status reads use the stored job state. A live IBM provider refresh is
opt-in, so the UI does not make every poll wait on IBM.

The job evidence records the normalized profile, effective limits, selection
method, selected candidate, and whether IBM submission occurred.

## Compatibility

- Existing v2 manual-operation nodes remain unchanged.
- Simulator and local QIntent execution remain available.
- ScoreModel and QIntent keep separate public ingress contracts.
- Both routes converge on the shared hardware worker and evidence model.
- Selecting baseline does not disable validation or authorize promotion.
