# 🏠 Cybersecurity Homelab Overview

Welcome to my Cybersecurity Homelab — a fully virtualized lab environment created to simulate real-world enterprise networks, security configurations, and threat scenarios. This lab serves as a platform for hands-on practice, experimentation, and demonstration of cybersecurity concepts and tools.

---

## 🎯 Purpose

This homelab is designed to:

- Build and test secure network architectures
- Explore enterprise technologies like Active Directory, DNS, DHCP, firewalls, and RADIUS
- Practice both defensive and offensive security techniques
- Create portfolio-ready projects and documentation
- Support continuous learning and research in cybersecurity

---

## 🧱 Core Components

### 🔹 Networking
- **MikroTik RouterOS** (used as primary gateway & firewall)
- NAT, static routing, DHCP relay, DNS forwarding

### 🔹 Server Infrastructure
- **Windows Server 2022**
  - Active Directory Domain Services (AD DS)
  - DHCP & DNS Server
  - Group Policy Management
  - Kerberos & RADIUS authentication

### 🔹 Clients & Tools
- **Windows 10 Clients** (domain-joined for policy testing)
- **Kali Linux** (penetration testing, scanning, auditing)
- **macOS** (for diversity and client behavior testing)

---

## 🗺️ Network Overview
![image](https://github.com/user-attachments/assets/b15bd8db-ce0a-45b3-9aaf-1b5b7465f1c0)


## 📦 Lab Features

- Virtualized on **VMware Workstation**
- Internal network segmentation and traffic control
- Internet access via NAT through MikroTik
- All systems communicate within a lab-only subnet

---

## 🔐 Focus Areas

- Active Directory Security
- GPO Implementation
- DHCP/DNS Management
- Firewall Rules & NAT
- Identity & Access Control (IAM)
- Offensive Security Testing
- Network Traffic Analysis

---

👨‍💻 Maintainer
Ediomo Brendan
Cybersecurity Analyst
