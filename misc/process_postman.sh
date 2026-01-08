#!/bin/sh

rm -rf ./misc/endpoints

# Input file path
POSTMAN_FILE=./misc/TransparencyPlatformRestfulAPI.postman_collection.json

# Base directory for all endpoints
BASE_DIR="./misc/endpoints"

# Create base directory
mkdir -p "$BASE_DIR"

# Function to sanitize path components to prevent path traversal
sanitize_path_component() {
    local input="$1"
    
    # Reject if empty, null, or contains null byte
    if [ -z "$input" ] || [ "$input" = "null" ] || echo "$input" | grep -q $'\0'; then
        return 1
    fi
    
    # Reject if starts with slash (absolute path) or dash (command option)
    if echo "$input" | grep -q '^[/-]'; then
        return 1
    fi
    
    # Reject if contains path traversal sequences or other dangerous characters
    if echo "$input" | grep -qE '(\.\./|/\.\.|^\.\.(/|$)|/|\\|\$|`|\||;|&|<|>|\(|\)|\{|\}|\[|\]|\*|\?|~|#|!|%|\^)'; then
        return 1
    fi
    
    # Accept only alphanumeric characters, spaces, hyphens, underscores, and periods (not at start)
    if ! echo "$input" | grep -qE '^[A-Za-z0-9_][A-Za-z0-9_ .-]*$'; then
        return 1
    fi
    
    return 0
}

# Create endpoint-specific JSON files organized by category
echo "Creating endpoint-specific JSON files..."

# Get all categories (top-level items with sub-items)
# Note: jq may output parse errors to stderr from malformed response examples in the collection.
# These errors are harmless and do not affect the extraction of category/endpoint metadata.
jq -c '.item[] | select(.item) | {name: .name, items: .item}' "$POSTMAN_FILE" | while read -r category; do
    category_name=$(printf '%s\n' "$category" | jq -r '.name')
    
    # Validate category name to prevent path traversal
    if ! sanitize_path_component "$category_name"; then
        echo "WARNING: Skipping invalid category name: $category_name" >&2
        continue
    fi
    
    # Create category directory with validated name
    category_dir="$BASE_DIR/$category_name"
    mkdir -p "$category_dir"
    
    # Process each endpoint in the category (only GET methods)
    printf '%s\n' "$category" | jq -c '.items[] | select(.request.method == "GET")' | while read -r endpoint; do
        endpoint_name=$(printf '%s\n' "$endpoint" | jq -r '.name // empty')
        
        # Validate endpoint name to prevent path traversal
        if ! sanitize_path_component "$endpoint_name"; then
            echo "WARNING: Skipping invalid endpoint name: $endpoint_name" >&2
            continue
        fi
        
        # Write endpoint to individual JSON file with filtered fields
        # Extract query parameters and clean up descriptions
        endpoint_file="$category_dir/$endpoint_name.json"
        printf '%s\n' "$endpoint" | jq '{
            name: .name, 
            method: .request.method, 
            query: ((.request.urlObject.query // .request.url.query) | map({
                key: .key,
                value: .value,
                description: (if .description.content then (.description.content | gsub("<[^>]*>"; "") | gsub("\\n"; " ") | gsub("^\\s+|\\s+$"; "")) else .description end),
                disabled: .disabled
            } | if .disabled then . else del(.disabled) end))
        }' > "$endpoint_file"
        echo "  Created: $endpoint_file"
    done
done

echo "Done! Endpoint JSON files created in misc/endpoints/"

jq '[.item[] | select(.item) | {name, items: [.item[] | select(.request.method == "GET") | .name]}]' "$POSTMAN_FILE" > "$BASE_DIR/all_endpoints.json"

# Extract and display the names of all Endpoints from a Postman collection JSON file
echo -e 'To regenerate this list, run:\n\n ```sh\n./misc/get_postman.sh \n./misc/process_postman.sh \n ```\n' > "$BASE_DIR/README.md"

jq -r '.item[] | select(.item) | .name as $cat | "## [\($cat)](\($cat | @uri))", (.item[] | select(.name) | select(.request.method == "GET") | "- [\(.name)](\($cat | @uri)/\(.name | @uri).json)"), ""' "$POSTMAN_FILE" >> "$BASE_DIR/README.md"