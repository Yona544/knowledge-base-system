@echo off
setlocal ENABLEEXTENSIONS ENABLEDELAYEDEXPANSION

rem stop_mcp_sse.bat [port]
rem Kills any process listening on the specified port (default: %MCP_SERVER_PORT% or 3000)

set PORT=%1
if "%PORT%"=="" set PORT=%MCP_SERVER_PORT%
if "%PORT%"=="" set PORT=3000

echo Stopping MCP SSE server (port %PORT%)...

set KILLED=0

rem --- Primary: PowerShell Get-NetTCPConnection (Windows 10+) ---
for /f "usebackq delims=" %%P in (`
  powershell -NoProfile -Command "Try { Get-NetTCPConnection -LocalPort %PORT% -State Listen -ErrorAction Stop ^| Select-Object -Expand OwningProcess ^| Sort-Object -Unique } Catch { }"
`) do (
  set PID=%%P
  if not "!PID!"=="" (
    echo Found PID !PID! listening on %PORT%. Terminating...
    taskkill /PID !PID! /F >nul 2>&1
    if "!ERRORLEVEL!"=="0" (
      echo Terminated PID !PID!.
      set KILLED=1
    ) else (
      echo Failed to terminate PID !PID!.
    )
  )
)

rem --- Fallback: netstat parsing if no PID found via PowerShell ---
if "!KILLED!"=="0" (
  echo No listener found via PowerShell. Trying netstat fallback...
  for /f "tokens=5" %%P in ('netstat -ano ^| findstr /R /C:":%PORT% .*LISTENING"') do (
    set PID=%%P
    if not "!PID!"=="" (
      echo Found PID !PID! via netstat. Terminating...
      taskkill /PID !PID! /F >nul 2>&1
      if "!ERRORLEVEL!"=="0" (
        echo Terminated PID !PID!.
        set KILLED=1
      ) else (
        echo Failed to terminate PID !PID!.
      )
    )
  )
)

if "!KILLED!"=="0" (
  echo No process found listening on port %PORT%.
) else (
  echo Stop completed for port %PORT%.
)

exit /b 0