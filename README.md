# MentorLink

A student-to-tutor booking platform built with **Django** and **Django REST Framework**, with a **React** frontend.

Students browse tutors and subjects, request an available slot, and manage their own bookings. Tutors manage their profile, availability and booking status.

> **Status:** In active development. The backend foundation (project shell and apps) is in place; models, API and frontend are being built session by session.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Getting Started](#getting-started)
- [Roadmap](#roadmap)
- [Scope](#scope)

---

## Features

**Students**
- Browse tutors and filter by subject
- View a tutor's profile and upcoming availability
- Request a slot and add a note
- View, edit and cancel their own bookings

**Tutors**
- Manage their profile and subjects
- Publish and update availability slots
- Confirm, cancel or complete bookings for their own slots

**Platform**
- Role-based accounts (student / tutor) on a custom user model
- Ownership enforced server-side: users can only access their own records
- Validation that prevents double-booking a slot
- Django Admin for managing all data

---

## Tech Stack

| Layer     | Technology                          |
| --------- | ----------------------------------- |
| Backend   | Python, Django 6                    |
| API       | Django REST Framework (planned)     |
| Frontend  | React + Vite (planned)              |
| Database  | SQLite (dev), PostgreSQL (planned)  |

---

## Project Structure

```
mentorlink/
├── backend/
│   ├── core/        # Project configuration: settings, root URLs, WSGI/ASGI
│   ├── accounts/    # Custom user model, authentication
│   ├── tutors/      # Tutor profiles, subjects, availability slots
│   ├── bookings/    # Booking requests and status lifecycle
│   └── manage.py
├── frontend/        # React app (added in the React phase)
└── README.md
```

---

## Data Model

```
CustomUser (student | tutor)
    └── TutorProfile            (OneToOne)
            ├── Subject         (ManyToMany)
            └── AvailabilitySlot (ForeignKey)

Booking
    ├── student → CustomUser        (ForeignKey)
    └── slot    → AvailabilitySlot  (ForeignKey)
```

Booking statuses: `pending`, `confirmed`, `cancelled`, `completed`.

---

## Getting Started

**Prerequisites:** Python 3.12+ and Git.

```bash
# Clone the repository
git clone https://github.com/Al-Farhan-Seg/mentorlink.git
cd mentorlink/backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install django

# Apply migrations and create an admin user
python manage.py migrate
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```

The app is then available at `http://127.0.0.1:8000/`, with the admin at `/admin/`.

---

## Roadmap

| Phase | Focus                                                        | Status      |
| ----- | ------------------------------------------------------------ | ----------- |
| 0     | Workspace, apps, project map                                 | In progress |
| 1–2   | Data design, models and migrations                           | Planned     |
| 3–6   | Admin, minimal pages, ORM queries, booking validation        | Planned     |
| 7–8   | Authentication, ownership, booking statuses, tests           | Planned     |
| 9–14  | DRF: serializers, booking CRUD, viewsets, permissions, pagination | Planned |
| 15–17 | React UI: data fetching, booking flow, login                 | Planned     |
| 18    | PostgreSQL, README polish, separate frontend/backend deploy  | Planned     |

---

## Scope

Version 1 deliberately stays small. The following are **out of scope**: payments, real-time chat, email notifications, calendar sync and maps.

The goal is to practise models, validation, ownership, API design and React integration end to end.
