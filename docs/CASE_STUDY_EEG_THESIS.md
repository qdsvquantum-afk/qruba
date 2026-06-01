# Case Study: EEG Thesis Comparison

This note summarizes an early Qruba/QDSV validation exercise inspired by the thesis:

**Classical and quantum machine learning for the classification of ictal and interictal periods in EEG signals.**

The goal was not to claim quantum advantage. The goal was to understand why a circuit-based quantum workflow performed far below classical baselines, and how Qruba/QDSV can approach the same kind of problem from a different starting point: prepared signals, semantic intention, ranking, evidence and backend-aware execution.

## 1. Problem Context

The reference task is binary EEG classification:

```text
interictal
vs
ictal
```

The important methodological question was:

> Did the classical model outperform the circuit-based quantum model only because it had access to more variables, or because the circuit route transformed the data in a way that reduced useful information?

The initial evidence suggests that the second explanation is important.

## 2. Datasets Reviewed

### Bonn

Cleaned dataset structure:

- 300 records for binary classification.
- 200 interictal samples.
- 100 ictal samples.
- 4097 samples per signal.

Binary mapping:

```text
N + F -> interictal = 0
S     -> ictal      = 1
```

### Delhi

Cleaned dataset structure:

- 100 records for binary classification.
- 50 interictal samples.
- 50 ictal samples.
- 1024 samples per signal.

Binary mapping:

```text
interictal = 0
ictal      = 1
preictal excluded
```

## 3. Prepared Features

For each EEG signal, 29 classical features were extracted:

- `activity`
- `mobility`
- `complexity`
- `energy`
- `shannon_entropy`
- `std`
- `skewness`
- `kurtosis`
- `zero_crossings`
- wavelet features over `dwt_cA3`, `dwt_cD3`, `dwt_cD2`, `dwt_cD1`

The generated feature tables had no `NaN` or `Inf` values.

For Qruba, the next step was to convert these into prepared, oriented signals on a common scale, rather than forcing them immediately into a fixed circuit encoding.

## 4. Classical Baseline

Classical baselines included:

- Decision Tree.
- Random Forest.
- ALL features.
- PCA reductions.
- SVD reductions.
- NMF reductions.
- UMAP reductions.
- Repeated 70/30 validation.

Best observed Bonn result:

```text
RandomForest + NMF 10
accuracy          ~= 0.9815
precision ictal   ~= 0.9780
recall ictal      ~= 0.9667
F1 ictal          ~= 0.9718
```

Best observed Delhi result:

```text
DecisionTree / RandomForest + ALL 29
accuracy          = 1.0000
precision ictal   = 1.0000
recall ictal      = 1.0000
F1 ictal          = 1.0000
```

## 5. Circuit-Based Quantum Baseline

The quantum baseline followed a VQC-style route:

```text
features
-> dimensionality reduction
-> angle encoding
-> RealAmplitudes ansatz
-> parity-style measurement
-> optimizer / threshold
```

Best observed focused Bonn result:

```text
BONN + NMF 7 + angle_ry
accuracy          ~= 0.6267
precision ictal   ~= 0.5404
recall ictal      ~= 0.8533
F1 ictal          ~= 0.6344
```

Best observed focused Delhi result:

```text
DELHI + PCA 7 or SVD 7 + angle_ry
accuracy          ~= 0.6200
precision ictal   ~= 0.6074
recall ictal      ~= 0.8400
F1 ictal          ~= 0.6878
```

The circuit model improved recall but produced lower precision and accuracy. It tended to mark many cases as ictal.

## 6. Main Methodological Reading

The hypothesis that the classical model only won because it used more variables became weaker after testing reductions with comparable feature counts.

The stronger interpretation is:

```text
The loss is not only in the amount of information.
The loss is also in the representation route.
```

The circuit workflow required the data to pass through:

- dimensionality reduction;
- angular encoding;
- fixed ansatz structure;
- fixed measurement interpretation;
- optimizer-dependent thresholding.

This can make the problem adapt to the circuit, instead of deriving the execution representation from the problem.

## 7. Qruba / QDSV Approach

Qruba should not initially claim that it beats RandomForest.

The cleaner objective is to demonstrate that Qruba/QDSV can:

- preserve prepared EEG signals;
- express the classification as semantic intention;
- build a traceable selection/ranking;
- produce evidence and reliability reports;
- compare QuEST, simulator and real hardware routes without hiding representation loss.

The Qruba formulation is:

```text
prepared EEG signals
-> semantic intention / predicate / ranking
-> evidence
-> backend route
```

Instead of:

```text
data
-> forced reduction
-> fixed encoding
-> fixed ansatz
-> measurement
```

## 8. Prepared Qruba Inputs

Generated Qruba-ready files:

- `bonn_qruba_features.csv`
- `delhi_qruba_features.csv`
- class separation reports
- feature quality reports
- signal parameter reports
- score preview validation summaries

Recommended BONN inputs for the Decision Model:

- `dwt_cD3_std_score`
- `std_score`
- `activity_score`
- `energy_score`
- `dwt_cD2_std_score`
- `complexity_score`

Recommended DELHI inputs for the Decision Model:

- `activity_score`
- `energy_score`
- `std_score`
- `dwt_cA3_energy_score`
- `dwt_cD3_energy_score`
- `dwt_cD2_energy_score`

Columns not used as decision inputs:

- `label`
- `clinical_class`
- preview prediction columns
- train-only threshold columns

These labels remain useful for validation, not for building the decision.

## 9. Initial Qruba Result on BONN

Using Qruba with QuEST on the BONN prepared features produced:

```text
full dataset:
accuracy          = 0.9800
precision ictal   = 0.9700
recall ictal      = 0.9700
F1 ictal          = 0.9700

test subset:
accuracy          = 0.9556
precision ictal   = 0.9643
recall ictal      = 0.9000
F1 ictal          = 0.9310
```

This result should be interpreted carefully:

- it validates the prepared-signal formulation;
- it shows Qruba can express the problem effectively as semantic selection/ranking;
- it does not prove general quantum advantage;
- it does not automatically prove that real quantum hardware reproduced the same decision.

## 10. IBM Hardware Interpretation

In a real IBM run, Qruba confirmed hardware execution, but the physical evidence was noisy:

```text
backend: IBM real hardware
shots: 1024
execution_mode: quantum_probabilistic
amplification_applied: true
solution_mass: low compared with QuEST/Aer
raw_confidence: low
normalized_entropy: high
```

This means:

```text
IBM real execution occurred,
but the hardware distribution was not yet strong enough to claim reliable row-by-row physical reproduction of the semantic selection.
```

Qruba now separates:

- semantic selection;
- hardware-reconstructed selection;
- reliability status;
- final decision.

This prevents a high semantic metric from being misread as hardware-confirmed accuracy.

## 11. Why This Case Matters

This case illustrates Qruba's value:

```text
Qruba does not force the user to adapt the problem to a fixed circuit first.
It lets the problem be formulated semantically, then reports how execution and evidence behave across backends.
```

The important contribution is not simply a higher metric. The important contribution is a more transparent route:

```text
problem formulation
-> prepared signal preservation
-> semantic selection
-> backend execution
-> reliability-aware evidence
```

That is the level where Qruba/QDSV differs from a circuit-first workflow.

## 12. Status

This is an early validation case.

Current status:

- useful for demonstration and research discussion;
- useful for comparing semantic formulation vs circuit-first formulation;
- not a production medical diagnostic claim;
- not a claim of quantum advantage;
- not a replacement for clinical validation.

The next step is to extend the comparison with controlled exports, QDSV Bridge artifacts and stronger hardware reliability analysis.
