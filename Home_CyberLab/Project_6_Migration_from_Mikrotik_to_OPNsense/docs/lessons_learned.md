# 🧩 Snapshot Recovery Saved My Lab – Twice

## Background

During the migration of my cybersecurity lab from MikroTik to **OPNsense**, I implemented **RADIUS-based authentication** for admin login using **Windows Server NPS**. Everything was working fine — until one misconfiguration caused a complete lockout.

## The First Lockout: A Hard Reset

- Misconfigured the RADIUS authentication chain.
- Lost access to both:
  - **Web GUI**
  - **Console login**
- No snapshot existed at the time.
- Result: Had to **completely remove and reinstall OPNsense** from scratch.
- Painful reset, but a powerful lesson.

## The Second Lockout: Snapshot to the Rescue

- After learning the lesson the hard way, I took **a snapshot before the next RADIUS test**.
- Misconfigured again (in development mode).
- Got locked out again.
- This time, I simply **restored the snapshot**, and everything was back in under 2 minutes.

---

## 🔁 Lessons Learned

Here are the practical takeaways for anyone configuring RADIUS, 802.1X, or working with firewall authentication in lab or production environments:

### ✅ Snapshot Discipline
- Take a **VM snapshot before any authentication-related changes** (RADIUS, 802.1X, login restrictions).
- Label snapshots clearly by purpose and date.

### ✅ Preserve a Local Admin Account
- Always keep **at least one local admin login** with full GUI/console access.
- Don’t tie *all* login access to RADIUS until you've tested it thoroughly.

### ✅ Test in Phases
- Start with **monitor or test mode**, not full enforcement.
- Confirm RADIUS/NPS is working with minimal scope before locking down access.

### ✅ Backup NPS Configurations Too
- Export NPS policies as templates to quickly recover or reimport settings.

### ✅ Write Access Policies Down
- Maintain a config log for each service tied to authentication (e.g., shared secrets, user groups, IP bindings).

### ✅ Use the Console Cautiously
- Don’t assume console access will override GUI issues — if RADIUS is enabled globally, it may block console login too.

### ✅ Enable SSH, if not already
- SSH can offer a fallback option for some CLI access, though it too can be tied to RADIUS (with risk).

---

## 📌 Moral of the Story

> In cybersecurity labs, **resilience isn't just defense — it's recovery.**

A well-timed snapshot can save hours of frustration. Backup isn't optional — it's your parachute.

