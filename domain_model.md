# Domain Model for Tutor Booking System

---

## Domain Entities

| Entity           | Attributes                                 | Methods                                     | Relationships                                            |
| ---------------- | ------------------------------------------ | ------------------------------------------- | -------------------------------------------------------- |
| User             | userId, email, password, role, status      | register(), login(), logout()               | Parent of Student and Tutor                              |
| Student          | studentId, name                            | searchTutor(), bookSession(), writeReview() | Creates Booking, writes Review                           |
| Tutor            | tutorId, name, subject, hourlyRate, rating | manageAvailability(), updateProfile()       | Receives Booking, manages AvailabilitySlot               |
| Booking          | bookingId, date, status                    | createBooking(), cancelBooking()            | Links Student & Tutor, creates Session, requires Payment |
| Session          | sessionId, startTime, endTime, status      | startSession(), endSession()                | Created from Booking                                     |
| Payment          | paymentId, amount, status                  | processPayment(), validatePayment()         | Associated with Booking                                  |
| AvailabilitySlot | slotId, startTime, endTime, status         | addSlot(), removeSlot()                     | Managed by Tutor                                         |
| Review           | reviewId, rating, comment                  | createReview(), updateReview()              | Written by Student for Tutor                             |

---

## Business Rules

1. A student can create multiple bookings, but each booking belongs to one student
2. A tutor can manage multiple availability slots
3. A booking must be paid before it is confirmed
4. A session is created only after booking confirmation
5. A review can only be created after session completion

---

## Relationships Summary

* User is a parent class of Student and Tutor
* Student creates multiple Bookings
* Tutor receives multiple Bookings
* Booking creates a Session and requires a Payment
* Tutor manages multiple AvailabilitySlots
* Session generates a Review
* Student writes Reviews for Tutor

---

## Traceability to Requirements

| Entity           | Functional Requirement          |
| ---------------- | ------------------------------- |
| User             | FR4 (User Registration & Login) |
| Student          | FR1, FR2, FR8                   |
| Tutor            | FR1, FR3, FR8                   |
| Booking          | FR2, FR9                        |
| Session          | FR2                             |
| Payment          | FR6                             |
| AvailabilitySlot | FR3                             |
| Review           | FR8                             |

---

## Conclusion

This domain model captures the core structure of the Tutor Booking System by defining key entities, their attributes, behaviors, and relationships. It ensures alignment with functional requirements and provides a solid foundation for the class diagram and overall system design.
