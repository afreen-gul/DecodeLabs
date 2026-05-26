from dataset import items

def recommend_items(user_input):

    user_keywords = user_input.lower().split()

    recommendations = []

    for item in items:

        score = 0

        matched_keywords = []

        for keyword in user_keywords:

            if keyword in item["tags"]:
                score += 2
                matched_keywords.append(keyword)

            if keyword == item["category"]:
                score += 3

        if score > 0:

            confidence = min(score * 15, 100)

            recommendations.append({

                "title": item["title"],
                "category": item["category"],
                "rating": item["rating"],
                "score": score,
                "confidence": confidence,
                "matched": matched_keywords
            })

    recommendations.sort(
        key=lambda x: (x["score"], x["rating"]),
        reverse=True
    )

    return recommendations[:6]