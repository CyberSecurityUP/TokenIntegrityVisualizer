# 🛡️ Token & Integrity Visualizer

**Author**: Joas A Santos

## 📌 Overview

**Token & Integrity Visualizer** is a Windows-focused security tool designed for red teamers, blue teamers, and system administrators.
It provides deep insights into process tokens, privileges, integrity levels, and access controls, and visualizes the relationships between processes and their security contexts.

Unlike traditional token viewers, this tool includes:

* A **graph-based visualization** of process-to-privilege mappings.
* Integration with **MITRE ATT\&CK techniques** for better contextualization.
* A **business impact mapping** to translate technical risks into real-world consequences.

---

## ⚙️ Features

* Enumerates running processes and inspects:

  * Security Identifiers (SIDs).
  * Enabled and disabled privileges.
  * Integrity Levels.
  * Effective Access Control Lists (ACLs).

* Maps privileges to **business impact** and **MITRE ATT\&CK techniques**.

* Generates both:

  * A static **PNG privilege graph** (for quick visualization inside the GUI).
  * An interactive **HTML graph** (movable, zoomable, and clickable).

* GUI built with **Tkinter** for usability.

---

## 🖥️ GUI Views

* **Processes & Tokens** → Lists all processes with detailed token information.
* **Privilege Graph** → Visualizes relationships between processes and privileges.

  * *Static PNG graph*: displayed in the application.
  * *Interactive HTML graph*: opens in a browser for full exploration.

---

## 📦 Requirements

Make sure you have **Python 3.10+** and install the following dependencies:

```bash
pip install pywin32 psutil networkx matplotlib pyvis pillow
```

---

## 🚀 Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/CyberSecurityUP/TokenIntegrityVisualizer.git
   cd TokenIntegrityVisualizer
   ```
2. Run the application:

   ```bash
   python main.py
   ```
3. In the GUI:

   * Use **Refresh** in *Processes & Tokens* to scan processes.
   * View privilege graphs in the *Privilege Graph* tab.
   * Use **Open Interactive Graph** to explore relationships dynamically in your browser.

---

## 📊 Example Output

### Token Information

```
PID: 6316 | Name: RuntimeBroker.exe
SID: S-1-5-21-2297296664-725062798-3513451955-1000
  SeDebugPrivilege (Enabled=True) → Potential credential theft
    MITRE: T1003.001 (Credential Access)
  SeImpersonatePrivilege (Enabled=False) → Lateral movement risk
    MITRE: T1134.001 (Privilege Escalation)
```

### Graph Visualization

* **Green nodes** = Processes.
* **Blue nodes** = Privileges.
* **Edges** = Enabled privilege relations.

---

## 🔒 Security Note

This tool requires elevated privileges (Administrator or SYSTEM) for complete results. Running without them will limit access to certain token data.

---

## 📖 Credits

Developed by **Joas A Santos**.
Inspired by real-world offensive and defensive security operations.
