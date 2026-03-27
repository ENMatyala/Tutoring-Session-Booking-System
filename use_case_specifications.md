# Use Case Specifications 

## 1. Register and Login (FR4)

### Description
Allows users (students and tutors) to register and log into the system.

### Preconditions
- User must have a valid email  
- System must be online  

### Postconditions
- User account is created  
- User is authenticated and redirected to dashboard  

### Basic Flow
1. User enters registration details or login credentials  
2. System validates input  
3. System creates account or authenticates user  
4. User is redirected to dashboard  

### Alternative Flows
- Invalid credentials → error message displayed  
- Existing account → user logs in  

---

## 2. Search Tutors (FR1)

### Description
Allows students to search for tutors by subject, price, and rating.

### Preconditions
- Student must be logged in  

### Postconditions
- Filtered list of tutors is displayed  

### Basic Flow
1. Student enters search criteria (subject, price, rating)  
2. System processes filters  
3. Matching tutors are displayed within 2 seconds  

### Alternative Flows
- No tutors found → system displays message  

---

## 3. Book Tutor Session (FR2, FR7)

### Description
Allows students to book available tutor time slots and receive confirmation.

### Preconditions
- Student must be logged in  
- Tutor must have available slots  

### Postconditions
- Booking is saved  
- Confirmation email is sent  

### Basic Flow
1. Student selects a tutor  
2. Student selects available time slot  
3. System confirms availability  
4. Booking is created instantly  
5. System sends confirmation email within 1 minute  

### Alternative Flows
- Slot unavailable → system suggests alternative slots  

---

## 4. Manage Tutor Availability (FR3)

### Description
Allows tutors to set and update their availability.

### Preconditions
- Tutor must be logged in  

### Postconditions
- Updated availability is reflected in real time  

### Basic Flow
1. Tutor accesses schedule dashboard  
2. Tutor adds or removes time slots  
3. System updates schedule instantly  

### Alternative Flows
- Conflicting booking → system prevents update and alerts tutor  

---

## 5. Manage Profile (FR5)

### Description
Allows users to create and update their profiles.

### Preconditions
- User must be logged in  

### Postconditions
- Profile information is saved and displayed accurately  

### Basic Flow
1. User navigates to profile page  
2. User enters or updates details  
3. System saves and displays updated profile  

---

## 6. Make Payment (FR6)

### Description
Allows students to make secure online payments for sessions.

### Preconditions
- Booking must exist  
- Payment gateway must be available  

### Postconditions
- Payment is processed securely  
- Transaction is recorded  

### Basic Flow
1. Student selects payment option  
2. System redirects to secure payment gateway  
3. Student completes payment  
4. System confirms transaction  

### Alternative Flows
- Payment failure → system prompts retry  

---

## 7. Rate Tutor (FR8)

### Description
Allows students to rate tutors after sessions.

### Preconditions
- Student must have completed a session  

### Postconditions
- Rating is recorded and updated immediately  

### Basic Flow
1. Student selects completed session  
2. Student submits rating  
3. System updates tutor rating instantly  

---

## 8. Cancel/Reschedule Session (FR9)

### Description
Allows students to cancel or reschedule bookings.

### Preconditions
- Booking must exist  

### Postconditions
- Booking is updated or cancelled  
- Changes reflected instantly  

### Basic Flow
1. Student selects booking  
2. Chooses cancel or reschedule  
3. System updates booking  
4. System confirms changes  

### Alternative Flows
- Invalid request → system displays error  

---

## 9. Admin Manage Users & Bookings (FR10)

### Description
Allows administrators to manage users and bookings.

### Preconditions
- Admin must be logged in  

### Postconditions
- System records updates  

### Basic Flow
1. Admin accesses dashboard  
2. Admin views users/bookings  
3. Admin edits or removes records  
4. System updates data in real time  