# Test Case Development (Aligned with Assignment 4)

## Functional Test Cases

| Test ID | Requirement ID | Description | Steps | Expected Result | Actual Result | Status |
|--------|---------------|------------|-------|----------------|---------------|--------|
| TC1 | FR4 | Register/Login user | Enter credentials  Submit | User logs in within 2 seconds | | |
| TC2 | FR1 | Search tutors | Enter subject, price, rating  Search | Results displayed within ≤2 seconds | | |
| TC3 | FR2 | Book tutor session | Select tutor  Choose slot  Confirm | Booking confirmed instantly | | |
| TC4 | FR3 | Manage tutor availability | Update schedule | Changes reflected in real time | | |
| TC5 | FR5 | Manage profile | Update profile details | Profile updated correctly | | |
| TC6 | FR6 | Make payment | Complete payment process | Transaction successful (99%) | | |
| TC7 | FR7 | Booking confirmation email | Book session | Email sent within 1 minute | | |
| TC8 | FR8 | Rate tutor | Submit rating | Rating updated immediately | | |
| TC9 | FR9 | Cancel/reschedule booking | Modify booking | Changes reflected instantly | | |
| TC10 | FR10 | Admin management | Admin edits users/bookings | Updates reflected in system | | |

---

## Non-Functional Test Cases

### NFR11 – Performance
- Scenario: System response time under load  
- Steps:
  - Simulate 1,000 concurrent users  
  - Perform search and booking  
- Expected Result: Response time ≤ 2 seconds  

---

### NFR10 – Security (RBAC)
- Scenario: Role-based access control enforcement  
- Steps:
  - Login as student  
  - Attempt to access admin features  
- Expected Result: Access denied  

---

### NFR9 – Data Encryption
- Scenario: Secure data storage  
- Steps:
  - Inspect stored user data  
- Expected Result: Data is encrypted using AES-256  

---

### NFR2 – Usability (Booking Flow)
- Scenario: Booking process simplicity  
- Steps:
  - Perform booking  
- Expected Result: Booking completed in ≤ 3 steps 