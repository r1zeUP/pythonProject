import json


def load_candidates_from_json():
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def get_all_candidate():
    return load_candidates_from_json()


def get_candidate(candidate_id):
    for candidate in load_candidates_from_json():
        if candidate["id"] == candidate_id:
            return candidate
    return


def get_candidates_by_name(candidate_name):
    result = []
    for candidate in load_candidates_from_json():
        if candidate_name.lower() in candidate["name"].lower():
            result.append(candidate)
    return result


def get_candidates_by_skill(skill):
    result = []
    for candidate in load_candidates_from_json():
        skills = candidate["skills"].lower().split(", ")
        if skill in skills:
            result.append(candidate)
    return result
