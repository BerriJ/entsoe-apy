#!/bin/sh

rm -rf ./misc/endpoints

# Input file path
POSTMAN_FILE=./misc/TransparencyPlatformRestfulAPI.postman_collection.json

# Create endpoint-specific JSON files organized by category
echo "Creating endpoint-specific JSON files..."

# Get all categories (top-level items with sub-items)
jq -c '.item[] | select(.item) | {name: .name, items: .item}' "$POSTMAN_FILE" | while IFS= read -r category; do
    category_name=$(printf '%s\n' "$category" | jq -r '.name')
    
    # Create category directory
    mkdir -p "./misc/endpoints/$category_name"
    
    # Process each endpoint in the category (only GET methods)
    printf '%s\n' "$category" | jq -c '.items[] | select(.request.method == "GET")' | while IFS= read -r endpoint; do
        endpoint_name=$(printf '%s\n' "$endpoint" | jq -r '.name // empty')
        
        # Skip if endpoint has no name or name is null
        if [ -n "$endpoint_name" ] && [ "$endpoint_name" != "null" ]; then
            # Write endpoint to individual JSON file with filtered fields
            # Extract query parameters and clean up descriptions
            printf '%s\n' "$endpoint" | jq '{
                name: .name, 
                method: .request.method, 
                query: ((.request.urlObject.query // .request.url.query) | map({
                    key: .key,
                    value: .value,
                    description: (if .description.content then (.description.content | gsub("<[^>]*>"; "") | gsub("\\n"; " ") | gsub("^\\s+|\\s+$"; "")) else .description end),
                    disabled: .disabled
                } | if .disabled then . else del(.disabled) end))
            }' > "./misc/endpoints/$category_name/$endpoint_name.json"
            echo "  Created: ./misc/endpoints/$category_name/$endpoint_name.json"
        fi
    done
done

echo "Done! Endpoint JSON files created in misc/endpoints/"

jq '[.item[] | select(.item) | {name, items: [.item[] | select(.request.method == "GET") | .name]}]' "$POSTMAN_FILE" > ./misc/endpoints/all_endpoints.json

# Extract and display the names of all Endpoints from a Postman collection JSON file
echo -e 'To regenerate this list, run:\n\n ```sh\n./misc/get_postman.sh \n./misc/process_postman.sh \n ```\n' > misc/endpoints/README.md

jq -r '.item[] | select(.item) | .name as $cat | "## [\($cat)](\($cat | @uri))", (.item[] | select(.name) | select(.request.method == "GET") | "- [\(.name)](\($cat | @uri)/\(.name | @uri).json)"), ""' "$POSTMAN_FILE" >> misc/endpoints/README.md