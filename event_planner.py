# UtsavAi Internship - Round 1 Submission
# Project: Vendor Recommendation & Event Planning AI

# Mock Event Input
event_type = "Wedding"
location = "Hyderabad"
budget = 120000
guest_count = 100

# Mock Vendor Data
vendors = [
    {"name": "Elite Caterers", "type": "Catering", "location": "Hyderabad", "rating": 4.5, "price_per_head": 500},
    {"name": "Flora Decors", "type": "Decoration", "location": "Hyderabad", "rating": 4.2, "price_fixed": 20000},
    {"name": "SnapMagic", "type": "Photography", "location": "Hyderabad", "rating": 4.8, "price_fixed": 30000},
    {"name": "DJ Sonic", "type": "Entertainment", "location": "Hyderabad", "rating": 4.0, "price_fixed": 15000},
    {"name": "Grand Venue", "type": "Venue", "location": "Hyderabad", "rating": 4.7, "price_fixed": 50000},
    {"name": "Urban Lens", "type": "Photography", "location": "Delhi", "rating": 4.6, "price_fixed": 25000},
    {"name": "Metro Decor", "type": "Decoration", "location": "Delhi", "rating": 4.3, "price_fixed": 18000},
]

# Vendor Recommendation Logic
selected_vendors = []
total_cost = 0

print(f"\n🎉 Event Plan for a '{event_type}' in {location}")
print(f"🪙 Budget: ₹{budget}")
print(f"👥 Guests: {guest_count}\n")

for vendor in vendors:
    if vendor["location"] == location:
        if "price_per_head" in vendor:
            cost = guest_count * vendor["price_per_head"]
        else:
            cost = vendor["price_fixed"]

        if total_cost + cost <= budget:
            selected_vendors.append({
                "name": vendor["name"],
                "type": vendor["type"],
                "cost": cost,
                "rating": vendor["rating"]
            })
            total_cost += cost

# Output Recommendations
if selected_vendors:
    print("✅ Recommended Vendors:\n")
    for v in selected_vendors:
        print(f"• {v['type']}: {v['name']} | Cost: ₹{v['cost']} | Rating: {v['rating']}")
else:
    print("⚠ No suitable vendors found within budget.")

print(f"\n🧾 Total Estimated Cost: ₹{total_cost}")
print(f"💡 Remaining Budget: ₹{budget - total_cost}")
