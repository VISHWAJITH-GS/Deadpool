# Initial Tools Specification

## calculator
Input: `{"expression":"25*18"}`
Use a safe parser, never unrestricted eval.
Permission: SAFE.

## time
Input: `{"timezone":"Asia/Kolkata"}`
Permission: SAFE.

## system_info
Return selected CPU/RAM/GPU/disk information.
Permission: READ.

## file_search
Input: `{"query":"requirements.txt","root":"project"}`
Restrict roots to configured directories.
Permission: READ.

## file_read
Input: `{"path":"README.md","max_chars":6000}`
Prevent path traversal outside allowed roots.
Permission: READ.

## web_search
Input: `{"query":"latest Python release"}`
Keep provider-specific code isolated.
Permission: READ.
