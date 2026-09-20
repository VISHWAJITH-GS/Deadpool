# Deadpool Desktop Agent — Product Specification

## Goal
Build a lightweight Windows desktop agent that accepts natural-language goals and safely operates the laptop.

Required capabilities:
- Open installed applications
- Open/navigate websites
- Execute multi-step tasks
- Understand goals
- Control mouse and keyboard
- Observe the screen
- Understand UI elements
- Verify actions
- Ask for confirmation for risky actions
- Recover from safe failures
- Remain fast and lightweight

Example: "Open Chrome, go to LeetCode, find Two Sum."

Expected:
1. Resolve Chrome as an app.
2. Launch/focus Chrome.
3. Resolve LeetCode as a website.
4. Navigate directly to LeetCode.
5. Observe the resulting UI.
6. Find/search for Two Sum.
7. Verify the requested page is open.
8. Stop and report the verified result.

Non-goals for v1:
- Android control
- unrestricted shell execution
- autonomous destructive actions
- continuous screen recording
- full multimodal model stack
- cloud dependency for normal operation
