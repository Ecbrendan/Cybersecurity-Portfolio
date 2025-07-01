# 🛡️ Wazuh Threat Detection Lab - Phase 1

## 📌 Project Overview

This project documents the initial deployment of a centralized threat detection system using **Wazuh**, focusing on core setup, Windows Server integration, and environment preparation for advanced monitoring.

Wazuh provides open-source threat detection, log analysis, and endpoint security capabilities — ideal for practical Blue Team training.

---

## 🚀 Phase 1 Deliverables

✅ Wazuh Manager & Dashboard deployed on **Ubuntu Server**  
✅ Static IP configuration for consistent management access  
✅ Windows Server integrated as a monitored endpoint  
✅ Real-time event collection and verification    

---

## 🖥️ Lab Environment

| Component         | Description                                      |
|-------------------|--------------------------------------------------|
| **Wazuh Manager** | Installed on Ubuntu Server 22.04 (Static IP)    |
| **Wazuh Dashboard** | Version 4.12.0 (latest stable release)        |
| **Windows Server** | Domain Controller with Active Directory        |
| **Wazuh Agent**   | Installed on Windows Server, collecting logs    |
| **Network**       | Private lab subnet: `192.168.10.0/24`           |

---

## 🛠️ Technical Setup Summary

### Wazuh Manager & Dashboard
- Deployed using semi-assisted installation  
- Static IP set for reliability: `192.168.10.20`  
- Verified Wazuh Manager and Dashboard services active  

### Windows Server Integration
- Wazuh Agent installed  
- Configured to communicate with Manager IP  
- Event logs successfully received and displayed in Dashboard  

---

## 🔒 Initial Hardening
- Changed all default passwords (Wazuh VM & Dashboard)  
- Basic firewall rules applied to limit access  
- Environment isolated from production networks  

---

## 📚 Planned Next Steps
- Integrate Sysmon for enhanced Windows visibility  
- Deploy NGINX reverse proxy and implement 2FA for Dashboard access  


---

## 👨‍💻 Why This Lab?
- Builds practical experience with threat detection tools  
- Reinforces Blue Team concepts in a controlled environment  
- Prepares for real-world SOC operations using open-source technology  

---

## 🏁 Conclusion
Phase 1 successfully delivers a functioning Wazuh setup, forming the foundation for advanced monitoring and detection capabilities.

Stay tuned for future updates as I enhance this lab with additional security layers and integrations.

---

## 🔗 Useful Resources
- [Wazuh Documentation](https://documentation.wazuh.com/current/index.html)  
- [Wazuh GitHub](https://github.com/wazuh/wazuh)  