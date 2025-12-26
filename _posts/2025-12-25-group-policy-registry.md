---
title: "The Group Policy and The Registry"
date: 2025-12-25 
categories: [Tutorial, Tweak]
tags: [group policy, registry, powershell, .reg file]
image: /assets/img/2025-12-25/group-policy-registry.jpg
---


## 📜 Group Policy vs ⚙️ Registry

whenever we face some problems we search in the internet and probably found solution that involve editing particular group policy or changing registry values. Some times we found easy method .reg file just double clicking on it and problem solved or powershell command that we blindly execute to solve the problem.

## What they ae actually?

In short, the **Group Policy** and the **Registry Editor** are tools used for tweaking system configuration.Group Policy functions as a user-friendly management layer that ultimately writes its settings to the Windows Registry. Most Group Policy settings are just "Administrative Templates" for specific Registry keys. When we "Enable" a policy in the **Local Group Policy Editor** , Windows creates the corresponding Registry entry automatically.

- Group Policy is like a friendly interface that sets rules.
- Under the hood, those rules are stored as Registry keys/values.
- That’s why changing a GPO often results in a new entry under 'HKLM\Software\Policies' or 'HKCU\Software\Policies'.

## The Enforcement Order: Preference

If a setting is configured in both tools, Group Policy generally takes precedence. This means if you change a Registry key manually, but a GPO says otherwise (not the *not configured state*), the system will eventually revert your change back to the GPO's value during its next refresh cycle. Then the question arises what if I change a registry value while group policy untouched, then since group policy has higher preference, registry settings should be revert back, the answer is in next paragraph.

## The "Not Configured" State

Most Group Policy settings are set to **"Not Configured state"** by default. In this state, the Group Policy engine ignores that specific Registry key entirely. It does not "hold" an old value; it simply doesn't send any instructions to the Registry, allowing your manual changes persist.

## What goes Where: Architecture of Registry and Group Policy

Confused to see the registry entry? here is the explanation.
🗂 **Windows Registry Architecture**
Think of the Registry as a hierarchical database (like folders and files, but for settings).

- `Root Hives` (top-level containers):
- `HKEY_LOCAL_MACHINE` (HKLM) → Machine-wide settings (applies to all users).
- `HKEY_CURRENT_USER` (HKCU) → Settings for the logged-in user.
- `HKEY_CLASSES_ROOT` (HKCR) → File associations and COM objects.
- HKEY_USERS (HKU) → Profiles for all users on the system.
- HKEY_CURRENT_CONFIG (HKCC) → Hardware profile currently in use.
- Keys and Values:
- Keys = folders.
- Values = actual settings (strings, numbers, binary).
- Example: HKCU\Software\Microsoft\Windows\CurrentVersion\Explorer controls Explorer behavior.






## Accessing the Registry

To access or modify the Registry, you need to use the **Registry Editor**.

- Type `win+R` to open run box and type 'regedit' Registry editor will open.
- ![Run Box](/assets/img/2025-12-25/run-regedit.png)
![Registry Editor](/assets/img/2025-12-25/registry-editor.png).
- Alternatively search in the start menu with reistry ![Regitry Editor](/assets/img/2025-12-25/registry-startmenu.png).
- Even you can use 3d part registry editor [Registry Finder](https://registry-finder.com/) which has some handy features. ![Registry Finder](/assets/img/2025-12-25/registry-finder.png)
- Command Prompt
