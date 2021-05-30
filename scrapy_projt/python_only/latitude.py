raw_data=  {'address_components':
                 [{'long_name': '101', 'short_name': '101', 'types': ['street_number']}, {'long_name': 'Oak Street', 'short_name': 'Oak St', 'types': ['route']}, {'long_name': 'Hayes Valley', 'short_name': 'Hayes Valley', 'types': ['neighborhood', 'political']}, {'long_name': 'San Francisco', 'short_name': 'SF', 'types': ['locality', 'political']}, {'long_name': 'San Francisco County', 'short_name': 'San Francisco County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94102', 'short_name': '94102', 'types': ['postal_code']}], 'formatted_address': '101 Oak St, San Francisco, CA 94102, USA', 'geometry': {'bounds': {'northeast': {'lat': 37.77513769999999, 'lng': -122.4210453}, 'southwest': {'lat': 37.7750128, 'lng': -122.4211758}}, 'location': {'lat': 37.7750683, 'lng': -122.4210876}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.7764242302915, 'lng': -122.4197615697085}, 'southwest': {'lat': 37.7737262697085, 'lng': -122.4224595302915}}}, 'partial_match': True, 'place_id': 'ChIJZQRo4J6AhYARbQ70tvpMUfE', 'types': ['subpremise']}


data = raw_data['geometry']['location']
print(data)

