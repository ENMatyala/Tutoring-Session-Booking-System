# Activity Workflow Modeling for Tutor Booking System

---

## 1. Book Tutor Session Workflow

```mermaid
flowchart LR

subgraph Student
    A[Select tutor]
    B[Select time slot]
end

subgraph System
    C{Slot available?}
    D[Create booking]
    E[Suggest alternatives]
    F[Send confirmation email]
    G[Update booking records]
end

Start([Start]) --> A
A --> B
B --> C

C -->|Yes| D
C -->|No| E

D --> F
D --> G

F --> End([End])
G --> End
E --> End
```

### Key Features

* **Swimlanes**: Student vs System clearly separated
* **Decision**: Slot availability check
* **Parallel Actions**:

  * Send confirmation
  * Update records

### Alignment

* FR2 (Booking), FR7 (Notifications)

---

## 2. Make Payment Workflow

```mermaid
flowchart LR

subgraph Student
    A[Select payment method]
end

subgraph System
    B[Process payment]
    C{Payment successful?}
    D[Confirm transaction]
    E[Notify failure]
    F[Update booking status]
end

Start --> A
A --> B
B --> C

C -->|Yes| D
C -->|No| E

D --> F
F --> End
E --> End
```

### Features

* Decision handling payment success/failure
* System-driven actions clearly separated

### Alignment

* FR6 (Payment)

---

## 3. Search Tutors Workflow

```mermaid
flowchart LR

subgraph Student
    A[Enter search filters]
end

subgraph System
    B[Process filters]
    C{Results found?}
    D[Display tutors]
    E[Show no results]
end

Start --> A
A --> B
B --> C

C -->|Yes| D
C -->|No| E

D --> End
E --> End
```

---

## 4. Manage Availability Workflow

```mermaid
flowchart LR

subgraph Tutor
    A[Open schedule]
    B[Add/remove slot]
end

subgraph System
    C{Conflict exists?}
    D[Show error]
    E[Update availability]
end

Start --> A
A --> B
B --> C

C -->|Yes| D
C -->|No| E

D --> End
E --> End
```

---

## 5. Cancel / Reschedule Booking Workflow

```mermaid
flowchart LR

subgraph Student
    A[Select booking]
    B[Choose cancel/reschedule]
end

subgraph System
    C[Update booking]
    D[Notify tutor]
    E[Update availability]
end

Start --> A
A --> B
B --> C

C --> D
C --> E

D --> End
E --> End
```

### Parallel Actions

* Notify tutor
* Update availability

---

## 6. Rate Tutor Workflow

```mermaid
flowchart LR

subgraph Student
    A[Select completed session]
    B[Submit rating]
end

subgraph System
    C[Store review]
    D[Update tutor rating]
end

Start --> A
A --> B
B --> C

C --> D
D --> End
```

---

## 7. Manage Profile Workflow

```mermaid
flowchart LR

subgraph User
    A[Open profile]
    B[Edit details]
end

subgraph System
    C[Validate changes]
    D[Save updates]
end

Start --> A
A --> B
B --> C
C --> D
D --> End
```

---

## 8. User Registration & Login Workflow

```mermaid
flowchart LR

subgraph User
    A[Enter credentials]
end

subgraph System
    B{Valid?}
    C[Create/Login user]
    D[Show error]
end

Start --> A
A --> B

B -->|Yes| C
B -->|No| D

C --> End
D --> End
```

---

## Conclusion

These activity diagrams:

* Use **swimlanes to separate responsibilities**
* Include **decision points and branching logic**
* Model **parallel system actions**
* Align with **functional requirements and real workflows**

They now fully satisfy the assignment brief and UML expectations.

---

## Traceability to Requirements

The activity workflows are directly mapped to functional requirements and user stories to ensure consistency and completeness.

| Workflow                  | Functional Requirement | Description                                 |
| ------------------------- | ---------------------- | ------------------------------------------- |
| User Registration & Login | FR4                    | Handles account creation and authentication |
| Search Tutors             | FR1                    | Enables filtering and discovery of tutors   |
| Book Tutor Session        | FR2, FR7               | Manages booking process and notifications   |
| Manage Availability       | FR3                    | Allows tutors to control their schedule     |
| Manage Profile            | FR5                    | Supports updating user information          |
| Make Payment              | FR6                    | Handles secure transaction processing       |
| Cancel / Reschedule       | FR9                    | Allows booking modifications                |
| Rate Tutor                | FR8                    | Enables feedback and rating system          |

### User Story Alignment

Each workflow corresponds to user stories defined in the Agile Planning document. The diagrams expand these stories by:

* Including system-level validation steps
* Representing decision points and alternative flows
* Capturing parallel system actions

---

## Conclusion Update

The activity diagrams are fully traceable to system requirements and user stories, ensuring that all workflows support the intended functionality of the Tutor Booking System.
