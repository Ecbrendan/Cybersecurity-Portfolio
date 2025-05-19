; === Assign Static IP to LAN Interface (ether2) ===
/ip address add address=192.168.10.1/24 interface=ether2

; === Enable DHCP Client on WAN Interface (ether1) ===
/ip dhcp-client add interface=ether1 disabled=no

; === Set Up DHCP Server on LAN Interface ===
/ip dhcp-server setup

; === Add NAT Rule to Enable Internet Access ===
/ip firewall nat add chain=srcnat out-interface=ether1 action=masquerade
