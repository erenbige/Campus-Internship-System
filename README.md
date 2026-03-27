# CodeCampus - Campus Internship & Job Tracking System

## 1. Executive Summary & Vision
The *CodeCampus Internship System* is a centralized, secure web-based platform designed exclusively to bridge the gap between university students seeking internship opportunities and companies looking for young talent. 
* *Vision:* To become the primary career-launching ecosystem for universities nationwide by providing a hyper-niche, distraction-free, and 100% relevant talent pool.

## 2. Team Structure & Roles
| Team Member | Role | Main Responsibility |
| :--- | :--- | :--- |
| *Cabir Eren Yıldırım* | Project Manager & Backend | Project Planning, Jira Management, Team Coordination, Backend API |
| *Eyüp Tekne* | Frontend Developer | UI/UX Design, HTML/CSS coding, Bootstrap 5 UI components |
| *Mert Hasan Yılmaz* | Backend Developer | Database architecture, Django REST API development |
| *Batuhan Yılmaz* | Tester / QA | Error detection, testing scenarios, quality control |
| *Alperen Uslu* | Documentation Specialist | Project reports, UML diagrams, presentation preparation |

## 3. Core Features
* *Student Module:* Secure registration, PDF CV uploads, and one-click applications to active postings.
* *Company Module:* Full CRUD operations for job postings and an intuitive dashboard to review incoming applications.
* *Admin Module:* A strict approval mechanism governed by university admins to ensure platform reliability and data safety.

## 4. Technical Architecture & Technology Stack
The project is built on a modern, decoupled Client-Server architecture. The backend and frontend operate independently, communicating via a RESTful API using JSON.

* *Frontend (Client-Side):* * HTML5, CSS3, and Bootstrap 5 (via CDN) for a rapid, responsive, and mobile-first design.
  * Vanilla JavaScript (Pure JS) for lightweight, instant page responses (filtering, modal windows).
* *Backend (Server-Side):* * Python 3.x with Django and Django REST Framework (DRF).
  * SQLite (Development) / PostgreSQL (Production).
* *Requirements:* Thin Client architecture requiring only a modern web browser.

## 5. Security & Authorization
System security is implemented across multiple layers:
* *Password Security:* Cryptographically hashed using Django's built-in PBKDF2 algorithm.
* *API Security:* Token-Based Session Management.
* *Role-Based Access Control (RBAC):* * Admin (Superuser): Full database and approval access.
  * Company (is_company=True): Authorized to manage own listings.
  * Student (is_student=True): Authorized to view active postings and apply.
* *Clearance Level System:* Object-Level Permissions ensure only is_active=True and admin-approved jobs are exposed to the public API.

## 6. User Experience and Interface (UX/UI)
* *Student Interface:* Listings are displayed using "Card" designs. Listing details open in fast "Modal Windows" without page refreshes.
* *Company & Admin Interface:* DataTables designs are used for easy management of applications. The overall UI adopts a distraction-free, minimalist corporate approach.

## 7. Licensing and Commercial Model
Operating on a *Freemium B2B SaaS Model*:
* *Students:* 100% free of charge forever.
* *Companies (Basic):* Free registration and limited standard internship listings.
* *Companies (Premium):* Pay-per-post or subscription model for multiple active listings, featured placements, and bulk CV export.

## 8. Installation and Deployment
Steps to set up the backend environment locally:


## 9. UML Diagram
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/f976df78-257b-4401-82c6-83df0be038e0" />

## 10. Risk Matrix
<img width="1872" height="1638" alt="image" src="https://github.com/user-attachments/assets/a62c7b4e-8cd5-4dfc-a81e-4bb621d49894" />

## 11. Pointing System
<img width="790" height="844" alt="pointingsystem" src="https://github.com/user-attachments/assets/fbf16f99-87b6-4a89-b9fb-bb8d112dda16" />

## 12. Live Demo Plan

This section outlines the structured flow of the live demonstration for the Campus Internship System MVP. The demo is designed to take approximately 5-7 minutes.

**Phase 1: Project Management & Agile Workflow**
* Present the GitHub Projects Kanban board.
* Review completed tasks (Frontend UI, Backend Django Models, CI/CD Integration) and backlog items (AWS Deployment, API Hookups).

**Phase 2: Codebase Architecture & CI/CD Automation**
* Showcase the isolated branch structure ensuring decoupled Frontend and Backend environments.
* Demonstrate the GitHub Actions pipeline (`main.yml`) in real-time, highlighting the automated HTML linting and TruffleHog secret scanning processes that secure the codebase.

**Phase 3: User Interface & Experience (Local Simulation)**
* Launch the frontend applications (`login.html`, `student-dashboard.html`, `company-dashboard.html`) locally in the browser.
* Walk through the UX flow for both Student and Company roles, emphasizing the fast modal windows, DataTables integration, and distraction-free corporate design.

**Phase 4: Risk Mitigation & Next Steps**
* Briefly discuss how Git proxy configurations and rebase strategies solved initial network/merge risks.
* Outline the roadmap for the next sprint: Deploying the PostgreSQL database to AWS RDS and hosting the application via ECS.





## 13. Sources

Jira: https://proje1755.atlassian.net/jira/software/projects/SCRUM/boards/1?jql=








