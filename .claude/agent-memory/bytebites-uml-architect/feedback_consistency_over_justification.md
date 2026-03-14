---
name: Consistency over per-class justification
description: When applying a design rule (e.g., constructors, setters, immutability), apply it uniformly across ALL classes and justify deviations explicitly from spec language -- never leave some classes unexamined
type: feedback
---

Every design decision in a diagram must be applied consistently across all classes, not selectively. If one class gets constructors, all classes must be examined for constructors. If one class is called "immutable," every other class must be explicitly evaluated against the same standard.

**Why:** The user caught an inconsistency where FoodItem was declared immutable (no setters) but Customer had the same problem (private name, no setter, no constructor) with no justification given. Selective reasoning creates hidden incoherence.

**How to apply:** After making any structural decision for one class, immediately audit all other classes against the same rule. Use spec language (verbs like "manage" vs "track") to justify per-class differences -- never leave a gap unexplained.
