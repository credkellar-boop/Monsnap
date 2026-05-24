import os
from google import genai
import googlemaps


class IntelEngine:
    """Combines Google Maps Spatial Intel, Gemini Multimodal Vision, and People Search."""

    def __init__(self, camera_lat=34.0522, camera_lng=-118.2437):
        # Initialize Google Maps Client (Requires GOOGLE_MAPS_API_KEY env var)
        self.gmaps = googlemaps.Client(key=os.environ.get("GOOGLE_MAPS_API_KEY"))
        
        # Initialize modern Gemini GenAI Client (Looks for GEMINI_API_KEY env var automatically)
        self.ai_client = genai.Client()
        
        # Camera physical coordinates
        self.lat = camera_lat
        self.lng = camera_lng
        
        # Resolve real address using Google Maps Geocoding API immediately
        self.location_address = self._resolve_camera_address()

    def _resolve_camera_address(self):
        try:
            reverse_geocode = self.gmaps.reverse_geocode((self.lat, self.lng))
            if reverse_geocode:
                return reverse_geocode[0]["formatted_address"]
            return "Unknown Geolocation"
        except Exception as e:
            return f"Maps Error: {str(e)}"

    def local_people_search(self, face_id):
        """Mock People Search Directory database lookup.
        
        In production, connect this method to an enterprise CRM, SQL DB, or HR system.
        """
        directory_database = {
            "user_001": {
                "name": "Jane Doe",
                "role": "Security Personnel",
                "clearance": "Level 3",
            },
            "user_002": {
                "name": "John Smith",
                "role": "Contractor",
                "clearance": "Level 1",
            }
        }
        return directory_database.get(face_id, {"name": "Unknown Person", "role": "Visitor", "clearance": "None"})

    def analyze_situation_with_gemini(self, frame_path, target_person_name):
        """Passes the image frame to Gemini to evaluate contextual threat levels."""
        try:
            # Upload the snapped frame to Gemini File API
            uploaded_file = self.ai_client.files.upload(file=frame_path)
            
            prompt = (
                f"Analyze this security camera frame taken at {self.location_address}. "
                f"The person in focus has been identified by internal records as {target_person_name}. "
                f"Describe their actions, visible expressions, clothing details, and provide a threat assessment status."
            )
            
            # Using the fast, production-ready multimodal flash model
            response = self.ai_client.models.generate_content(
                model="gemini-2.5-flash",
                contents=[uploaded_file, prompt]
            )
            return response.text
        except Exception as e:
            return f"Gemini Analysis Error: {str(e)}"
