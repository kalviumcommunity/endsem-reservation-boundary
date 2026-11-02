# End Semester Examination, Set 2, Question 2
# Repair Exact-Capacity Reservations

**Total: 30 marks | Submit one PDF**

## Problem

A resource reservation program wrongly rejects a request equal to remaining capacity. Repair this boundary without allowing oversized requests or changing capacity after rejection.

Starter: https://github.com/kalviumcommunity/endsem-reservation-boundary

Use your assigned repository. Run Python files from project root with your available Python 3 launcher. Standard library only. Inspect README.md for entry point and checks. Editable files: reservation.py, regression_check.py and RUNBOOK.md. Keep app.py, checks.py and README.md unchanged. Preserve all non-placeholder assertions.

## Requirements

reserve(capacity, requested) returns (accepted, remaining). For supplied non-negative integer inputs, requests less than or equal to capacity must succeed and subtract requested units. Requests above capacity must fail and return original capacity unchanged. Zero-unit requests succeed, including at zero capacity. No UI, database or additional validation is required. Booleans and negative/non-integer values are outside assessed input domain.

## Task 1: Reproduce and trace

Show initial Git status and project files. Run app.py and compare expected versus observed results for below-capacity, exact-capacity and above-capacity cases. Locate the caller, reservation decision and capacity update using code search or editor navigation. Explain the input-to-result path with source file names.

Evidence: status/files, actual run, three-case comparison, located decision/update and short trace.

## Task 2: Expose the missing boundary check

Create a repair branch. Run checks.py unchanged. Complete only the two expected-result placeholders in regression_check.py using the requirements. Execute regression against unchanged reservation.py and capture exact-capacity failure before repair. Show implementation has not yet changed and explain why old checks passing misses this boundary.

Evidence: branch, unchanged old check result, completed regression assertions, actual pre-fix failure, unchanged implementation and explanation.

## Task 3: Repair and validate

Make a focused repair in reservation.py without hard-coded sample results. Rerun app.py, checks.py and complete regression. Verify below, exact, above, zero request, zero capacity and rejected-request capacity preservation using supplied assertions. Remove temporary diagnostics and keep all expectations unchanged. Explain cause and correction.

Evidence: focused diff, corrected three-case run, full successful checks and explanation.

## Task 4: Document and propose

Complete RUNBOOK.md with reproduction, cause, correction, commands actually run, observed results and one testing limit. Review staged changes, make a meaningful commit and push branch. Open PR into main in the same repository, with useful title and description covering problem, cause, change and actual validation. Capture open state/direction and final clean local status. Leave PR open for review.

Evidence: runbook, staged diff, commit/push, open PR/title/description/direction and clean state. No merge required.

## Submission

Submit one PDF containing solutions for all four tasks. Organise it into Task 1 to Task 4. Include the screenshots requested in each task, with a one- or two-sentence label explaining the result and answering any requested short question. Multiple readable screenshots per task are allowed. Do not include credentials.

