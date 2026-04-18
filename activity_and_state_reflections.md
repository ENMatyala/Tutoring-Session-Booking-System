# Reflection: Challenges in Activity and Object State Modeling

---

## 1. Choosing Granularity for States and Actions

One of the main challenges during modeling was determining the appropriate level of detail for both state diagrams and activity workflows. There was a constant need to balance clarity with completeness.

For example, in the **Booking state diagram**, adding too many intermediate states (such as “Awaiting Confirmation Email”) made the diagram unnecessarily complex. However, removing important states such as “Expired” would omit critical system behavior related to timeouts and payment handling.

Similarly, in activity diagrams, including every minor system step (e.g., logging actions or UI rendering) cluttered workflows and reduced readability.

### Resolution

The final approach focused on:

* Including only **states and actions that directly support functional requirements**
* Removing redundant or low-value steps
* Ensuring diagrams remain **readable and meaningful to stakeholders**

### Lesson Learned

Granularity should be **driven by system functionality and stakeholder value**, not by technical completeness alone.

---

## 2. Aligning Diagrams with Agile User Stories

Another challenge was aligning high-level **user stories** with detailed system workflows.

For example:

* User Story: *“As a student, I want to book a tutor session so that I can receive help.”*

This story does not explicitly mention:

* Availability checks
* Payment validation
* Notification handling

However, these steps are essential for fulfilling:

* FR2 (Booking System)
* FR6 (Payment)
* FR7 (Notifications)

### Resolution

Activity diagrams were expanded to include:

* System validation steps (e.g., “Check availability”)
* Parallel processes (e.g., sending confirmation + updating records)
* Implicit actions required by system logic

### Lesson Learned

User stories provide a **high-level view**, while diagrams expose:

* Hidden system steps
* Dependencies between actions
* Required validations

---

## 3. State Diagrams vs. Activity Diagrams

### Comparison

| Aspect      | State Diagrams                            | Activity Diagrams                               |
| ----------- | ----------------------------------------- | ----------------------------------------------- |
| Purpose     | Model object lifecycle                    | Model workflow processes                        |
| Focus       | *What states an object can be in*         | *How tasks are performed*                       |
| Perspective | Object-centered                           | Process-centered                                |
| Example     | Booking transitions (Pending → Confirmed) | Booking workflow (Select tutor → Pay → Confirm) |

---

### Complementary Roles

* **State diagrams** define system constraints:

  * Example: A booking cannot be completed unless it is in a *Confirmed* state

* **Activity diagrams** define workflows:

  * Example: Steps a student follows to complete a booking

---

### Integration Example

* The **Booking state diagram** ensures that a booking only moves to *Confirmed* after payment
* The **Activity diagram** shows how the payment process leads to that transition

---

## 4. Challenges with Parallel Actions and Swimlanes

Implementing **swimlanes** and **parallel actions** introduced additional complexity.

### Example:

In the booking workflow:

* After creating a booking, the system must:

  * Send confirmation email
  * Update booking records

These actions occur **concurrently**, not sequentially.

### Resolution

* Swimlanes were used to separate:

  * Student actions
  * System processes
  * Tutor actions (where applicable)
* Parallel flows were introduced to reflect real-world system behavior

### Lesson Learned

* Swimlanes improve **clarity of responsibility**
* Parallel actions improve **accuracy of system modeling**

---

## 5. Key Takeaways

1. **Granularity Requires Balance**

   * Too much detail reduces clarity
   * Too little detail removes essential logic

2. **Diagrams Enhance Agile Artifacts**

   * Activity diagrams reveal missing steps in user stories
   * State diagrams enforce system rules

3. **Different Diagrams, Different Purposes**

   * State diagrams define **boundaries**
   * Activity diagrams define **process flows**

4. **Traceability is Critical**

   * Every diagram element was aligned with:

     * Functional Requirements (FRs)
     * User Stories

---

## Conclusion

The combination of activity and state diagrams provided a comprehensive understanding of the Tutor Booking System. While activity diagrams captured dynamic workflows, state diagrams ensured that object lifecycles remained consistent and valid throughout the system.
