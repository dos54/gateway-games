import json

# Input JSON data
data = [
    {
        "url": "/images/dice-with-bags.jpg",
        "alt": "Dice With Bags",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/dice-sets-4.jpg",
        "alt": "Dice Sets 4",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/display-3.jpg",
        "alt": "Display 3",
        "aspectRatio": "aspect-four-to-three"
    },
    {
        "url": "/images/gateway-games-flag.jpg",
        "alt": "Gateway Games Flag",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/magic-display-1.jpg",
        "alt": "Magic Display 1",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/tabletop-games-wall.jpg",
        "alt": "Tabletop Games Wall",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/dice-sets.jpg",
        "alt": "Dice Sets",
        "aspectRatio": "aspect-four-to-three"
    },
    {
        "url": "/images/warhammer-2.jpg",
        "alt": "Warhammer 2",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/display-2.jpg",
        "alt": "Display 2",
        "aspectRatio": "aspect-four-to-three"
    },
    {
        "url": "/images/tabletop-games-wall-2.jpg",
        "alt": "Tabletop Games Wall 2",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/display-1.jpg",
        "alt": "Display 1",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/dice-sets-2.jpg",
        "alt": "Dice Sets 2",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/books-wall.jpg",
        "alt": "Books Wall",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/tabeltop-games-display.jpg",
        "alt": "Tabeltop Games Display",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/magic-decks.jpg",
        "alt": "Magic Decks",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/store-from-entrance.jpg",
        "alt": "Store From Entrance",
        "aspectRatio": "aspect-nine-to-four"
    },
    {
        "url": "/images/dice-sets-5.jpg",
        "alt": "Dice Sets 5",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/wrapped-dice.jpg",
        "alt": "Wrapped Dice",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/storefront.jpg",
        "alt": "Storefront",
        "aspectRatio": "aspect-nine-to-four"
    },
    {
        "url": "/images/magic-folder.jpg",
        "alt": "Magic Folder",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/display-4.jpg",
        "alt": "Display 4",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/warhammer.jpg",
        "alt": "Warhammer",
        "aspectRatio": "aspect-four-to-three"
    },
    {
        "url": "/images/bones.jpg",
        "alt": "Bones",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/hippie-duck.jpg",
        "alt": "Hippie Duck",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/books-display.jpg",
        "alt": "Books Display",
        "aspectRatio": "aspect-one-to-one"
    },
    {
        "url": "/images/dice-sets-3.jpg",
        "alt": "Dice Sets 3",
        "aspectRatio": "aspect-one-to-one"
    }
]

# Add `low_res_url` attribute
for item in data:
    # Extract the filename from the `url`
    filename = item["url"].split("/")[-1]
    # Add the `low_res_url` field
    item["low_res_url"] = f"/images/resized/{filename}"

# Convert the updated data to a JSON string
output_json = json.dumps(data, indent=4)

# Save the updated JSON to a file
with open("updated_images.json", "w") as f:
    f.write(output_json)

print("Updated JSON saved to 'updated_images.json'")
