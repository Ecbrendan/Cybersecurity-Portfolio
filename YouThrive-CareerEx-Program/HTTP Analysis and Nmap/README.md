# Network Security Assignment 

This repository contains my network security assignment, which includes packet capture and Nmap network scanning.

## Task 1: Packet Capture & Protocol Comparison Using Wireshark
- Captured HTTP and HTTPS traffic to observe the difference between plaintext and encrypted data.
- Included screenshots showing the username and password from an HTTP site (in plaintext) and an HTTPS site (encrypted).

 ## Steps Taken

  Open Wireshark and start a capture on your Wi-Fi or Ethernet interface.

  Visit: http://testphp.vulnweb.com

  Go to the login page.

  Input a dummy username and password.

  Use the filter http.request.method == "POST" to identify packets with login information.

  Click the relevant packet → Expand Hypertext Transfer Protocol section → Locate and screenshot the username and password in plain text.
  
  Extract the username and password in plaintext from the HTTP request.

  Repeat the process with an HTTPS website but with TLS filter to observe the encrypted request.

## Task 2: Nmap Network Scanning and Analysis
- Conducted an Nmap scan on a public website to detect open ports, services, versions, and operating system details.
Nmap Commands:

Service Detection: nmap -sV <website URL>

Version Detection (Intensive): nmap -sV --version-intensity 9 <website URL>

Operating System Detection: nmap -O <website URL>

Analyze the scan results and identify open ports, services, versions, and operating system details.


### Disclaimer:
- Ethical hacking and responsible usage of cybersecurity tools were strictly adhered to in this assignment.
