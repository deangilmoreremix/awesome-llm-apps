#!/bin/bash

# Test if the instant_lab wrappers work
echo "=== Testing instant_lab wrappers ==="

# Test one of the apps
test_app="ai_travel_agent"
wrapper_path="app_modules/instant_lab/${test_app}/app/main.py"

echo "Testing: $test_app"
echo "Wrapper path: $wrapper_path"

if [ -f "$wrapper_path" ]; then
    echo "✓ Wrapper exists"
    
    # Try to import and run the main function
    python3 -c "
import sys
import os
sys.path.insert(0, '$wrapper_path')
try:
    import main
    print('✓ Main module imported successfully')
    if hasattr(main, 'main'):
        print('✓ main() function exists')
        print('✓ Wrapper appears to be working')
    else:
        print('✗ main() function missing')
except Exception as e:
    print(f'✗ Import failed: {e}')
"
else
    echo "✗ Wrapper not found"
fi

echo "=== Test complete ==="