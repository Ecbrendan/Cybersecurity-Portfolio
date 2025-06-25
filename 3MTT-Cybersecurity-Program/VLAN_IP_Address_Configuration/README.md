# VLAN Segmentation & Inter-VLAN Routing with Cisco Packet Tracer

## Overview
This project demonstrates how to implement VLAN segmentation and Inter-VLAN Routing using Cisco Packet Tracer to enhance network organization, security, and performance.

Through this lab, I configured VLANs, assigned IP addresses, and established inter-VLAN communication using a Router-on-a-Stick setup, simulating real-world enterprise networking.

---

## Lab Objectives

- Create two VLANs for network segmentation:
  - VLAN 10: Administrative Traffic
  - VLAN 20: Guest Traffic
- Assign devices to appropriate VLANs
- Configure static IP addresses within each VLAN
- Enable Inter-VLAN Routing using router sub-interfaces
- Verify communication within and across VLANs

---

## Tools & Environment

- Cisco Packet Tracer
- Cisco Switch
- Cisco Router
- 6 End Devices
- CLI commands for Switch & Router configuration

---

## Network Design

```
                  +---------------------+
                  |      Cisco Router    |
                  | 192.168.10.1 (VLAN10)|
                  | 192.168.20.1 (VLAN20)|
                  +----------+----------+
                             |
                    Trunk Link (Dot1Q)
                             |
                 +----------------------+
                 |    Cisco Switch      |
                 +----------------------+
              VLAN 10 Ports    VLAN 20 Ports
              PC1, PC2, PC3    PC4, PC5, PC6
```

---

## IP Addressing Scheme

| Device  | VLAN | IP Address      | Subnet Mask      | Default Gateway |
|---------|------|-----------------|------------------|-----------------|
| PC1     | 10   | 192.168.10.2    | 255.255.255.0    | 192.168.10.1    |
| PC2     | 10   | 192.168.10.3    | 255.255.255.0    | 192.168.10.1    |
| PC3     | 10   | 192.168.10.4    | 255.255.255.0    | 192.168.10.1    |
| PC4     | 20   | 192.168.20.2    | 255.255.255.0    | 192.168.20.1    |
| PC5     | 20   | 192.168.20.3    | 255.255.255.0    | 192.168.20.1    |
| PC6     | 20   | 192.168.20.4    | 255.255.255.0    | 192.168.20.1    |

---

## Step-by-Step Configuration

### 1. VLAN Creation & Port Assignment (Switch)


enable
configure terminal
vlan 10
 name admin-traffic
vlan 20
 name guest-traffic

interface range FastEthernet0/1
 switchport mode access
 switchport access vlan 10

interface range FastEthernet0/2
 switchport mode access
 switchport access vlan 10

interface range FastEthernet0/3
 switchport mode access
 switchport access vlan 10

interface range FastEthernet0/4
 switchport mode access
 switchport access vlan 20

interface range FastEthernet0/5
 switchport mode access
 switchport access vlan 20

interface range FastEthernet0/6
 switchport mode access
 switchport access vlan 20

interface FastEthernet0/24  (This is connect to the router)
 switchport mode trunk      

---

### 2. Router Configuration - Router-on-a-Stick

enable
configure terminal

interface GigabitEthernet0/0/0
 no shutdown

interface GigabitEthernet0/0/0.10
 encapsulation dot1Q 10
 ip address 192.168.10.1 255.255.255.0

interface GigabitEthernet0/0/0.20
 encapsulation dot1Q 20
 ip address 192.168.20.1 255.255.255.0

### 3. PC Static IP Configuration

On each PC (via Packet Tracer Desktop > IP Configuration):

- VLAN 10 PCs:
  - IP Range: 192.168.10.2 to 192.168.10.4
  - Gateway: 192.168.10.1

- VLAN 20 PCs:
  - IP Range: 192.168.20.2 to 192.168.20.4
  - Gateway: 192.168.20.1

---

## Verification & Testing

**Intra-VLAN Ping (VLAN 10)**

PC1> ping 192.168.10.3

**Inter-VLAN Ping (VLAN 10 to VLAN 20)**

PC1> ping 192.168.20.2

**TraceRoute Example**

PC1> tracert 192.168.20.2

---

## Outcome & Key Learnings

- Effective network segmentation using VLANs
- Successful Inter-VLAN Routing with sub-interfaces
- Hands-on experience configuring Layer 2 and Layer 3 devices
- Understanding traffic isolation and controlled communication

---

## Conclusion

This project reinforces core networking concepts of VLANs, IP management, and router-based traffic control. These skills are essential for building scalable, secure enterprise networks.
