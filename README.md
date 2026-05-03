# Penguin Tests
POC sandbox to test out pytest functionality with a UI.

# VSC / Cursor
## Running tests

| Action | Commands          | Description                                                                             |
| :----------------- | ----------------- | --------------------------------------------------------------------------------------- |
| Debugger | `cmd + shift + d` | Open the debugger panel. There will be a select box near the top of the explorer panel. |
| Run Debugger | `f5`              | Execute selected configuration while pausing for all active breakpoints                 |
| Run Debugger w/o breakpoints | `ctrl + f5`       | Executed selected configuration ignoring all breakpoints                                |
| Execute Test File | ` cmd + ;` <br> `cmd + shift + f` | Executes test in the current file |
| Debug Test File | ` cmd + ;` <br> `cmd  + f` | Debugs test in the current file |


# Thoughts
- Using Cursor's test execution is quite nice because it uses the lower panel with current and historical runs
![Testing Panel](assets/test-panel.png)



| Packages          | My Thoughts                                                                             |
| ----------------- | --------------------------------------------------------------------------------------- |
| pytest-html | HTML display seems to get good details but it's not very pretty. |
| pytest-csv              | Exporting CSV might be a great way to consolidate distributed test executions.                 |
| allure-pytest       | None                                |


# TODO
- Disply aggregations of multiple test executions (emulate distributed testing framework).
- Display test executions over time to view patterns
