#!/bin/bash

JSON_FILE="broadcast/resources/test_environment.postman_environment.json"
PROPERTIES_FILE="./config.properties"
TEMP_FILE="${JSON_FILE}.tmp"

sed -i 's/[[:space:]]*$//' "$PROPERTIES_FILE"

# Werte aus der .properties-Datei lesen
COM_OTHER_UUID=$(grep -oP '^COM_OTHER_UUID=\K.*' "$PROPERTIES_FILE" | tr -d '\n')
COM_OTHER_IP=$(grep -oP '^COM_OTHER_IP=\K.*' "$PROPERTIES_FILE" | tr -d '\n')
COM_OTHER_TCP=$(grep -oP '^COM_OTHER_TCP=\K.*' "$PROPERTIES_FILE" | tr -d '\n')

awk -v tcp="$COM_OTHER_TCP" \
    -v ip="$COM_OTHER_IP" \
    -v uuid="$COM_OTHER_UUID" '
{
    print
    if ($0 ~ /"key": "COM_OTHER_UUID"/) {
        getline
        sub(/"value": "[^"]*"/, "\"value\": \"" uuid "\"")
        print
    } else if ($0 ~ /"key": "COM_OTHER_IP"/) {
        getline
        sub(/"value": "[^"]*"/, "\"value\": \"" ip "\"")
        print
    } else if ($0 ~ /"key": "COM_OTHER_TCP"/) {
        getline
        sub(/"value": "[^"]*"/, "\"value\": \"" tcp "\"")
        print
    }
}' "$JSON_FILE" | sed 's/\([0-9]*\)[[:space:]]*\n/\1/' > "$TEMP_FILE"


if [[ -f "$TEMP_FILE" ]]; then
    mv "$TEMP_FILE" "$JSON_FILE"
    echo "Changes applied successfully!"
else
    echo "Error processing file."
fi