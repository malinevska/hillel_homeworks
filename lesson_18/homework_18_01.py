import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

# print("1. Searching for images of the Curiosity rover...")
search_response = requests.get(search_url, params=search_params)
search_data = search_response.json()
items = search_data.get("collection", {}).get("items", [])

nasa_ids = [
    items[0]["data"][0]["nasa_id"],
    items[1]["data"][0]["nasa_id"]
]
# print(f"   Found nasa_id for download: {nasa_ids}\n")

for index, nasa_id in enumerate(nasa_ids, start=1):
    # print(f"2. Fetching data for image {index} (ID: {nasa_id})...")

    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    asset_response = requests.get(asset_url)
    asset_data = asset_response.json()

    file_items = asset_data.get("collection", {}).get("items", [])

    jpg_url = None
    for item in file_items:
        href = item.get("href", "")
        if href.endswith(".jpg"):
            jpg_url = href
            break

    if jpg_url:
        jpg_url = jpg_url.replace(" ", "%20")

        # print(f"   Downloading file: {jpg_url}")
        img_response = requests.get(jpg_url)

        filename = f"mars_photo{index}.jpg"
        with open(filename, "wb") as file:
            file.write(img_response.content)

    #     #print(f"   ✅ Successfully saved as {filename}\n")
    # else:
    #     #print(f"   ❌ JPG image for {nasa_id} not found.\n")

# print("Script finished")