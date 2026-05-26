from dataset import data

def get_recommendations(user_input):

    user_input = user_input.lower()

    recommendations = []

    for category, items in data.items():

        if category in user_input:

            recommendations.extend(items)

    if not recommendations:

        recommendations.append(
            "No matching recommendations found."
        )

    return recommendations