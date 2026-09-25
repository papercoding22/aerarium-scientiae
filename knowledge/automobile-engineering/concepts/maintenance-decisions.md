---
status: draft
confidence: needs-review
domain: automobile-engineering
---

# Maintenance Decisions

## Table Of Contents

- [Concept](#concept)
- [Background And Context](#background-and-context)
- [Foundation](#foundation)
- [First Principles](#first-principles)
- [How It Works](#how-it-works)
- [Concrete Example](#concrete-example)
- [Mental Model And Summary](#mental-model-and-summary)
- [How To Apply](#how-to-apply)
- [Practice Question](#practice-question)
- [Sources](#sources)
- [Related Notes](#related-notes)

## Concept

What does a car need, and what evidence supports that decision?

## Background And Context

Every component has a job. Tyres provide grip, brakes slow the car, and engine oil helps protect moving surfaces. Each can do its job properly only while certain conditions remain acceptable.

Those conditions change gradually. An owner needs a way to decide when to inspect something, carry out routine care, or correct a fault.

## Foundation

Three common ways that a component's condition changes are:

| Process | What changes | Example |
| --- | --- | --- |
| Wear | Contact gradually removes material | Brake-pad material becomes thinner through use |
| Aging | Time and exposure change a material's properties | Rubber becomes harder or cracked |
| Contamination | Unwanted material builds up | Dirt collects in a filter |

A car may still seem to work normally while a component approaches a service limit. For example, brake pads may still provide normal-feeling braking as their remaining thickness approaches the applicable wear limit. Measuring their condition reveals information that driving alone may not show.

## First Principles

A component must meet certain requirements to perform its job. A maintenance decision connects those requirements with evidence about its condition and any scheduled work that is due.

The basic reasoning is: **compare the component's condition and service status with its requirements, then choose an action.**

Use requirements for the correct vehicle and component. Low mileage or the absence of noticeable problems does not, by itself, establish whether maintenance is due.

## How It Works

Four useful actions are:

| Action | Purpose | Example |
| --- | --- | --- |
| Inspect | Find out the condition | Measure brake-pad thickness and compare it with the applicable limit |
| Service | Carry out planned care to keep the car working properly | Change engine oil and its filter when required by the applicable service guidance |
| Repair | Restore correct operation after identifying a fault | Repair damaged wiring confirmed to be causing an electrical fault |
| Replace | Fit another component because the existing one needs changing | Fit new brake pads when their condition requires replacement |

These actions overlap. Replacement can be part of servicing or repair. Replacing an oil filter during scheduled servicing and replacing a failed component are different reasons for the same physical action.

Connect the action to the reason it needs attention:

- **Time or mileage:** the applicable schedule says a task is due.
- **Measured condition:** inspection shows that a limit has been reached.
- **A symptom:** something changes, so it needs investigation.

A symptom is an observation, not a confirmed cause. Diagnose the cause before choosing a repair.

## Concrete Example

Suppose a tyre repeatedly loses pressure. The pressure loss is the symptom. Possible causes include a puncture, a leaking valve, or another leak.

Inspection and diagnosis identify where the air is escaping. The appropriate action then depends on the finding: a valve fault and tyre damage may need different fixes. Whether a tyre can be repaired or needs replacement depends on the damage and applicable repair criteria.

The decision follows the evidence instead of assuming that every pressure loss requires a new tyre. After the work, check that the problem has been resolved.

## Mental Model And Summary

**Notice or check → compare with the requirement → choose an action → confirm the result.**

Every recommended action should have a clear reason: a scheduled requirement, an inspection finding, or a diagnosed fault.

## How To Apply

When discussing a workshop recommendation, ask:

- What makes this action necessary now: time, mileage, a measurement, or a fault finding?
- Which requirement or specification supports the recommendation?
- How will the result be checked after the work?

Use the vehicle's service information and inspection findings to answer these questions. Exact limits, intervals, and repair procedures still need vehicle-specific sources.

## Practice Question

OPEN QUESTION: Suppose your BMW's wipers begin leaving streaks across the windscreen. Someone immediately suggests new wiper blades. What would you check before deciding whether to replace them?

This question is still open from the learning session.

## Sources

- Based on the first lesson in the car-service and maintenance learning session.
- [Service and maintenance terminology](../terminology/design-testing-manufacturing-safety-and-service.md) — supporting vocabulary for symptoms, diagnosis, wear, and maintenance.

## Related Notes

- [Car Service And Maintenance Learning Path](../applications/car-service-and-maintenance-learning-path.md) — Stage 1: understand maintenance decisions.
