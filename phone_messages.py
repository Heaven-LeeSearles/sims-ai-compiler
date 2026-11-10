"""
Sims AI Messaging Mod
Custom Phone Messages Interaction
"""

import os

from interactions.base.immediate_interaction import ImmediateSuperInteraction


class SimsAIMessagesInteraction(ImmediateSuperInteraction):

    def _run_interaction_gen(self, timeline):

        yield from super()._run_interaction_gen(timeline)

        try:
            home = os.path.expanduser("~")

            log_path = os.path.join(
                home,
                "Documents",
                "Electronic Arts",
                "The Sims 4",
                "sims_ai_phone_test.txt"
            )

            actor = getattr(self, "sim", None)
            sim_info = getattr(actor, "sim_info", None)

            sim_name = "Unknown Sim"

            if sim_info is not None:
                sim_name = "{} {}".format(
                    getattr(sim_info, "first_name", ""),
                    getattr(sim_info, "last_name", "")
                ).strip()

            with open(log_path, "w") as log:
                log.write("Sims AI phone interaction activated!\n")
                log.write("Selected by: {}\n".format(sim_name))

        except Exception:
            pass