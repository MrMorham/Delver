from ast import Try
from utility.Monster import Monster
from utility.Sites import Sites

site = Sites()
monster = Monster()

new_location = site.create_site(5)
creature = monster.get_monster(100)

def format_denizen(place):
    return str(
        """
        Denizen: 
            Challenge: {challenge}
            Form: {form}
            Size: {size}
            Features: {features}
            Abilities: {abilities}
        """.format(
            challenge = place["danger"]["denizen"].get("challenge"),
            form = place["danger"]["denizen"].get("form"),
            size = place["danger"]["denizen"].get("size"),
            features = place["danger"]["denizen"].get("features"),
            abilities = place["danger"]["denizen"].get("abilities")
            )
        )

print(
    """
    {} ({} {})
    """.format(new_location["name"], new_location["theme_display"], new_location["domain_display"])
)

area_count = 1

for place in new_location["map"].values():
    print("""        Area {count}
        Feature: {feature} ({aspect} / {focus})
        Danger: {danger}
        {denizen}
        ============================================
        """.format(
            count = area_count,
            feature = place["feature"]["description"],
            aspect = place["feature"]["aspect"],
            focus = place["feature"]["focus"],
            danger = place["danger"]["description"],
            denizen = format_denizen(place) if place["danger"]["denizen"].get("challenge") else ""
            )
    )
    area_count += 1
