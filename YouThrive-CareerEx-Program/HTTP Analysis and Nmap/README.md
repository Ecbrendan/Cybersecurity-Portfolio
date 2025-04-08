# Network Security Assignment

This repository contains my network security assignment, which includes packet capture and Nmap network scanning.

## Task 1: Packet Capture & Protocol Comparison Using Wireshark
### Overview:
In this task, I captured both HTTP and HTTPS traffic to observe the difference between plaintext and encrypted data. I included screenshots showing the username and password from an HTTP site (in plaintext) and an HTTPS site (encrypted).

### Steps Taken:
1. Open Wireshark and start a capture on your Wi-Fi or Ethernet interface.
2. Visit: [http://testphp.vulnweb.com](http://testphp.vulnweb.com)
3. Go to the login page.
4. Input a dummy username and password.
5. Use the filter `http.request.method == "POST"` to identify packets with login information.
6. Click the relevant packet → Expand the Hypertext Transfer Protocol section → Locate and screenshot the username and password in plain text.
7. Extract the username and password in plaintext from the HTTP request.
8. Repeat the process with an HTTPS website but with the `TLS` filter to observe the encrypted request.

### Deliverable:
- **Screenshots**:
  - HTTP packet showing credentials in plaintext.
  - HTTPS packet showing encrypted credentials.

## Task 2: Nmap Network Scanning and Analysis
### Overview:
For this task, I conducted an Nmap scan on a public website to detect open ports, services, versions, and operating system details.

### Nmap Commands:
1. **Service Detection**: `nmap -sV <website URL>`
2. **Version Detection (Intensive)**: `nmap -sV --version-intensity 9 <website URL>`
3. **Operating System Detection**: `nmap -O <website URL>`

### Results:
- Identified open ports
- Detected services running on each port
- Gathered version information for the services
- In some cases, detected the operating system and version

### Deliverable:
- **Screenshots** of Nmap terminal outputs.

## Disclaimer:
Ethical hacking and responsible usage of cybersecurity tools were strictly adhered to in this assignment.
