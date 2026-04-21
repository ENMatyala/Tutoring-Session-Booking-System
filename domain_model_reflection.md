# Reflection: Domain Model and Class Diagram Design

---

## 1. Challenges Faced

One of the main challenges encountered during the development of the domain model and class diagram was determining the appropriate level of abstraction. Initially, there was a tendency to include excessive implementation details, which made the model overly complex and difficult to interpret. Striking a balance between simplicity and completeness required careful consideration.

Another challenge involved defining accurate relationships between entities. For example, deciding whether the Booking entity should directly include session-related data or reference a separate Session entity required evaluating system behavior and lifecycle separation.

Additionally, identifying suitable methods for each class was challenging, as it required thinking beyond static structure and considering how objects would behave within the system.

---

## 2. Alignment with Previous Assignments

The domain model and class diagram were designed to align closely with artifacts developed in earlier assignments:

* **Functional Requirements (Assignment 4):**

  * Booking, Payment, Availability, and Review functionalities are directly represented in the model

* **Use Case Specifications (Assignment 5):**

  * Use cases such as “Book Tutor Session,” “Manage Availability,” and “Rate Tutor” are reflected through entity interactions

* **Activity Diagrams (Assignment 8):**

  * Booking and payment workflows correspond to interactions between Booking, Payment, and Session entities

* **State Diagrams (Assignment 8):**

  * Booking lifecycle states (Pending → Confirmed → Completed) align with the Booking entity
  * Session and Payment lifecycles are also reflected in their respective entities

This alignment ensures consistency between system structure and behavior.

---

## 3. Trade-offs

A key trade-off in the design process was balancing simplicity and detail. While adding more attributes and methods could improve completeness, it also risked reducing readability. The final model focuses on core elements necessary for understanding system functionality.

Another trade-off involved the use of inheritance versus associations. Implementing inheritance for the User entity (with Student and Tutor as subclasses) improved structure and reduced redundancy but required careful consideration of shared and distinct attributes.

Separating Booking and Session into two entities improved clarity in representing system workflows but introduced additional relationships that needed to be managed.

---

## 4. Object-Oriented Design Insights

The modeling process reinforced several important object-oriented design principles:

* **Encapsulation:** Each class contains its own attributes and methods, representing both data and behavior
* **Abstraction:** Only essential details are included to maintain clarity and relevance
* **Inheritance:** The User class is generalized into Student and Tutor roles to avoid duplication
* **Separation of Concerns:** Distinct entities (e.g., Booking, Session, Payment) handle different responsibilities

These principles contributed to a more structured and scalable design.

---

## 5. Lessons Learned

* Effective system modeling requires balancing abstraction with practical system behavior
* Relationships between entities are more critical than individual attributes
* Models must remain aligned with system requirements and workflows
* Simplicity improves readability and communication with stakeholders

---

## Conclusion

The domain model and class diagram provide a clear and structured representation of the Tutor Booking System. By aligning with previous assignments and applying object-oriented design principles, the models support a consistent and comprehensive understanding of the system. These artifacts form a strong foundation for further system development and implementation.
