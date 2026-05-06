# Python Skill-Building Exercises 🐍

A collection of focused, single-purpose scripts and CLI tools. Each folder is a standalone exercise targeting a specific Python skill or library — the foundational building blocks behind larger applications.

---

## Exercises

### Email Sender
A CLI script to send emails programmatically via an external SMTP server (Gmail).

**Key Concepts:**
- SMTP interaction using Python's built-in `smtplib`
- MIME-compliant email construction with the `email` module
- Secure authentication using App Passwords
- Credentials management via `.env` files

---

###  Batch Image Processor
A CLI utility that processes a directory of images to generate web-optimized thumbnails and apply watermarks.

**Key Concepts:**
- Image manipulation (resizing, drawing) with `Pillow`
- File system navigation using `pathlib`
- Handling mixed file types and skipping non-image files

---

###  PDF Utility Tool
A multi-function CLI script for PDF manipulation — merging files and applying text watermarks across pages.

**Key Concepts:**
- Reading and writing PDFs with `pypdf`
- Batch processing logic for multiple input files

---

###  Secure Password Checker
Checks if a password has been exposed in a known data breach using the Have I Been Pwned public API.

**Key Concepts:**
- REST API interaction with the `requests` library
- SHA-1 hashing via `hashlib` — only the hash prefix is sent, the full password is never exposed

---

###  SMS Notifier
Sends SMS messages via a third-party gateway (Twilio), demonstrating a standard backend notification pattern.

**Key Concepts:**
- Integration with a PaaS provider
- Using an official client library (`twilio-python`) to call a REST API

---

*(More exercises will be added as they are completed.)*