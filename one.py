def jaccard(set1, set2):
    common = len(set1 & set2)
    total = len(set1 | set2)
    if total == 0:
        return 0.0
    return common / total

purchases = {
    "Amit": ["Laptop", "Mouse", "Keyboard"],
    "Bina": ["Laptop", "Mouse", "Headphones"],
    "Chetan": ["Phone", "Charger"],
    "Divya": ["Laptop", "Keyboard", "Monitor", "Webcam"]
}

name = input("Recommend for: ").strip()

if name == "":
    print("Name cannot be empty.")
elif name not in purchases:
    print(f"Customer '{name}' not found.")
else:
    target_set = set(purchases[name])
    scores = {}
    for customer, items in purchases.items():
        if customer != name:
            scores[customer] = jaccard(target_set, set(items))

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    if all(score == 0 for _, score in sorted_scores):
        print("No similar customers found.")
        count = {}
        for items in purchases.values():
            for product in items:
                count[product] = count.get(product, 0) + 1
        popular = max(count, key=lambda x: count[x])
        print(f"Popular product: {popular} (bought by {count[popular]} customers)")
    else:
        print("Similarity scores:")
        for customer, score in sorted_scores:
            print(f"{customer} : {score:.2f}")
        most_similar = sorted_scores[0][0]
        print(f"Most similar customer: {most_similar}")
        recommended = [p for p in purchases[most_similar] if p not in target_set]
        if recommended:
            print(f"Recommended: {recommended[0]}")
        else:
            print("No new products to recommend.")