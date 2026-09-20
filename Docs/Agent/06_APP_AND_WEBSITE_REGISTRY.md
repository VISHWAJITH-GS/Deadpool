# App and Website Registry

Application example:

```json
{
  "id": "chrome",
  "name": "Google Chrome",
  "aliases": ["chrome", "google chrome"],
  "type": "app",
  "executable": "chrome.exe"
}
```

Website example:

```json
{
  "id": "leetcode",
  "name": "LeetCode",
  "aliases": ["leetcode", "leet code"],
  "type": "website",
  "url": "https://leetcode.com"
}
```

Requirements:
- discover installed applications once and cache results
- refresh on demand
- support user aliases
- support user websites
- never scan the whole disk for every command
- use direct URLs for registered websites
