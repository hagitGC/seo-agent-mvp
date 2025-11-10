# Virtual Environment Activation - Windows Solutions

## Problem
PowerShell is blocking script execution for security reasons.

## ✅ SOLUTION 1: Use Command Prompt (Easiest!)

Instead of PowerShell, use Command Prompt (cmd.exe):

```bash
# Open Command Prompt (cmd.exe) in VS Code or Windows Terminal
# Then run:

cd C:\Users\rafi_\Desktop\seo-agent-mvp
.venv\Scripts\activate.bat

# You'll see (.venv) in your prompt
# Now you can use python and pip directly:
python -m uvicorn backend.app.main:app --reload --port 3001
```

## ✅ SOLUTION 2: Don't Activate (Works Perfectly!)

You don't actually need to activate! Just use the full path:

```powershell
# From project root, run commands like this:
.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --port 3001

# Install packages:
.venv\Scripts\pip.exe install package-name

# Check installed packages:
.venv\Scripts\pip.exe list
```

This works perfectly and is actually more explicit about which Python you're using!

## ⚠️ SOLUTION 3: Change PowerShell Policy (Requires Admin)

If you want to enable script execution in PowerShell:

```powershell
# Run PowerShell as Administrator
# Then run:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Confirm with 'Y'
# Close and reopen PowerShell
# Now you can activate:
.venv\Scripts\Activate.ps1
```

## 🎯 RECOMMENDED: Use Solution 1 or 2

Solution 1 (cmd.exe) or Solution 2 (direct path) are safest and easiest!

## ✅ Quick Test

**Command Prompt:**
```cmd
cd C:\Users\rafi_\Desktop\seo-agent-mvp
.venv\Scripts\activate.bat
python --version
```

**PowerShell (without activating):**
```powershell
cd C:\Users\rafi_\Desktop\seo-agent-mvp
.venv\Scripts\python.exe --version
```

Both should show: `Python 3.11.9`

## 🚀 Start Server (Both Ways)

**With activation (cmd.exe):**
```cmd
.venv\Scripts\activate.bat
cd backend
python -m uvicorn app.main:app --reload --port 3001
```

**Without activation (PowerShell):**
```powershell
.venv\Scripts\python.exe -m uvicorn backend.app.main:app --reload --port 3001
```

## 📝 Summary

**You have 3 options:**
1. Switch to cmd.exe (easiest)
2. Use .venv\Scripts\python.exe directly (no activation needed)
3. Change PowerShell execution policy (requires admin)

**Pick the one you're most comfortable with!**
