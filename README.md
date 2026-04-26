# Tutoring Session Booking System

## Description

The Tutoring Session Booking System is a software application designed to help students schedule tutoring sessions with tutors. The system allows students to browse available tutors, book tutoring sessions, and manage their bookings. Tutors can manage their availability and view scheduled sessions, while administrators oversee the system and manage users.

The goal of this system is to simplify the process of organizing tutoring sessions by providing a centralized platform for scheduling and managing tutoring activities.

## Project Documentation

- [Activity and State Reflections](activity_and_state_reflections.md)
- [Activity Workflow Modelling](activity_worflow_modelling.md)
- [ARCHITECTURE.md](ARCHITECTURE.md)
- [Class Diagram.md](class_diagram.md)
- [Domain Model.md](domain_model.md)
- [Domain Model Explanation.md](domain_model_explanation.md)
- [Domain Model Reflection.md](domain_model_reflection.md)
- [Kanban Explanation](kanban_explanation.md)
- [Object State Modelling](object_state_modelling.md)
- [Reflection In Balancing Stakeholder Needs.md](reflection_in_balancing_stakeholder.md)
- [Reflection Translating Requirements To Use Cases.md](releflection_translating_requirements_to_use_cases.md)
- [Selecting and Customising Reflection](selecting_and_customising_reflection.md)
- [SPECIFICATION.md](SPECIFICATION.md)
- [Stakeholder Analysis.md](stakeholder_analysis.md)
- [System Requirements Document.md](system_requirements_document.md)
- [Template Analysis](template_analysis.md)
- [Test Cases Table](test_cases_table.md)
- [Use Case Specifications](use_case_specifications.md)
- [User Stories Reflection](user_stories_reflection.md)
- [src](./src)
- [creational patterns](./creational_patterns)
- [tests](./tests)

---
&nbsp;

### Kanban Board Implementation 

A new GitHub Project was created using the **Team Planning template** and customized to function as a Kanban board for managing the Tutor Booking System development workflow.

#### Customization of the Kanban Board

The default template was modified to better align with Agile and Kanban principles. The following workflow columns were defined:

- **Backlog**: Contains all tasks and user stories from the sprint backlog (Assignment 6).
- **Todo**: Tasks that are ready to be started.
- **In Progress**: Tasks that are currently being worked on.
- **Testing**: Tasks that have been developed and are undergoing verification.
- **Blocked**: Tasks that cannot proceed due to dependencies or issues.
- **Done**: Completed and verified tasks.

These custom columns were added to improve workflow visibility and better represent real-world software development processes.

#### Task Management and Workflow

All sprint tasks (T1–T12) were created as GitHub Issues and linked to the project board. Each task includes:
- A clear description  
- Assigned role  
- Estimated time  
- Labels (e.g., backend, frontend, testing, security)  
- Task assignment using @mentions  

Tasks are moved across columns as work progresses, providing a visual representation of the development lifecycle.

#### Work-In-Progress (WIP) Control

To improve efficiency and avoid overloading, a Work-In-Progress limit was applied:
- A maximum of **2–3 tasks** are allowed in the **In Progress** column at any given time.

This helps maintain focus, reduce multitasking, and prevent bottlenecks.

#### Benefits of the Kanban Board

The customized Kanban board provides:
- **Improved visibility** of task progress  
- **Better organization** of development activities  
- **Enhanced workflow tracking**  
- **Support for Agile principles**, including continuous delivery and adaptability  

---

### Language Choice & Design Decisions

#### Language Choice
Python was selected due to its simplicity, readability, and strong support for object-oriented programming. It allows rapid development and easy implementation of design patterns without excessive boilerplate code.

#### Key Design Decisions
- **Object-Oriented Design:** The system is built using OOP principles such as inheritance, encapsulation, and modularity.
- **Separation of Concerns:** Core system logic (`/src`) is separated from creational patterns (`/creational_patterns`) and testing (`/tests`).
- **Scalability:** The design allows easy extension (e.g., adding new user types or payment methods).
- **Maintainability:** Code is modular and organized into logical components for readability and reuse.

---


### Creational Design Patterns & Justification

#### 1. Simple Factory
- **Implementation:** UserFactory
- **Why used:** Centralizes creation of Student and Tutor objects, reducing duplication and simplifying future extension (e.g., adding Admin users).


#### 2. Factory Method
- **Implementation:** Payment processors (CreditCard, PayPal)
- **Why used:** Delegates object creation to subclasses, allowing flexible addition of new payment methods without modifying existing code.

#### 3. Abstract Factory
- **Implementation:** Notification system (Student/Tutor notifications)
- **Why used:** Creates related notification objects (Email and SMS) for different user types, ensuring consistency across communication channels.

#### 4. Builder
- **Implementation:** BookingBuilder
- **Why used:** Allows step-by-step construction of Booking objects, especially useful when some attributes are optional or added incrementally.

#### 5. Prototype
- **Implementation:** SessionPrototype
- **Why used:** Enables cloning of existing Session objects, avoiding repeated initialization for similar session configurations.

#### 6. Singleton
- **Implementation:** DatabaseConnection
- **Why used:** Ensures only one database connection instance exists, preventing resource conflicts and unnecessary duplication.