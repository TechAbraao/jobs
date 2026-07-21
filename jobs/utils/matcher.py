def calculate_match(job: dict, keywords: list[str]):
    text = (
        job["name"]
        + "\n"
        + job["description"]
    ).lower()

    found = []

    for keyword in keywords:
        if keyword.lower() in text:
            found.append(keyword)

    score = (len(found) / len(keywords) * 100) if keywords else 0

    return score, found