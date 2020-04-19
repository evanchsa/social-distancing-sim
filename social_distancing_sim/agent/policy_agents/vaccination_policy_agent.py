from typing import List, Dict

from social_distancing_sim.agent.agent_base import AgentBase
from social_distancing_sim.environment.observation_space import ObservationSpace


class VaccinationPolicyAgent(AgentBase):
    """
    Vaccination applies vaccination during a set time period.

    Unlike VaccinationAgent, vaccinates any clear node even if they have some immunity.

    It can be used to model availability of a vaccine, for max or staggered use.

     0         start['vaccinate']         end['vaccinate']
    |   Does nothing   |   Isolates ANY node      |      Does nothing ...
    """

    @property
    def available_actions(self) -> List[str]:
        """Isolation agent can only isolate. It can't even un-isolate (yet?)"""
        return ['vaccinate']

    @staticmethod
    def available_targets(obs: ObservationSpace) -> List[int]:
        """Same as VaccinationAgent."""
        return list(set(obs.current_clear_nodes))

    def select_actions(self, obs: ObservationSpace) -> Dict[int, str]:
        if len(self.currently_active_actions) > 0:
            # Don't track sample call here as self.get_actions() will handle that.
            return self.sample(obs,
                               track=False)
        else:
            return {}