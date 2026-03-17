# Reflection – Balancing Stakeholder Needs in Tutor Booking System

## Introduction
This project required balancing the needs of multiple stakeholders, including students, tutors, administrators, and technical teams. Each group had different priorities, which often conflicted during the requirements definition process.

---

## Key Challenges in Balancing Stakeholder Needs

### 1. Students vs Tutors
Students require a fast and simple booking process, while tutors need flexibility in managing their schedules.

- **Conflict**: Students prefer instant booking, but tutors need control over availability.
- **Resolution**: Implemented a real-time availability system where tutors define time slots, ensuring both ease of booking and tutor control.

---

### 2. Usability vs Security
Students and tutors expect a quick and seamless experience, while the system must enforce strong security measures.

- **Conflict**: Security features like authentication and encryption can slow down user interactions.
- **Resolution**: Balanced by implementing secure login with minimal steps and optimized encryption processes.

---

### 3. Performance vs Scalability
The system must be fast for current users while also supporting future growth.

- **Conflict**: Designing for scalability can introduce complexity that affects performance.
- **Resolution**: Defined performance limits (≤2 seconds response time) while ensuring the system can handle 1,000 concurrent users.

---

### 4. Administrators vs Users
Administrators require control over the system, while users prefer minimal restrictions.

- **Conflict**: Too many admin controls can negatively impact user experience.
- **Resolution**: Designed role-based access control to ensure admins have oversight without disrupting users.

---

### 5. Payment Reliability vs User Convenience
Users want quick payments, while financial stakeholders require secure and verifiable transactions.

- **Conflict**: Strong payment validation may slow the process.
- **Resolution**: Implemented secure but optimized payment processing with high success rates.

---

## Lessons Learned

- Stakeholder needs often conflict and require trade-offs rather than perfect solutions.
- Clear prioritization of requirements helps in resolving conflicts.
- Non-functional requirements play a critical role in balancing stakeholder expectations.

---

## Conclusion

Balancing stakeholder needs was a critical part of this project. By identifying conflicts early and designing appropriate solutions, the system ensures usability, performance, and security while satisfying all major stakeholders.