# 🎯 MikroTik DHCP Relay & RADIUS Authentication Lab

This lab simulates a production-style setup where a centralized Windows Server DHCP allocates IP addresses across Subnets, and MikroTik RouterOS uses RADIUS authentication (via NPS + Active Directory) for admin logins.

## 📡 Network Overview

| Segment         | Subnet            | VMnet   | MikroTik Interface  | Gateway IP     |
|-----------------|-------------------|---------|---------------------|----------------|
| Subnet10 (Server) | 192.168.10.0/24   | VMnet2  | ether2              | 192.168.10.1   |
| Subnet20 (Client) | 192.168.20.0/24   | VMnet3  | ether3              | 192.168.20.1   |

- DHCP Server IP: `192.168.10.10`
- Clients (Kali/macOS) on VMnet3 receive IPs via DHCP relay.
- MikroTik authenticates admin access via Active Directory using NPS (RADIUS).

---

## ⚙️ Lab Components

### ✅ DHCP Relay from MikroTik to Windows Server

- MikroTik relays DHCP requests to `192.168.10.10`
- Windows Server handles DHCP Scope for Subnet20:
  - **Range:** 192.168.20.50–100
  - **Router:** 192.168.20.1
  - **DNS:** AD server

### ✅ RADIUS Authentication for MikroTik Login

- NPS on Windows Server authenticates MikroTik logins
- Domain Admins group used for access control
- Auth method: MS-CHAPv2
- MikroTik RADIUS config:
  - Service: `login`, `ppp`
  - Server: `192.168.10.10`
  - Secret: _defined manually_

---

## 📁 Files Included

- `screenshots/`: Visuals and screenshots
- `docs/`: Walkthrough of the full lab setup and testing steps

---

## 🧪 Verification Steps

- ✅ Devices on Subnet20 receive IPs from Server
- ✅ RADIUS-authenticated login works on MikroTik (WebFig, Winbox, SSH)
- ✅ Inter-Subnet communication succeeds with firewall rules
- ✅ Windows Server is domain-joined and handles DHCP + NPS roles

---

## 🔒 Key Learning Outcomes

- Real-world understanding of inter-VLAN IP assignment using DHCP relay
- Integration of AAA (Authentication, Authorization, Accounting) using NPS
- Centralized login control for network infrastructure using Active Directory

---

## 🛠 Tools Used

- VMware Workstation
- MikroTik RouterOS
- Windows Server 2022 (AD + DHCP + NPS roles)
- Kali Linux, macOS (Clients)

---

## 🌐 Connect

If you found this useful, connect with me on [LinkedIn](https://www.linkedin.com/in/ediomobrendan)

---

## 📌 Tags

`#Cybersecurity` `#WindowsServer` `#MikroTik` `#DHCPRelay` `#RADIUS` `#ActiveDirectory` `#NPS` `#VMwareLab` `#Homelab` `#NetworkSecurity`