---
name: No orphaned private fields
description: Every private field in a UML class must have a defined entry point -- constructor parameter or mutator method -- no exceptions
type: feedback
---

A private field with a getter but no constructor parameter and no setter is a dead end. It can never be set, which means it can never be read meaningfully. This is a diagram bug, not a style choice.

**Why:** The user identified that the original diagram had private fields across multiple classes with no way to initialize them. Getters alone are not a complete interface.

**How to apply:** When reviewing or creating any class diagram, verify that every private field has at least one write path (constructor or mutator). Flag any field that lacks one as an error before publishing.
