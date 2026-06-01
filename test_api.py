import urllib.request
import json

print("Testing API endpoints on localhost:3000...")

try:
    # 1. Test Movie List Endpoint
    list_url = "http://localhost:3000/api/movies"
    print(f"GET {list_url}")
    with urllib.request.urlopen(list_url) as res:
        data = json.loads(res.read().decode('utf-8'))
        movies = data.get("data", [])
        print(f"[SUCCESS] Received {len(movies)} movies.")
        if len(movies) > 0:
            print("First movie details sample:")
            print(json.dumps(movies[0], indent=2))
            
            # Use the first movie's ID to test single movie detail
            movie_id = movies[0].get("id")
            
            # 2. Test Single Movie Detail Endpoint
            detail_url = f"http://localhost:3000/api/movies/{movie_id}"
            print(f"\nGET {detail_url}")
            with urllib.request.urlopen(detail_url) as res_det:
                detail_data = json.loads(res_det.read().decode('utf-8'))
                movie = detail_data.get("data", {})
                print(f"[SUCCESS] Found movie: {movie.get('title')}")
                print(f"Tagline: {movie.get('tagline')}")
                print(f"Runtime: {movie.get('runtime')} mins")
                print(f"Release Date: {movie.get('release_date')}")
                print(f"Vote Average: {movie.get('vote_average')}")
        else:
            print("[WARNING] Received empty movie list.")

except Exception as e:
    print("[ERROR] API verification failed with error:", e)
