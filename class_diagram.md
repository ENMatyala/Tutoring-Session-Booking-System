# Class Diagram for Tutor Booking System

```mermaid
classDiagram

class User {
  -userId: String
  -email: String
  -password: String
  -role: String
  -status: String
  +register()
  +login()
  +logout()
}

class Student {
  -studentId: String
  -name: String
  +searchTutor()
  +bookSession()
  +writeReview()
}

class Tutor {
  -tutorId: String
  -name: String
  -subject: String
  -hourlyRate: Float
  -rating: Float
  +manageAvailability()
  +updateProfile()
}

class Booking {
  -bookingId: String
  -date: Date
  -status: String
  +createBooking()
  +cancelBooking()
}

class Session {
  -sessionId: String
  -startTime: DateTime
  -endTime: DateTime
  -status: String
  +startSession()
  +endSession()
}

class Payment {
  -paymentId: String
  -amount: Float
  -status: String
  +processPayment()
  +validatePayment()
}

class AvailabilitySlot {
  -slotId: String
  -startTime: DateTime
  -endTime: DateTime
  -status: String
  +addSlot()
  +removeSlot()
}

class Review {
  -reviewId: String
  -rating: int
  -comment: String
  +createReview()
  +updateReview()
}

User <|-- Student
User <|-- Tutor

Student "1" --> "0..*" Booking : creates
Tutor "1" --> "0..*" Booking : receives
Booking "1" --> "1" Session : creates
Booking "1" --> "1" Payment : requires
Tutor "1" --> "0..*" AvailabilitySlot : manages
Session "1" --> "0..1" Review : generates
Student "1" --> "0..*" Review : writes
Tutor "1" --> "0..*" Review : receives
```

---

## Design Decisions

* **Inheritance used** for User → Student/Tutor to avoid duplication
* **Booking and Session separated** to distinguish reservation vs execution
* **Payment linked to Booking** to enforce transaction validation
* **Multiplicity defined** to reflect real-world constraints

---

## Alignment with Previous Assignments

* Use Cases: Booking, Payment, Review workflows
* Activity Diagrams: Booking & payment flows
* State Diagrams: Booking lifecycle, session lifecycle

This ensures consistency across all system models.
