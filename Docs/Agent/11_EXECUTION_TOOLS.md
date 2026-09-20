# Execution Tools

Registered tools only.

App:
- launch_app(app_id)
- focus_app(app_id)
- close_app(app_id)

Browser:
- open_url(url)
- focus_browser()
- browser_back()
- browser_forward()
- browser_refresh()

Keyboard:
- press_key(key)
- hotkey(keys)
- type_text(text)

Mouse:
- click(target)
- double_click(target)
- right_click(target)
- scroll(direction, amount)
- move(target)

Observation:
- get_active_window()
- get_ui_tree()
- get_screenshot()

The LLM cannot invent tool names. Every tool has an argument schema, risk level, executor and verification strategy.
