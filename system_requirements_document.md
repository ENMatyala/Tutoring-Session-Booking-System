# System Requirements Document (SRD)
## Tutor Booking System

---

## 1. Functional Requirements

### Booking System
**FR1**: The system shall allow students to search for tutors by subject, price, and rating.  
- Acceptance Criteria: Results displayed in ≤2 seconds with filters applied.

**FR2**: The system shall allow students to book available time slots.  
- Acceptance Criteria: Booking confirmation is shown immediately after selection.

**FR3**: The system shall allow tutors to set and update availability.  
- Acceptance Criteria: Updated schedule reflects in real time.

---

### User Management
**FR4**: The system shall allow users to register and log in.  
- Acceptance Criteria: Login succeeds within 2 seconds.

**FR5**: The system shall allow profile creation for tutors and students.  
- Acceptance Criteria: Profiles display accurate user details.

---

### Payment System
**FR6**: The system shall support secure online payments.  
- Acceptance Criteria: Transactions complete successfully 99% of the time.

---

### Notifications
**FR7**: The system shall send booking confirmations via email.  
- Acceptance Criteria: Email delivered within 1 minute.

---

### Reviews & Ratings
**FR8**: The system shall allow students to rate tutors.  
- Acceptance Criteria: Ratings update immediately.

---

### Session Management
**FR9**: The system shall allow cancellation and rescheduling of bookings.  
- Acceptance Criteria: Changes reflected instantly.

---

### Admin Controls
**FR10**: The system shall allow admins to manage users and bookings.  
- Acceptance Criteria: Admin dashboard updates in real time.

---

## 2. Non-Functional Requirements

### Usability
**NFR1**: The system shall have an intuitive UI usable without training.  
**NFR2**: Booking process shall not exceed 3 steps.

---

### Deployability
**NFR3**: The system shall be deployable on Linux and Windows.  
**NFR4**: Deployment shall be completed within 1 hour using Docker.

---

### Maintainability
**NFR5**: Code shall follow modular architecture.  
**NFR6**: Documentation shall include API guides.

---

### Scalability
**NFR7**: The system shall support 1,000 concurrent users.  
**NFR8**: The system shall support future feature expansion.

---

### Security
**NFR9**: All user data shall be encrypted (AES-256).  
**NFR10**: Role-based access control shall be implemented.

---

### Performance
**NFR11**: System response time shall be ≤2 seconds.  
**NFR12**: Booking confirmation shall occur instantly.

---

## 3. Requirements Traceability

- Student needs → FR1, FR2, FR8  
- Tutor needs → FR3, FR5  
- Admin needs → FR10  
- Payment concerns → FR6, NFR9  
- Performance concerns → NFR11, NFR12  

---

## 4. Requirements Coverage

This section maps functional and non-functional requirements to stakeholder concerns and quality attributes.

### Coverage by Quality Attributes

- **Usability**
  - Addressed by: FR1, FR2, FR4, FR5, NFR1, NFR2  
  - Explanation: Students and tutors can easily navigate the system, register, and complete bookings in a few steps.

- **Deployability**
  - Addressed by: NFR3, NFR4  
  - Explanation: System supports Docker-based deployment across platforms, enabling easy installation and setup.

- **Maintainability**
  - Addressed by: NFR5, NFR6, FR10  
  - Explanation: Modular design and admin controls allow easy updates, debugging, and system management.

- **Scalability**
  - Addressed by: NFR7, NFR8  
  - Explanation: System supports increasing users and future feature expansion without performance degradation.

- **Security**
  - Addressed by: FR4, FR6, NFR9, NFR10  
  - Explanation: Authentication, secure payments, and encrypted data protect user information.

- **Performance**
  - Addressed by: FR1, FR2, FR7, NFR11, NFR12  
  - Explanation: Fast search, booking, and notifications ensure a responsive user experience.

---

### Coverage by Stakeholder Needs

- **Students**
  - Addressed by: FR1, FR2, FR7, FR8, FR9  
  - Ensures easy booking, communication, and feedback.

- **Tutors**
  - Addressed by: FR3, FR5, FR8  
  - Supports schedule management and performance tracking.

- **Administrators**
  - Addressed by: FR10, NFR5  
  - Enables system monitoring and management.

- **Finance/Payment Stakeholders**
  - Addressed by: FR6, NFR9  
  - Ensures secure and reliable transactions.

- **IT/DevOps Team**
  - Addressed by: NFR3, NFR7, NFR11  
  - Supports deployment, scaling, and performance.

- **Support Staff**
  - Addressed by: FR9, FR10  
  - Helps resolve user issues efficiently.

---