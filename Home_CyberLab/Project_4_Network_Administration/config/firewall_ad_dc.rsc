# ================================================
# ⚙️  LAB FIREWALL CONFIG - AD/DC CORE + EXPANDED
# Target: Windows Server (AD/DC) - 192.168.10.10
# Author: Ediomo Brendan
# Description: Enables required services for AD, DNS, DHCP, GPO, RADIUS, RDP, PKI
# ================================================

# ------------------------------
# ✅ CORE AD SERVICES
# ------------------------------

/ip firewall filter
add chain=forward action=accept protocol=tcp dst-port=53 dst-address=192.168.10.10 comment="✅ Allow DNS TCP to AD/DC"
add chain=forward action=accept protocol=udp dst-port=53 dst-address=192.168.10.10 comment="✅ Allow DNS UDP to AD/DC"
add chain=forward action=accept protocol=udp dst-port=67-68 dst-address=192.168.10.10 comment="✅ Allow DHCP to AD/DC"
add chain=forward action=accept protocol=tcp dst-port=88 dst-address=192.168.10.10 comment="✅ Allow Kerberos (TCP)"
add chain=forward action=accept protocol=tcp dst-port=135 dst-address=192.168.10.10 comment="✅ Allow RPC Endpoint Mapper"
add chain=forward action=accept protocol=tcp dst-port=389 dst-address=192.168.10.10 comment="✅ Allow LDAP TCP"
add chain=forward action=accept protocol=udp dst-port=389 dst-address=192.168.10.10 comment="✅ Allow LDAP UDP"
add chain=forward action=accept protocol=tcp dst-port=445 dst-address=192.168.10.10 comment="✅ Allow SMB TCP (GPO/FileShare)"
add chain=forward action=accept protocol=udp dst-port=445 dst-address=192.168.10.10 comment="✅ Allow SMB UDP (GPO/FileShare)"
add chain=forward action=accept protocol=tcp dst-port=636 dst-address=192.168.10.10 comment="✅ Allow LDAPS (LDAP over SSL)"
add chain=forward action=accept protocol=udp dst-port=636 dst-address=192.168.10.10 comment="✅ Allow LDAPS UDP (if needed)"
add chain=forward action=accept protocol=tcp dst-port=3268 dst-address=192.168.10.10 comment="✅ Allow Global Catalog"

# 🔐 RADIUS (for NPS/802.1X)
add chain=forward action=accept protocol=udp dst-port=1812 dst-address=192.168.10.10 comment="🔐 Allow RADIUS Auth (UDP 1812)"
add chain=forward action=accept protocol=udp dst-port=1813 dst-address=192.168.10.10 comment="🔐 Allow RADIUS Accounting (UDP 1813)"

# 🖥️ Remote Desktop Access
add chain=forward action=accept protocol=tcp dst-port=3389 dst-address=192.168.10.10 comment="🖥️ Allow Remote Desktop (TCP 3389)"

# 🔏 Certificate Services (CA)
# Note: Certificate Services use dynamic RPC ports (49152–65535). You can either open this range or restrict RPC with static ports.
add chain=forward action=accept protocol=tcp dst-port=49152-65535 dst-address=192.168.10.10 comment="🔏 Allow DCOM/RPC High Ports for CA Services"

# 📡 Syslog (Optional)
add chain=forward action=accept protocol=udp dst-port=514 dst-address=192.168.10.10 comment="📡 Allow Syslog UDP"

# ⚙️ Admin Tools (Optional – Windows Admin Center)
add chain=forward action=accept protocol=tcp dst-port=6516 dst-address=192.168.10.10 comment="⚙️ Allow Windows Admin Center (TCP 6516)"

# ================================================
# 🔻 Ensure these rules are placed above DROP rules
# ================================================
