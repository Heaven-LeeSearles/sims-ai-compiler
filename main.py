
"""
Sims AI Messaging Mod
Main Entry Point
"""

import services
import sims4.commands

import sim_profiles


MOD_NAME = "Sims AI Messaging Mod"
VERSION = "0.2.0"


@sims4.commands.Command(
    'simsai.list_sims',
    command_type=sims4.commands.CommandType.Live
)
def list_sims(_connection=None):

    output = sims4.commands.CheatOutput(_connection)

    try:
        sim_manager = services.sim_info_manager()
        sim_infos = list(sim_manager.get_all())

        profiles = sim_profiles.build_sim_profiles(sim_infos)

        output("{}: Found {} Sims".format(
            MOD_NAME,
            len(profiles)
        ))

        for profile in profiles:

            output(
                "{} | ID: {} | Household: {} | Age: {} | Species: {} | Traits: {}".format(
                    profile["full_name"],
                    profile["sim_id"],
                    profile["household_id"],
                    profile["age"],
                    profile["species"],
                    len(profile["trait_ids"])
                )
            )

    except Exception as error:
        output("Sims AI error: {}".format(error))

