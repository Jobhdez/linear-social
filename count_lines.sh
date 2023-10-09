#!/bin/bash

# Call cloc for the specified directories and files
cloc src/interpreter/ src/python_client/ src/ws_client/ src/server/api/*.py src/server/actions/*.py src/server/chat/*.py
