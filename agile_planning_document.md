## Agile Planning Document

---

### 1. User Stories

| Story ID | User Story                                                                                                              | Acceptance Criteria                                                                                                     | Priority |
| -------- | ----------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------- |
| US1      | As a **student**, I want to register and log into the system so that I can access tutoring services securely.           | - User can register with valid details <br> - User can log in with correct credentials <br> - Invalid login shows error | High     |
| US2      | As a **student**, I want to search for tutors by subject, price, and rating so that I can find suitable tutors quickly. | - Search results load within 2 seconds <br> - Filters apply correctly <br> - No results message displayed if none found | High     |
| US3      | As a **student**, I want to book available tutor time slots so that I can schedule sessions easily.                     | - Available slots are displayed <br> - Booking confirmation shown instantly <br> - Double booking is prevented          | High     |
| US4      | As a **tutor**, I want to set and update my availability so that students can book sessions based on my schedule.       | - Tutor can add/remove time slots <br> - Updates reflect instantly <br> - Conflicts are prevented                       | High     |
| US5      | As a **user**, I want to create and manage my profile so that my information is accurate and up to date.                | - Profile data is saved correctly <br> - Updates reflect immediately                                                    | Medium   |
| US6      | As a **student**, I want to make secure online payments so that I can pay for sessions safely.                          | - Payment is processed successfully <br> - System records transaction <br> - Failed payments prompt retry               | High     |
| US7      | As a **student**, I want to receive booking confirmation emails so that I have proof of my scheduled session.           | - Email sent within 1 minute <br> - Email contains booking details                                                      | Medium   |
| US8      | As a **student**, I want to rate tutors after sessions so that I can provide feedback.                                  | - Ratings update instantly <br> - Rating is stored correctly                                                            | Medium   |
| US9      | As a **student**, I want to cancel or reschedule bookings so that I can manage my time flexibly.                        | - Booking updates instantly <br> - Confirmation message displayed                                                       | High     |
| US10     | As an **admin**, I want to manage users and bookings so that I can maintain system control.                             | - Admin can view/edit/delete records <br> - Changes reflect in real time                                                | High     |
| US11     | As a **system admin**, I want user data to be encrypted so that security compliance is ensured.                         | - Data encrypted using AES-256 <br> - Unauthorized access is blocked                                                    | High     |
| US12     | As a **user**, I want the system to respond quickly so that I can use it without delays.                                | - System response time ≤ 2 seconds <br> - System remains stable under load                                              | High     |

---

### 2. Product Backlog

| Story ID | User Story                      | Priority (MoSCoW) | Effort Estimate | Dependencies |
| -------- | ------------------------------- | ----------------- | --------------- | ------------ |
| US1      | User registration and login     | Must-have         | 3               | -            |
| US2      | Search tutors                   | Must-have         | 4               | US1          |
| US3      | Book tutor session              | Must-have         | 5               | US2          |
| US4      | Manage tutor availability       | Must-have         | 3               | -            |
| US5      | Manage user profile             | Should-have       | 2               | US1          |
| US6      | Secure online payment           | Must-have         | 5               | US3          |
| US7      | Booking confirmation email      | Should-have       | 2               | US3          |
| US8      | Rate tutors                     | Could-have        | 2               | US3          |
| US9      | Cancel/reschedule session       | Must-have         | 4               | US3          |
| US10     | Admin management                | Should-have       | 3               | US1          |
| US11     | Data encryption                 | Must-have         | 4               | -            |
| US12     | System performance optimization | Could-have        | 3               | -            |

#### Prioritization Justification

* **Must-have** stories represent the **core MVP functionality** required for system usability, including authentication, tutor search, booking, and payments. These directly align with primary stakeholder goals (students and tutors).
* **Security (US11)** is classified as Must-have because it ensures **data protection and compliance**, which is critical even in early releases.
* **Should-have** stories improve system usability and administrative control but are not essential for initial deployment.
* **Could-have** stories enhance user experience (e.g., ratings, performance optimization) but can be deferred without impacting core functionality.
* This prioritization ensures that **high-value, user-centric features are delivered first**, supporting Agile’s iterative development approach.

---

### 3. Sprint Planning

#### Sprint Goal

**"Implement core tutor booking functionality including authentication, tutor search, and session booking to deliver a usable MVP."**

#### Selected User Stories

* US1
* US2
* US3
* US4
* US11

---

#### Sprint Backlog

| Task ID | Task Description                        | Assigned To        | Estimated Hours | Status |
| ------- | --------------------------------------- | ------------------ | --------------- | ------ |
| T1      | Develop user registration API           | Backend Developer  | 8               | To Do  |
| T2      | Implement login authentication          | Backend Developer  | 6               | To Do  |
| T3      | Design registration & login UI          | Frontend Developer | 10              | To Do  |
| T4      | Develop tutor search API with filters   | Backend Developer  | 10              | To Do  |
| T5      | Design tutor search UI                  | Frontend Developer | 8               | To Do  |
| T6      | Implement booking system API            | Backend Developer  | 12              | To Do  |
| T7      | Create booking interface UI             | Frontend Developer | 10              | To Do  |
| T8      | Develop availability management feature | Backend Developer  | 8               | To Do  |
| T9      | Design availability dashboard           | Frontend Developer | 6               | To Do  |
| T10     | Implement data encryption (AES-256)     | Backend Developer  | 8               | To Do  |
| T11     | Set up database schema                  | Database Engineer  | 6               | To Do  |
| T12     | Write unit tests for core features      | QA Engineer        | 10              | To Do  |

---

#### Sprint Justification

This sprint focuses on delivering the **Minimum Viable Product (MVP)** by:

1. Enabling **user authentication** (US1) to allow secure system access.
2. Providing **tutor search functionality** (US2) so students can find suitable tutors.
3. Implementing **booking functionality** (US3) as the core system feature.
4. Supporting **tutor availability management** (US4) to enable scheduling.
5. Ensuring **data security** (US11) through encryption.

These features collectively establish a **fully functional core system**, enabling basic user interaction and validating the system’s primary purpose.

---

### 4. Traceability Mapping

| User Story | Functional Requirement | Use Case                  |
| ---------- | ---------------------- | ------------------------- |
| US1        | FR4                    | Register & Login          |
| US2        | FR1                    | Search Tutors             |
| US3        | FR2, FR7               | Book Tutor Session        |
| US4        | FR3                    | Manage Tutor Availability |
| US5        | FR5                    | Manage Profile            |
| US6        | FR6                    | Make Payment              |
| US7        | FR7                    | Book Tutor Session        |
| US8        | FR8                    | Rate Tutor                |
| US9        | FR9                    | Cancel/Reschedule Session |
| US10       | FR10                   | Admin Management          |
| US11       | NFR9                   | Security                  |
| US12       | NFR11                  | Performance               |
