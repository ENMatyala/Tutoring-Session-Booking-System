# Domain Model Explanation for Tutor Booking System

---

## 1. Overview

This domain model represents the core entities, relationships, and business rules of the Tutor Booking System. It captures how students, tutors, bookings, and payments interact to support the system’s main functionality.

The model is aligned with the system’s functional requirements and supports workflows such as tutor search, session booking, payment processing, and review submission.

---

## 2. Core Entities

### A. User (Central Entity)

Represents all users of the system, including students and tutors.

**Key Attributes:**

* `email`, `password`: Used for authentication
* `role`: Defines whether the user is a student, tutor, or admin
* `status`: Tracks account state (e.g., active, suspended)

**Purpose:**

* Supports authentication and access control
* Maps to **FR4 (User Registration & Login)**

---

### B. Student

Represents users who request tutoring services.

**Responsibilities:**

* Search for tutors
* Book sessions
* Make payments
* Submit reviews

**Relationships:**

* A student can create multiple bookings
* A student can write multiple reviews

**Alignment:**

* FR1 (Search Tutors)
* FR2 (Book Session)
* FR8 (Rate Tutor)

---

### C. Tutor

Represents service providers offering tutoring sessions.

**Key Attributes:**

* `subject`: Area of expertise
* `hourlyRate`: Pricing for sessions
* `rating`: Aggregated feedback from students

**Responsibilities:**

* Manage availability
* Deliver sessions
* Receive reviews

**Alignment:**

* FR1 (Search Tutors)
* FR3 (Manage Availability)
* FR8 (Ratings)

---

### D. Booking (Core Transaction Entity)

Represents a reservation made by a student for a tutor session.

**Key Attributes:**

* `date`: Scheduled session date
* `status`: Tracks lifecycle (pending, confirmed, cancelled)

**Responsibilities:**

* Connects student and tutor
* Initiates session creation
* Triggers payment process

**Relationships:**

* One booking creates one session
* One booking requires one payment

**Alignment:**

* FR2 (Booking System)
* FR9 (Cancel/Reschedule)

---

### E. Session

Represents the actual tutoring session.

**Key Attributes:**

* `startTime`, `endTime`: Duration of session
* `status`: Tracks session progress (scheduled, ongoing, completed)

**Purpose:**

* Tracks execution of booked services
* Enables post-session actions like reviews

**Alignment:**

* FR2 (Booking execution)
* FR9 (Session updates)

---

### F. Payment

Handles financial transactions associated with bookings.

**Key Attributes:**

* `amount`: Payment value
* `status`: Payment state (processing, successful, failed)

**Responsibilities:**

* Ensures secure transaction processing
* Confirms booking validity

**Alignment:**

* FR6 (Secure Online Payments)
* NFR9 (Security - encryption)

---

### G. AvailabilitySlot

Represents time slots defined by tutors for booking.

**Key Attributes:**

* `startTime`, `endTime`
* `status`: Available, booked, or unavailable

**Purpose:**

* Prevents double booking
* Enables real-time scheduling

**Alignment:**

* FR3 (Manage Tutor Availability)

---

### H. Review

Represents feedback provided by students after sessions.

**Key Attributes:**

* `rating`: Numeric evaluation
* `comment`: Written feedback

**Purpose:**

* Improves tutor transparency
* Supports decision-making for students

**Alignment:**

* FR8 (Rating System)

---

## 3. Relationships

The relationships in the domain model define how entities interact:

* A **User** is extended into **Student** and **Tutor** roles
* A **Student** creates multiple **Bookings**
* A **Tutor** receives multiple **Bookings**
* A **Booking** creates a **Session** and requires a **Payment**
* A **Tutor** manages multiple **Availability Slots**
* A **Session** generates a **Review**
* A **Student** writes reviews for a **Tutor**

These relationships ensure clear separation of responsibilities and support system scalability.

---

## 4. Key Business Rules

1. **Booking Lifecycle**

   * A booking must exist before payment is processed
   * A session is created only after booking confirmation

2. **Availability Constraint**

   * A time slot cannot be double-booked
   * Conflicts are prevented at booking time

3. **Payment Validation**

   * Bookings are confirmed only after successful payment

4. **Review Eligibility**

   * Reviews can only be submitted after session completion

---

## 5. Alignment with Requirements

| Requirement | Domain Model Component |
| ----------- | ---------------------- |
| FR1         | Tutor                  |
| FR2         | Booking, Session       |
| FR3         | AvailabilitySlot       |
| FR4         | User                   |
| FR5         | Student, Tutor         |
| FR6         | Payment                |
| FR8         | Review                 |
| FR9         | Booking                |

---

## 6. Alignment with Behavioral Models

The domain model is consistent with the behavioral models developed in Assignment 8:

* **Activity Diagrams**

  * Booking and payment workflows directly involve the Booking, Payment, and Session entities
  * Availability management aligns with the AvailabilitySlot entity

* **State Diagrams**

  * Booking lifecycle (Pending → Confirmed → Completed) aligns with the Booking entity
  * Session lifecycle aligns with the Session entity
  * Payment states align with the Payment entity

This ensures consistency between system structure and behavior.

---

## 7. Design Decisions

Several key design decisions were made during modeling:

* **Separation of Booking and Session**

  * Booking represents reservation, while Session represents execution
  * Improves clarity and lifecycle management

* **Use of Inheritance (User → Student, Tutor)**

  * Reduces duplication
  * Supports scalability for additional roles

* **Association between Booking and Payment**

  * Ensures that bookings are validated through payment

* **Use of AvailabilitySlot**

  * Prevents double booking
  * Supports flexible scheduling

---

## 8. Conclusion

The domain model provides a clear representation of the Tutor Booking System’s structure. It ensures that all major system functionalities—booking, payment, scheduling, and feedback—are properly modeled and aligned with functional requirements, behavioral models, and design decisions.

This model serves as a strong foundation for both system design and implementation.
