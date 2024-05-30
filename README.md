This project checks websites for changes.

# Configuration
You can configure the application with a config.json.

## url
url of the website to check for changes

## elementQuery
Css-Selector for the elements to watch for

## expectedExpressions
regular expressions that have to match at least once on the text of the elements determined by elementQuery. It at least one expression does not match the user will be informed about the change.

# Example
The exampleConfig.json contains a example configuration that checks the english wikipedia page of python for a change in the current version number
