# Case Study: EEG Signal Classification

This case study presents an early Qruba/QDSV workflow for binary EEG signal classification:

```text
interictal
vs
ictal
```

The goal is not to claim quantum advantage or make a medical diagnostic claim. The goal is to show how Qruba can formulate a signal-classification problem as prepared signals, semantic intention, ranking, evidence and backend-aware execution, without forcing the user to start from a fixed circuit.

## 1. Case Objective

The practical question was:

> Can Qruba preserve relevant EEG signals and express the classification as a traceable semantic decision, while also showing how different execution routes behave?

This matters because circuit-first workflows often require the data to be reduced, encoded and adapted to a specific ansatz before execution. Qruba starts earlier in the modeling chain:

```text
prepared signals
-> semantic intention / predicate / ranking
-> evidence
-> backend route
```

## 2. Dataset Structure

### Bonn

Prepared binary dataset:

- 300 records.
- 200 interictal samples.
- 100 ictal samples.
- 4097 samples per signal.

Binary mapping:

```text
N + F -> interictal = 0
S     -> ictal      = 1
```

### Delhi

Prepared binary dataset:

- 100 records.
- 50 interictal samples.
- 50 ictal samples.
- 1024 samples per signal.

Binary mapping:

```text
interictal = 0
ictal      = 1
preictal excluded
```

## 3. Prepared Signals

For each EEG signal, 29 numerical features were extracted:

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

For Qruba, these values were converted into prepared, oriented signals on a common scale. Higher values represent stronger evidence for the target decision, which lets the Decision Model evaluate the case as a semantic ranking/selection problem instead of as a fixed circuit design problem.

Generated Qruba-ready files:

- `bonn_qruba_features.csv`
- `delhi_qruba_features.csv`
- class separation reports
- feature quality reports
- signal parameter reports
- score preview validation summaries

## 4. Qruba Configuration

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

## 5. Initial Qruba Result on BONN

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

## 6. Benchmark Context

To understand the behavior of this case, two reference baselines were compared.

### Classical Baseline

Classical baselines included Decision Tree, Random Forest and multiple feature reductions such as PCA, SVD, NMF and UMAP.

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

### Circuit-First Quantum Baseline

A VQC-style circuit baseline followed this route:

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

The circuit baseline improved recall but produced lower precision and accuracy. It tended to mark many cases as ictal.

## 7. Methodological Reading

The comparison suggests that the challenge is not only the amount of information available to the model. The representation route also matters.

The circuit-first workflow required the data to pass through:

- dimensionality reduction;
- angular encoding;
- fixed ansatz structure;
- fixed measurement interpretation;
- optimizer-dependent thresholding.

This can make the problem adapt to the circuit, instead of deriving the execution representation from the problem.

Qruba's route is different:

```text
problem formulation
-> prepared signal preservation
-> semantic selection
-> backend execution
-> reliability-aware evidence
```

## 8. IBM Hardware Interpretation

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

Qruba separates:

- semantic selection;
- hardware-reconstructed selection;
- reliability status;
- final decision.

This prevents a high semantic metric from being misread as hardware-confirmed accuracy.

## 9. Why This Case Matters for Qruba

This case illustrates Qruba's value:

```text
Qruba does not force the user to adapt the problem to a fixed circuit first.
It lets the problem be formulated semantically, then reports how execution and evidence behave across backends.
```

The important contribution is not simply a higher metric. The important contribution is a more transparent route from problem formulation to evidence.

## 10. Status

This is an early validation case.

Current status:

- useful for demonstration and research discussion;
- useful for comparing semantic formulation vs circuit-first formulation;
- not a production medical diagnostic claim;
- not a claim of quantum advantage;
- not a replacement for clinical validation.

The next step is to extend the comparison with controlled exports, QDSV Bridge artifacts and stronger hardware reliability analysis.
