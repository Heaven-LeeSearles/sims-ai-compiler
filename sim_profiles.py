
"""
Sims AI Messaging Mod
Sim Profile System

Collects basic identity information from Sims.
This module does not modify Sims or save data.
"""


def _get_enum_name(value):
    if value is None:
        return None

    return getattr(value, "name", str(value))


def _get_sim_id(sim_info):
    sim_id = getattr(sim_info, "id", None)

    if sim_id is None:
        sim_id = getattr(sim_info, "sim_id", None)

    return sim_id


def _get_household_id(sim_info):
    household = getattr(sim_info, "household", None)

    if household is None:
        return None

    return getattr(household, "id", None)


def _get_trait_ids(sim_info):
    trait_ids = []

    tracker = getattr(sim_info, "trait_tracker", None)

    if tracker is None:
        return trait_ids

    traits = getattr(tracker, "equipped_traits", None)

    if traits is None:
        return trait_ids

    for trait in traits:
        trait_id = getattr(trait, "guid64", None)

        if trait_id is not None:
            trait_ids.append(int(trait_id))

    return sorted(set(trait_ids))


def build_sim_profile(sim_info):
    first_name = getattr(sim_info, "first_name", "Unknown")
    last_name = getattr(sim_info, "last_name", "")

    return {
        "sim_id": _get_sim_id(sim_info),
        "first_name": str(first_name),
        "last_name": str(last_name),
        "full_name": "{} {}".format(
            first_name,
            last_name
        ).strip(),
        "household_id": _get_household_id(sim_info),
        "age": _get_enum_name(
            getattr(sim_info, "age", None)
        ),
        "species": _get_enum_name(
            getattr(sim_info, "species", None)
        ),
        "is_human": getattr(sim_info, "is_human", None),
        "trait_ids": _get_trait_ids(sim_info)
    }


def build_sim_profiles(sim_infos):
    profiles = []

    for sim_info in sim_infos:
        try:
            profiles.append(build_sim_profile(sim_info))
        except Exception:
            continue

    return profiles
