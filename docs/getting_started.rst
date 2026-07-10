Getting Started
===============

1. Prepare your data
--------------------

Qruba expects prepared data:

* one row per candidate;
* a stable candidate identifier, usually ``candidate_index``;
* numeric or boolean prepared values;
* clear scales, for example 0 to 1000;
* validation labels kept separate from decision inputs;
* no empty critical fields.

2. Build a workflow
-------------------

Typical workflow:

.. code-block:: text

   Dataset Input
   -> Predicate / Oracle or Decision Model or QIntent
   -> Output
   -> Traces / Verification

3. Choose an execution route
----------------------------

Qruba can work with different execution routes depending on deployment and
license:

* logical or semantic validation;
* QuEST/statevector route;
* Aer-style simulation routes;
* IBM hardware routes when configured;
* private Docker routes for controlled environments.

4. Review results
-----------------

After execution, review selected candidates, rankings, backend, execution
path, reliability status, exported output, traces and evidence reports.

For hardware workflows, avoid reading a single accuracy metric as full
physical validation. Qruba separates semantic decisions from hardware evidence
and reliability.
