from typing import List, Dict

from social_distancing_sim.agent.agent_base import AgentBase
from social_distancing_sim.environment.observation_space import ObservationSpace


class VaccinationAgent(AgentBase):
    """VaccinationAgent randomly vaccinates clear nodes."""
    @property
    def available_actions(self) -> List[str]:
        """Isolation agent can only isolate. It can't even un-isolate (yet?)"""
        return ['vaccinate']

    @staticmethod
    def available_targets(obs: ObservationSpace) -> List[int]:
        return list(set(obs.current_clear_nodes).difference(obs.current_immune_nodes))

    def select_actions(self, obs: ObservationSpace) -> Dict[int, str]:
        # Don't track sample call here as self.get_actions() will handle that.
        return self.sample(obs,
                           track=False)