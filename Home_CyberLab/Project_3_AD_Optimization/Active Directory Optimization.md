# 🛡️ Project 1 – Active Directory Optimization

This project is part of my practical cybersecurity lab setup where I optimized Active Directory (AD) by organizing directory structure, enforcing security policies via Group Policy Objects (GPOs), and applying system-hardening best practices.

## 🏗️ Lab Overview

- **Domain Controller:** Windows Server 2022 Standard
- **Clients:** 2 Windows domain-joined machines
- **Router:** MikroTik RouterOS (gateway)
- **Other Devices:** macOS & Kali (not domain-joined)

## 📁 Organizational Units Created

- `Workstations` – For all domain-joined PCs
- `Servers` – For critical infrastructure machines
- `Users` – For regular domain users
- `Guests` – For limited access accounts

## 🛡️ Group Policies Applied

### 1. Password Policy (Domain Level)
- Minimum length: **12 characters**
- Enforced password history: **24**
- Password complexity: **Enabled**
- Maximum age: **42 days**

### 2. Login Banner (User OU Level)
- Title: `WARNING: Authorized Users Only`
- Message: This system is for the use of authorized individuals only.
        Unauthorized access or use is prohibited and may be subject to disciplinary or legal action.

### 3. Software Restriction Policy (Workstations OU)
- Default security level: **Disallowed**
- Whitelisted:
- `C:\Program Files\*`
- `C:\Windows\*`
- Blocked:
- `%HOMEPATH%\Downloads\*`
- `%USERPROFILE%\AppData\*`

## 🧪 Validation

- Login banner tested and displayed on login
- Password complexity enforced on all user accounts
- Software from Downloads and USB blocked, verified via test executables

## 📸 Screenshots

Stored in `/screenshots/` folder:
- `create_ous.png`
- `gpo_password_policy.png`
- `gpo_login_banner.png`
- `gpo_software_restriction1.png`
- `gpo_software_restriction2.png`

## 📌 Key Skills Demonstrated

- Active Directory structuring
- Group Policy management
- System hardening techniques
- Domain security best practices


## 🧑‍💻 About Me

I’m a cybersecurity analyst building real-world environments to sharpen my skills in infrastructure defense, enterprise administration, and red/blue teaming.

🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/ediomobrendan)  
📂 Explore other projects in my [GitHub Portfolio](https://github.com/Ecbrendan)

---