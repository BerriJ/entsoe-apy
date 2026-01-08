#!/usr/bin/env bash

# Input file path
POSTMAN_FILE="./misc/Transparency Platform Restful API.postman_collection.json"

# Create endpoint-specific JSON files organized by category
echo "Creating endpoint-specific JSON files..."

# Get all categories (top-level items with sub-items)
jq -c '.item[] | select(.item) | {name: .name, items: .item}' "$POSTMAN_FILE" | while read -r category; do
    category_name=$(echo "$category" | jq -r '.name')
    
    # Create category directory
    mkdir -p "./misc/endpoints/$category_name"
    
    # Process each endpoint in the category
    echo "$category" | jq -c '.items[]' | while read -r endpoint; do
        endpoint_name=$(echo "$endpoint" | jq -r '.name // empty')
        
        # Skip if endpoint has no name or name is null
        if [ -n "$endpoint_name" ] && [ "$endpoint_name" != "null" ]; then
            # Write endpoint to individual JSON file with filtered fields
            echo "$endpoint" | jq '{name: .name, method: .request.method, query: .request.url.query}' > "./misc/endpoints/$category_name/$endpoint_name.json"
            echo "  Created: ./misc/endpoints/$category_name/$endpoint_name.json"
        fi
    done
done

echo "Done! Endpoint JSON files created in misc/endpoints/"

jq '[.item[] | select(.item) | {name, items: [.item[].name]}]' "$POSTMAN_FILE" > ./misc/endpoints/all_endpoints.json

# Extract and display the names of all Endpoints from a Postman collection JSON file
echo -e "Endpoints extracted from Postman collection on $(date +"%Y-%m-%d"):\n" > misc/endpoints/README.md
"$POSTMAN_FILE"
echo -e 'To regenerate this list, run:\n\n ```sh\n./misc/process_postman.sh \n ```\n' >> misc/endpoints/README.md

jq -r '.item[] | select(.item) | .name as $cat | "## [\($cat)](\($cat | @uri))", (.item[] | select(.name) | "- [\(.name)](\($cat | @uri)/\(.name | @uri).json)"), ""' "$POSTMAN_FILE" >> misc/endpoints/README.md