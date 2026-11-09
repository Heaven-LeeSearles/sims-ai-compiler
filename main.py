
"""
Sims AI Messaging Mod
Sim Profile Detection Test
"""

import services
import sims4.commands


@sims4.commands.Command(
    'simsai.list_sims',
    command_type=sims4.commands.CommandType.Live
)
def list_sims(_connection=None):

    output = sims4.commands.CheatOutput(_connection)

    try:
        sim_manager = services.sim_info_manager()
        sims = list(sim_manager.get_all())

        output("Sims AI: Found {} Sims".format(len(sims)))

        for sim in sims:
            first = getattr(sim, "first_name", "Unknown")
            last = getattr(sim, "last_name", "")
            sim_id = getattr(sim, "id", "Unknown")

            household = getattr(sim, "household", None)
            household_id = getattr(household, "id", "None")

            output(
                "{} {} | Sim ID: {} | Household ID: {}".format(
                    first,
                    last,
                    sim_id,
                    household_id
                )
            )

    except Exception as error:
        output("Sims AI error: {}".format(error))
