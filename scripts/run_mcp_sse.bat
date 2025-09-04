@echo off
setlocal ENABLEDELAYEDEXPANSION

REM Resolve repo root as the parent of this script directory
pushd "%~dp0\.."

REM Optional: activate venv if present
if exist ".venv\Scripts\activate.bat" (
  call ".venv\Scripts\activate.bat"
)

REM Default port if not provided
if "%MCP_SERVER_PORT%"=="" set MCP_SERVER_PORT=3000

echo.
echo Pinecone KB MCP Server - Local SSE
echo Repo: %CD%
echo Port: %MCP_SERVER_PORT%
if "%MCP_API_KEY%"=="" (
  echo Warning: MCP_API_KEY not set; SSE clients will be unauthorized.
) else (
  echo MCP_API_KEY is set.
)
if "%OPENAI_API_KEY%"=="" (
  echo Warning: OPENAI_API_KEY not set; embedding may fail.
) else (
  echo OPENAI_API_KEY is set.
)
if "%PINECONE_API_KEY%"=="" (
  echo Warning: PINECONE_API_KEY not set; Pinecone operations may fail.
) else (
  echo PINECONE_API_KEY is set.
)

echo.
echo Starting server...
python mcp-server\mcp_pinecone_server.py --cloud --port %MCP_SERVER_PORT%

popd
endlocal