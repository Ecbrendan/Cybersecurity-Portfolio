# 🛡️ OPNsense Migration & RADIUS Integration

This project showcases a real-world migration from MikroTik to OPNsense firewall, with complete integration of Windows Server for DHCP, DNS, and RADIUS authentication — all within a subnet-based architecture for lab segmentation and policy enforcement.

---

## 🧭 Network Architecture

| Subnet          | Purpose                        | Gateway          |
|---------------- |--------------------------------|------------------|
| 192.168.10.0/24 | Domain-joined clients          | OPNsense LAN     |
| 192.168.20.0/24 | Unjoined devices (Kali/macOS)  | OPNsense OPT1    |

- OPNsense routes traffic and enforces firewall policies
- Windows Server (192.168.10.10) handles DHCP, DNS, and NPS (RADIUS)
- DHCP is relayed from OPNsense to Windows Server

---

## ✅ Migration Highlights

- Replaced MikroTik with OPNsense (VM on VMware)
- Configured OPNsense LAN (192.168.10.1) and OPT1 (192.168.20.1)
- Enabled DHCP Relay to Windows Server
- Set up RADIUS server on OPNsense pointing to Windows NPS
- Added fallback to local database to avoid lockouts
- Mapped AD users to web UI access on OPNsense

---

## 🔐 Admin Authentication

- Domain users (via RADIUS) can access OPNsense Web UI securely
- Access controlled by NPS policies (Windows Server)
- Local `root` user retained as fallback
---

## 🧪 Test Matrix

| Test                             | Result           |
|----------------------------------|----------------  |
| Web UI login (RADIUS)            | ✅ Success      |
| Local root login                 | ✅ Success      |
| DHCP IP allocation via relay     | ✅ Working      |
| Inter-subnet communication       | ✅ Routed       |
| DNS & Internet access            | ✅ Functional   |

---

## 🔧 Tech Stack

- 🖥️ OPNsense (Firewall & DHCP Relay)
- 🧱 Windows Server 2022 (AD, DNS, DHCP, NPS)
- 💻 VMware Workstation
- 🔄 Subnet Segmentation (No VLANs used)

---

## 📸 Screenshots & Configs

Screenshots are stored under the `/screenshots` folder.

---

## 🤝 License

This project is open-source for educational use.

---

## 🌐 Connect

If you found this useful, connect with me on [LinkedIn](https://www.linkedin.com/in/ediomobrendan)

---
