# 🎾 Sports Club Management System
### Powered by Django & Supabase

A sports club management platform built using the **PostgreSQL Exercises (pgexercises.com)** schema. This project simulates a real-world business environment for managing members, facility bookings, and revenue tracking.

---

## 🚀 Overview
This project transforms the static "ClubData" dataset into a full-stack Django application.

### Key Features
* **Facility Booking:** Real-time scheduling for tennis courts, massage rooms, and squash courts.
* **Revenue Analytics:** Automated calculation of monthly income per facility, distinguishing between member and guest costs.
* **Member Directory:** Management of member profiles, including a hierarchical recommendation system.

---

## 🛠️ Tech Stack
* **Backend:** Django (Python 3.x)
* **Database:** PostgreSQL (Hosted via **Supabase**)
* **Deployment:** Render

---

## 📊 Database Schema
The project is built on three core entities:
1.  **Members:** Names, addresses, and referral links.
2.  **Facilities:** Details on costs and maintenance for 9 different club areas.
3.  **Bookings:** The transactional layer linking members to facilities with specific time slots.
