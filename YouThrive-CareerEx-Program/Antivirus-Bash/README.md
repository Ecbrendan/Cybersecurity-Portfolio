# Antivirus&Bash
### 📌 Overview of Tasks

1. ✅ Create an antivirus test file using the EICAR standard
2. ✅ Write a Bash script to shut down a Linux system
3. ✅ Install Kali Linux inside a VMware virtual machine
4. ✅ Share the experience in a professional LinkedIn post


##### 1️⃣ EICAR Test File – Antivirus Testing

##### 🔍 Description:
The [EICAR test string](https://www.eicar.org/?page_id=3950) is a harmless file designed to test the response of antivirus software.

##### 📄 File: [`eicar_test_file.txt`](./eicar_test_file.txt)
This file is a `.txt` version of the standard `eicar.com` test file to avoid automatic antivirus flags or GitHub restrictions.

##### 🧪 How to Test:
1. Copy and paste this string into a text editor:
X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*

2. Save as `eicar.com`
3. Your antivirus should immediately detect and quarantine it

---

## 2️⃣ Bash Script – Power Off System

##### 📜 File: [`shutdown.sh`](./shutdown.sh)
A basic Bash script that powers off the system.

Note: Requires sudo privileges.

#!/bin/bash
echo "Shutting down system in 60s!!!..."
sudo shutdown

#### ▶️ How to Use:
Open terminal in Linux

Create file:
nano shutdown.sh

Paste the script and save (Ctrl + O, then Ctrl + X)
Make it executable:

chmod +x shutdown.sh
Run it:

./shutdown.sh

## 3️⃣ Installing Kali Linux in VMware
##### 🧰 Tools Used:
VMware Workstation Pro
Kali Linux ISO

🛠️ Steps Followed:
1. Download VMware Workstation Pro from the official VMware site and install it on your system.

2. Download the Kali Linux ISO file from the official Kali Linux website (https://www.kali.org/get-kali/). Choose the “Installer” ISO, not the prebuilt VM.

3. Open VMware Workstation Pro after installation.

4. Click on "Create a New Virtual Machine" or go to File > New Virtual Machine.

5. Select "Typical (recommended)" and click Next.

6. Choose "Installer disc image file (iso)", then click Browse and locate your Kali Linux ISO file. Click Next.

7. Select the Guest Operating System:
    OS: Linux
    Version: Debian 11.x or later (64-bit) (since Kali is Debian-based)
    Click Next

8. Enter a name for the VM (e.g., “Kali Linux”) and choose the location where the VM files will be saved. Click Next.

9. Specify the Disk Capacity:
    Maximum disk size: e.g., 40 GB
    Select "Store virtual disk as a single file" for better performance.
   Click Next

9. Click Customize Hardware:
  Memory (RAM): Set at least 4GB (4096 MB) or more.
  Processors: Allocate 2 processors or more.
  Network Adapter: Set to Bridged or NAT, depending on your network setup.
  Optional: Add a USB controller, sound card, or printer.
  Click Close when done.

10. Click Finish to create the VM.

11. Power on the VM by clicking “Power on this virtual machine.”

12. Kali Linux installer will boot. On the menu, select “Graphical Install” and press Enter.

13. Choose your preferred language, then click Continue.

14. Select your location (country), then click Continue.

15. Choose your keyboard layout, then click Continue.

16. Kali will begin detecting hardware and loading components. Wait for it to finish.

17. Enter a hostname for the system (e.g., kali), then click Continue.

18. Leave the domain name blank (unless you're part of a domain), click Continue.

19. Set up the user account:
    Full name: Enter your name
    Username: Enter a short login name (e.g., kaliuser)
    Password: Set and confirm a secure password
    Click Continue

20. Set your time zone, then click Continue.
    For partitioning:
    Choose Guided - use entire disk
    Select your virtual disk (should be the only one listed)
    Choose All files in one partition (recommended)
    Select Finish partitioning and write changes to disk
    Confirm by selecting Yes to write the changes
    Click Continue

21. Kali will begin installing the base system — this might take several minutes.

22. When prompted about a network mirror, select Yes to allow downloading of extra packages, then click Continue.

23. If using a proxy, enter it (optional), otherwise leave blank and click Continue.

24. Wait for the package manager to finish configuration.

25. Select Yes to install the GRUB boot loader to the master boot record (MBR), then click Continue.

26. Choose the disk to install GRUB (usually /dev/sda), then click Continue.

27. Kali will finish installation. Once done, select Continue to reboot the VM.

28. On reboot, Kali will boot into the login screen. Use your username and password to log in.

29. After logging in, you’re now inside Kali Linux. Open a terminal and update your system:
    ##### sudo apt update && sudo apt upgrade -y


## 4️⃣ LinkedIn Post
#### 🌐 Shared My Experience:
I created a LinkedIn post summarizing the assignment, key learnings, and screenshots.

🔗 View my LinkedIn post here
https://www.linkedin.com/posts/ediomobrendan_cybersecurity-bash-kalilinux-activity-7314026742619299840-nLsp?utm_source=share&utm_medium=member_desktop&rcm=ACoAAAygdu8BiXuSfUFd4QGhYv_lwwCi0957EfM
