# Python Skill-Building Exercises 🐍

This repository is my "developer sketchbook"—a collection of focused, single-purpose scripts and command-line tools. Each folder contains a standalone exercise designed to master a specific, industry-relevant Python skill or library.

While my main portfolio consists of larger, multi-file applications, these exercises demonstrate the foundational building blocks and practical automation tasks that are essential for any software developer.

---

## Scripts & Exercises

Here is a list of the exercises contained in this repository.

### 📧 Email Sender
A command-line script to programmatically send emails using an external SMTP server (like Gmail). This project focuses on secure authentication and protocol interaction.

* **Key Concepts Mastered:**
    * Interacting with the SMTP protocol using Python's built-in `smtplib`.
    * Constructing MIME-compliant emails with the `email` module.
    * **Secure Authentication:** Using **App Passwords** instead of primary account passwords, a critical security best practice.
    * **Secrets Management:** Loading credentials safely from a `.env` file to keep them out of the source code.

### 🖼️ Batch Image Processor
A command-line utility that processes a directory of images to generate web-optimized thumbnails and apply watermarks. This mimics a core task in backend web development for handling user-uploaded media.

* **Key Concepts Mastered:**
    * Image manipulation (resizing, drawing) with the **`Pillow`** library.
    * Modern file system navigation and path manipulation using `pathlib`.
    * Handling different file types and gracefully skipping non-image files.

### 📄 PDF Utility Tool
A multi-functional command-line script for manipulating PDF documents, including merging multiple files into one and applying a text watermark to every page.

* **Key Concepts Mastered:**
    * Reading and writing a complex binary file format using the **`pypdf`** library.
    * Batch processing logic to handle multiple input files.

### 🔐 Secure Password Checker
A security-focused script that checks if a password has been exposed in a known data breach by securely interacting with the "Have I Been Pwned" public API.

* **Key Concepts Mastered:**
    * Interacting with an external REST API using the `requests` library.
    * **Hashing Fundamentals:** Using the `hashlib` module to hash a password with **SHA-1** before sending its prefix to the API, ensuring the full password is never exposed.

### 📱 SMS Notifier
A script to send SMS messages to a phone number using a professional third-party SMS gateway service like Twilio. This demonstrates a core backend skill for sending user notifications.

* **Key Concepts Mastered:**
    * Integrating with a major PaaS (Platform as a Service) provider.
    * Using an official client library (e.g., `twilio-python`) to interact with a REST API.

---
*(More exercises will be added here as they are completed...)*