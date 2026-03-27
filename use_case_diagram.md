# Use Case Diagram 

```mermaid
graph LR

%% Actors
Student["Student"]
Tutor["Tutor"]
Admin["Platform Administrator"]
PaymentSystem["Payment System"]
NotificationService["Email Service"]
ITTeam["IT/DevOps Team"]

%% Use Cases
UC1["Register/Login (FR4)"]
UC2["Search Tutors (FR1)"]
UC3["Book Session (FR2)"]
UC4["Manage Availability (FR3)"]
UC5["Manage Profile (FR5)"]
UC6["Make Payment (FR6)"]
UC7["Receive Confirmation (FR7)"]
UC8["Rate Tutor (FR8)"]
UC9["Cancel/Reschedule (FR9)"]
UC10["Manage Users/Bookings (FR10)"]

%% Relationships

Student --> UC1
Student --> UC2
Student --> UC3
Student --> UC6
Student --> UC8
Student --> UC9

Tutor --> UC1
Tutor --> UC4
Tutor --> UC5

Admin --> UC10

PaymentSystem --> UC6
NotificationService --> UC7

ITTeam --> UC10

%% Include Relationships
UC3 -->|<<include>>| UC7
UC3 -->|<<include>>| UC6

%% Generalization
User["User"]
User --> Student
User --> Tutor
```

---

#### **Explanation of the Use Case Diagram**

1. **Key Actors and Roles**:
    - **Platform Administrator**: Manages users and bookings through the admin dashboard.
    - **Tutor**: Sets availability, manages profile, and delivers tutoring sessions.
    - **Student**: Searches for tutors, books sessions, makes payments, and rates tutors.
    - **Payment System**: Processes secure online payments.
    - **Email Service**: Sends booking confirmations and notifications.
    - **IT/DevOps Team**: Monitors system performance and ensures uptime.

2. **Relationships**:
    - **Generalization**: Student and Tutor inherit from a general "User" actor, as both interact with the system but have different permissions.
    - **Inclusion**:
        - Booking a session includes making a payment.
        - Booking a session includes sending a confirmation email.
    - **Dependency**:
        - Notifications depend on the email service.
        - Payment processing depends on the external payment system.

3. **Alignment with Stakeholder Concerns**:
    - **Students**: Use cases like "Search Tutors" and "Book Session" address ease of booking and availability concerns.
    - **Tutors**: "Manage Availability" and "Manage Profile" support flexible scheduling and visibility.
    - **Platform Administrators**: "Manage Users/Bookings" ensures system control and data accuracy.
    - **Finance/Payment Stakeholders**: "Make Payment" ensures secure and reliable transactions.
    - **IT/DevOps Team**: System interactions ensure performance, scalability, and uptime requirements are maintained.