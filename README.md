# paloalto-rss-monitor
monitors the palo alto security advisories page for new entires with your chosen string. (technically it monitors the json, since their rss seems outdated)

# requirements

- python3
- urllib.request
- pymsteams (if send to Teams is required)

# usage

this script runs in an infinite while loop, so its best to run in a screen or docker container