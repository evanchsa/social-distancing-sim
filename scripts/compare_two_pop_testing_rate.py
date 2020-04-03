from social_distancing_sim.disease.disease import Disease
from social_distancing_sim.population.graph import Graph
from social_distancing_sim.population.healthcare import Healthcare
from social_distancing_sim.population.observation_space import ObservationSpace
from social_distancing_sim.population.population import Population

if __name__ == "__main__":
    disease = Disease(name='COVID-19')
    healthcare = Healthcare()

    pop_close_tested = Population(name='A herd of cats',
                                  disease=disease,
                                  healthcare=healthcare,
                                  observation_space=ObservationSpace(graph=Graph(community_n=40,
                                                                                 community_size_mean=16,
                                                                                 seed=123),
                                                                     test_rate=1))

    pop_close_untested = Population(name='A herd of cats, observed',
                                    disease=disease,
                                    healthcare=healthcare,
                                    observation_space=ObservationSpace(graph=Graph(community_n=40,
                                                                                   community_size_mean=16,
                                                                                   seed=123),
                                                                       test_rate=0.04))

    pop_distanced_tested = Population(name='A socially responsible population',
                                      disease=disease,
                                      healthcare=healthcare,
                                      observation_space=ObservationSpace(graph=Graph(community_n=40,
                                                                                     community_size_mean=16,
                                                                                     community_p_in=0.05,
                                                                                     community_p_out=0.04,
                                                                                     seed=123),
                                                                         test_rate=1))

    pop_distanced_untested = Population(name='A socially responsible population, observed',
                                        disease=disease,
                                        healthcare=healthcare,
                                        observation_space=ObservationSpace(graph=Graph(community_n=40,
                                                                                       community_size_mean=16,
                                                                                       community_p_in=0.05,
                                                                                       community_p_out=0.04,
                                                                                       seed=123),
                                                                           test_rate=0.04))

    pop_close_tested.run(steps=130,
                         plot=False)
    pop_close_tested.replay(duration=0.1)

    pop_close_untested.run(steps=130,
                           plot=False)
    pop_close_untested.replay(duration=0.1)

    pop_distanced_tested.run(steps=130,
                             plot=False)
    pop_distanced_tested.replay(duration=0.1)

    pop_distanced_untested.run(steps=130,
                               plot=False)
    pop_distanced_untested.replay(duration=0.1)
