# Network Administration – Cybersecurity Lab

This project showcases the design, configuration, and optimization of core network services and security controls within a controlled cybersecurity lab. The lab includes a MikroTik router, Windows Server 2022 (AD, DNS, DHCP), two AD-joined Windows clients, and non-domain macOS and Kali Linux systems.

---

## 🔧 DHCP & DNS Optimization

### Goals:
- Assign static IPs via DHCP reservations for Kali.
- Enable dynamic DNS registration and updates for Windows AD clients.
- Configure and route internal DNS queries through Windows Server from MikroTik.
- Enforce secure communication between clients and the AD.

### 🛠️ Implemented:
- 🎯 DHCP reservations with MAC/IP bindings.
- 🧠 Dynamic DNS integration using Windows Server.
- 🌐 Set **DNS forwarding** in MikroTik to point to the domain controller (`192.168.10.10`).
- ✅ Firewall rules to allow essential AD/DC ports.

### 📸 Screenshots:
- DHCP reservations
- MikroTik DNS forwarding rule
- nslookup tests
- DHCP reservation for Kali
- Dynamic DNS update verification

## 🗂️ Folder Contents

- `screenshots/`: Visuals of DHCP and DNS configurations
- `config/`: Sample configuration export (`.rsc`) of settings
- `docs/`: Setup manual

---

## 💡 Tools Used
- 🖥️ Windows Server 2022
- 🌐 MikroTik RouterOS
- 🐧 Kali Linux
- 📸 Winbox, WebFig nslookup for verification


## 🧑‍💻 About Me

I’m a cybersecurity analyst building real-world environments to sharpen my skills in infrastructure defense, enterprise administration, and red/blue teaming.

🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/ediomobrendan)  
📂 Explore other projects in my [GitHub Portfolio](https://github.com/Ecbrendan)

---

